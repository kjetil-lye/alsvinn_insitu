#include "dll_adaptor.hpp"
#include "parameters.hpp"
#include "data.hpp"
#include "isosurfaceVtkPipeline.hpp"

#include <fstream>
#include <limits>
#include <iomanip>
#include <iostream>
#include <vtkCPDataDescription.h>
#include <vtkCPInputDataDescription.h>
#include <vtkCPProcessor.h>
#include <vtkCPPythonScriptPipeline.h>
#include <vtkDoubleArray.h>
#include <vtkImageData.h>
#include <vtkNew.h>
#include <vtkPointData.h>
#include <vtkPoints.h>



// Simple macro to print parameters
#define PRINT_PARAM(X) std::cout << "Value of " << #X << " is " << X << std::endl
extern "C" {

vtkCPProcessor* Processor = NULL;
vtkImageData* VTKGrid = NULL;

DLL_ADAPTOR_EXPORT void* create(const char* simulator_name,
                                const char* simulator_version, void* parameters) {


        auto my_parameters = static_cast<MyParameters*>(parameters);
        const std::string version = my_parameters->getParameter("basename");


        // Initialize catalyst, set processes
        if (Processor == NULL)
        {
                Processor = vtkCPProcessor::New();
                Processor->Initialize();
        }
        else
        {
                Processor->RemoveAllPipelines();
        }


        if(false) //version=="meanVar")
        {
                int outputFrequency=1;
                std::string name = "out";
                vtkNew<isosurfaceVtkPipeline> pipelinevtk;
                pipelinevtk->Initialize(outputFrequency, name);
                Processor->AddPipeline(pipelinevtk);

        }
        else
        {
                //default script
                const char *script_default = "../pythonScripts/gridwriter.py";

                vtkNew<vtkCPPythonScriptPipeline> pipeline;
                pipeline->Initialize(script_default);
                Processor->AddPipeline(pipeline);

                // png etc script
                const std::string script_str = my_parameters->getParameter("catalystscript");
                const char *script_loc = script_str.c_str();

                if(script_str =="none")
                {
                        std::cout<<"only default pipeline script: "<< script_default<<std::endl;
                }
                else
                {
                        std::cout<<"pipeline script: "<< script_loc<<std::endl;
                        pipeline->Initialize(script_loc);
                        Processor->AddPipeline(pipeline);
                }

        }

        return static_cast<void*>(new MyData);
}


DLL_ADAPTOR_EXPORT void delete_data(void* data) {
        std::cout << "In delete_data" << std::endl;
        if (Processor)
        {
                Processor->Delete();
                Processor = NULL;
        }
        if (VTKGrid)
        {
                VTKGrid->Delete();
                VTKGrid = NULL;
        }
        delete static_cast<MyData*>(data);
}


/**
 * CatalystCoProcess
 * @param nx, ny, nz are number of cells in respective direction
 * @param ngx, ngy, ngz are number of ghost cells in respective direction
 */
DLL_ADAPTOR_EXPORT void CatalystCoProcess(void* data, void* parameters, double time,
                                          const char* variable_name,  double* variable_data, int nx, int ny, int nz,
                                          int ngx, int ngy, int ngz, double ax, double ay, double az, double bx,
                                          double by, double bz, int gpu_number ) {



//asuming only one variable: rho:
        if(std::string(variable_name)=="rho")
        {
                auto my_data = static_cast<MyData*>(data);
                auto my_parameters = static_cast<MyParameters*>(parameters);
                //  auto timeStep = my_data->getCurrentTimestep();
                //    const std::string description_namestr = my_parameters->getParameter("basename");        const char *description_name = description_namestr.c_str();

                int mpi_rank;
                MPI_Comm_rank(my_parameters->getMPIComm(), &mpi_rank);
                int mpi_size;
                MPI_Comm_size(my_parameters->getMPIComm(), &mpi_size);

                //check if we can run all in parallel:
                 int nsamples = std::stoi(my_parameters->getParameter("samples"));
                if(mpi_size <=  nsamples) {
                        std::cerr<< "WARNING: NOT ENOUGH MPI NODES, reduce sample size to number of NODES: "<< mpi_size<<std::endl;
                }


                          //    if(mpi_rank == 0) ?
                vtkCPDataDescription* dataDescription = vtkCPDataDescription::New();
                dataDescription->SetTimeData(my_data->getCurrentTime(), my_data->getCurrentTimestep());
                dataDescription->AddInput("input");

                size_t ndata = (ngx*2+nx)*(ny+2*ngy)*(nz+2*ngz);    //(nz+ngz-1)*(nx+2*ngx)*(ny+2*ngy)+(ny+ngy-1)*(nx*2*ngx)+(nx+ngx-1); //nx*ny*nz
                double* avrg_data;
                if(mpi_size>1) {
                        MPI_Reduce(variable_data, avrg_data, ndata, MPI_DOUBLE, MPI_SUM, 0, my_parameters->getMPIComm());
                }else{
                        //treat as seperate sampels
                        avrg_data = variable_data;
                        nsamples = 1;
                }



                if(mpi_rank == 0)
                {

                        // the last time step shuld always be output
                        //either we are looking at new variable or new timestep or the last time step
                        if( my_data->isNewVariable(variable_name) || my_data->isNewTimestep() || my_data->isEndTimestep() ) {
                                dataDescription->ForceOutputOn();
                        }


                        if(Processor->RequestDataDescription(dataDescription)!=0 )
                        {

                                int extend[6]  = {0,nx-1,0,ny-1,0,nz-1};//{ngx, nx+ngx, ngy, ny+ngy, ngz, 0}; //nz+ngz };

                                if (VTKGrid == NULL)
                                {
                                        VTKGrid = vtkImageData::New();
                                        VTKGrid->SetExtent(extend); //ngx, ngx+nx, ngy, ngy+ny, ngz, ngz+nz);
                                }


                                dataDescription->GetInputDescriptionByName("input")->SetGrid(VTKGrid);
                                // For structured grids we need to specify the global data extents
                                dataDescription->GetInputDescriptionByName("input")->SetWholeExtent(extend);


                                // Create a field associated with points
                                vtkDoubleArray* field_array = vtkDoubleArray::New();
                                int ntuples = nx*ny*nz;
                                field_array->SetNumberOfComponents(1);
                                field_array->SetNumberOfTuples(ntuples);
                                field_array->SetName(variable_name);
                                int index = 0;
                                int idx = 0;
                                // ignoring ghost cells (ngy is number of ghost cells in z direction)
                                for (int z = ngz; z < nz + ngz; ++z) {
                                        // ignoring ghost cells (ngy is number of ghost cells in y direction)
                                        for (int y = ngy; y < ny + ngy; ++y) {
                                                // ignoring ghost cells (ngx is number of ghost cells in x direction)
                                                for (int x = ngx; x < nx + ngx; ++x) {
                                                        index = z * (nx + 2 * ngx) * (ny + 2 * ngy) + y * (nx + 2 * ngx) + x;
                                                        field_array->SetValue(idx, avrg_data[index]/double(nsamples));
                                                        idx += 1;
                                                }
                                        }

                                }

                                VTKGrid->GetPointData()->AddArray(field_array);
                                field_array->Delete();

                                Processor->CoProcess(dataDescription);
                        }

                        dataDescription->Delete();
                        my_data->setNewTimestep(false);
                }
        }//endif rho
}


DLL_ADAPTOR_EXPORT void* make_parameters() {
        std::cout << "In make_parameters" << std::endl;
        return static_cast<void*>(new MyParameters());
}


DLL_ADAPTOR_EXPORT void delete_parameters(void* parameters) {
        std::cout << "In delete_parameters" << std::endl;
        delete static_cast<MyParameters*>(parameters);
}


DLL_ADAPTOR_EXPORT bool needs_data_on_host(void* data, void* parameters) {
        return true;
}


DLL_ADAPTOR_EXPORT void set_parameter(void* parameters, const char* key,
                                      const char* value) {
        std::cout<<key <<" : "<<value <<std::endl;
        auto my_parameters = static_cast<MyParameters*>(parameters);
        my_parameters->setParameter(key, value);
}


DLL_ADAPTOR_EXPORT void set_mpi_comm(void* data, void* parameters,
                                     MPI_Comm communicator) {

        auto my_parameters = static_cast<MyParameters*>(parameters);
        std::cout << "In set_mpi_comm" << std::endl;

        PRINT_PARAM(parameters);
        PRINT_PARAM(data);
        PRINT_PARAM(communicator);

        my_parameters->setMPIComm(communicator);
}


DLL_ADAPTOR_EXPORT void new_timestep(void* data, void* parameters, double time,
                                     int timestep_number) {
        PRINT_PARAM(time);
        auto my_parameters = static_cast<MyParameters*>(parameters);
        auto my_data = static_cast<MyData*>(data);
        my_data->setCurrentTimestep(timestep_number);
        my_data->setCurrentTime(time);
        my_data->setNewTimestep(true);

        if(time >= std::stoi(my_parameters->getParameter("endTime"))) {
                my_data->setEndTimeStep(true);
        }


}


DLL_ADAPTOR_EXPORT void end_timestep(void* data, void* parameters, double time,
                                     int timestep_number) {
        PRINT_PARAM(timestep_number);
}

}//extern c
