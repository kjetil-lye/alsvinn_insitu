#include "dll_adaptor.hpp"
#include "parameters.hpp"
#include "data.hpp"
#include "isosurfaceVtkPipeline.hpp"
#include <mpi.h>
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
#include <vtkMPI.h>


// Simple macro to print parameters
#define PRINT_PARAM(X) std::cout << "Value of " << #X << " is " << X << std::endl
extern "C" {

vtkCPProcessor* Processor = NULL;
vtkImageData* VTKGrid = NULL;
vtkMPICommunicatorOpaqueComm* Comm = NULL;

DLL_ADAPTOR_EXPORT void* create(const char* simulator_name,
                                const char* simulator_version, void* parameters) {



        auto my_parameters = static_cast<MyParameters*>(parameters);

  const std::string version = my_parameters->getParameter("basename");
        // Initialize catalyst, set processes
    /*    if (Processor == NULL)
        {
                Processor = vtkCPProcessor::New();
          //      Comm = new vtkMPICommunicatorOpaqueComm( my_parameters->getMPICommPtr() );
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
        */

        return static_cast<void*>(new MyData);

}


DLL_ADAPTOR_EXPORT void delete_data(void* data) {
    //  std::cout << "In delete_data" << std::endl;
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

                auto my_parameters = static_cast<MyParameters*>(parameters);
                //  auto timeStep = my_data->getCurrentTimestep();
                //    const std::string description_namestr = my_parameters->getParameter("basename");        const char *description_name = description_namestr.c_str();
            /*    int mpi_init;
                MPI_Initialized(&mpi_init);
                if(mpi_init){
                  std::cerr<< "MPI has been initialized"<<std::endl;
                  std::cerr<< "using Comm : "<< my_parameters->getMPIComm() <<std::endl;
                  }else{
                     std::cerr<< "MPI has"<<"NOT"<<" been Initialized"<<std::endl;
                   }
*/
                int mpi_rank;
                MPI_Comm_rank(my_parameters->getMPIComm(), &mpi_rank);
                int mpi_size;
                MPI_Comm_size(my_parameters->getMPIComm(), &mpi_size);
                //check if we can run all in parallel:
                 int nsamples = std::stoi(my_parameters->getParameter("samples"));
                if(mpi_size < nsamples) {
                        std::cerr<< "warning: not enough mpi nodes,  reduce sample size to number of mpi nodes: "<< mpi_size<<std::endl;
                }




                 const size_t ndata = (ngx*2+nx)*(ny+2*ngy)*(nz+2*ngz);
                double avrg_data[ndata];
              //  double  avrg_sqr_data[ndata];

              MPI_Reduce(variable_data, avrg_data, ndata, MPI_DOUBLE, MPI_SUM, 0, my_parameters->getMPIComm());
if(mpi_rank == 0)  std::cout << "after reduction" << std::endl;

          //      double sqr_variable_data[ndata];
//get squared sum to use for variance,
            /*    for (int i = 0; i< ndata; ++i) {
                  sqr_variable_data[i] = variable_data[i]*variable_data[i];
                }

                if(mpi_size>1) {
                        MPI_Reduce(&sqr_variable_data, avrg_sqr_data, ndata, MPI_DOUBLE, MPI_SUM, 0, my_parameters->getMPIComm());
                }else{
                        //treat as seperate sampels
                        avrg_sqr_data = sqr_variable_data;
                        nsamples = 1;
                }
*/

                if(mpi_rank == 0)
                {

    std::cout << "rank " << mpi_rank << " : RequestDataDescription" << std::endl;
                  auto my_data = static_cast<MyData*>(data);

                  vtkCPDataDescription*  dataDescription = vtkCPDataDescription::New();
                  dataDescription->SetTimeData(my_data->getCurrentTime(), my_data->getCurrentTimestep());
                  dataDescription->AddInput("input");


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


                                // Create a field associated with points
                                vtkDoubleArray* field_array_mean = vtkDoubleArray::New();
                      //          vtkDoubleArray* field_array_var = vtkDoubleArray::New();
                                int ntuples = nx*ny*nz;
                                field_array_mean->SetNumberOfComponents(1);
                                field_array_mean->SetNumberOfTuples(ntuples);
                            //    field_array_var->SetNumberOfComponents(1);
                    //            field_array_var->SetNumberOfTuples(ntuples);
                                field_array_mean->SetName( (std::string(variable_name)+"_mean").c_str());
                  //              field_array_var->SetName( (std::string(variable_name)+"_var").c_str() );
                                int index = 0;
                                int idx = 0;

                                // ignoring ghost cells (ngy is number of ghost cells in z direction)
                                for (int z = ngz; z < nz + ngz; ++z) {
                                        // ignoring ghost cells (ngy is number of ghost cells in y direction)
                                        for (int y = ngy; y < ny + ngy; ++y) {
                                                // ignoring ghost cells (ngx is number of ghost cells in x direction)
                                                for (int x = ngx; x < nx + ngx; ++x) {
                                                        index = z * (nx + 2 * ngx) * (ny + 2 * ngy) + y * (nx + 2 * ngx) + x;
                                                        double tmp = avrg_data[index]/double(nsamples);
                                                        field_array_mean->SetValue(idx, tmp);
                                                      //   tmp = avrg_sqr_data[index]/double(nsamples)-(avrg_data[index]/double(nsamples))*(avrg_data[index]/double(nsamples));
                                    //                    field_array_var->SetValue(idx, tmp);
                                                        idx += 1;
                                                }
                                        }

                                }

                                VTKGrid->GetPointData()->AddArray(field_array_mean);
                        //        VTKGrid->GetPointData()->AddArray(field_array_var);
                                field_array_mean->Delete();
                      //          field_array_var->Delete();
  std::cout<<"mpi rank : "<<mpi_rank<< "before set CoProcess" <<std::endl;
                                Processor->CoProcess(dataDescription);
                                  std::cout<<"mpi rank : "<<mpi_rank<< "after set CoProcess" <<std::endl;
                        }//end RequestDataDescription
                        std::cout<<"mpi rank : "<<mpi_rank<< "before delete" <<std::endl;
                        dataDescription->Delete();
                        std::cout<<"mpi rank : "<<mpi_rank<< "before set new timestep" <<std::endl;
                        my_data->setNewTimestep(false);
                }//end rank 0
        }//endif rho
}


DLL_ADAPTOR_EXPORT void* make_parameters() {
  //      std::cout << "In make_parameters" << std::endl;
        return static_cast<void*>(new MyParameters());
}


DLL_ADAPTOR_EXPORT void delete_parameters(void* parameters) {
    //    std::cout << "In delete_parameters" << std::endl;
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

        PRINT_PARAM(communicator);

        my_parameters->setMPIComm(communicator);
        int mpi_rank;
        MPI_Comm_rank(my_parameters->getMPIComm(), &mpi_rank);

        std::cout << "rank " << mpi_rank << " : In set_mpi_comm" << std::endl;
if(mpi_rank == 0)
{
        const std::string version = my_parameters->getParameter("basename");
              // Initialize catalyst, set processes
              if (Processor == NULL)
              {
                    std::cout << "rank " << mpi_rank << " : proc == 0" << std::endl;
                      Processor = vtkCPProcessor::New();
                      Comm = new vtkMPICommunicatorOpaqueComm( my_parameters->getMPICommPtr() );
                      Processor->Initialize(*Comm);
                        std::cout << "rank " << mpi_rank << " : initialized processor with comm "<<Comm->GetHandle() << std::endl;
              }
              else
              {
                  std::cout << "rank " << mpi_rank << " : proc != 0" << std::endl;
                      Processor->RemoveAllPipelines();
              }


              if(false) //version=="meanVar")
              {
                  std::cout << "rank " << mpi_rank << " : In false" << std::endl;
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
                  std::cout << "rank " << mpi_rank << " : set up processor" << std::endl;
}
}


DLL_ADAPTOR_EXPORT void new_timestep(void* data, void* parameters, double time,
                                     int timestep_number) {
      //  PRINT_PARAM(time);
        auto my_parameters = static_cast<MyParameters*>(parameters);
        int mpi_rank;
        MPI_Comm_rank(my_parameters->getMPIComm(), &mpi_rank);
        std::cout<<"mpi rank : "<<mpi_rank<< " at time "<< time<<std::endl;

        if(mpi_rank==0){

        auto my_data = static_cast<MyData*>(data);
        my_data->setCurrentTimestep(timestep_number);
        my_data->setCurrentTime(time);
        my_data->setNewTimestep(true);

        if(time >= std::stoi(my_parameters->getParameter("endTime"))) {
                my_data->setEndTimeStep(true);
        }
}

}


DLL_ADAPTOR_EXPORT void end_timestep(void* data, void* parameters, double time,
                                     int timestep_number) {
        PRINT_PARAM(timestep_number);
}

}//extern c
