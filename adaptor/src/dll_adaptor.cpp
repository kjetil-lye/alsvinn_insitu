#include "dll_adaptor.hpp"
#include "parameters.hpp"
#include "data.hpp"
#include "isosurfaceVtkPipeline.hpp"
#include <mpi.h>
#include <fstream>
#include <limits>
#include <iomanip>
#include <algorithm>
#include <iostream>
#include <vtkCPDataDescription.h>
#include <vtkCPInputDataDescription.h>
#include <vtkCPProcessor.h>
#include <vtkCPPythonScriptPipeline.h>
#include <vtkFloatArray.h>
#include <vtkDoubleArray.h>
#include <vtkIntArray.h>
#include <vtkImageData.h>
#include <vtkNew.h>
#include <vtkPointData.h>
#include <vtkPoints.h>
#include <vtkMPI.h>
#include <iterator>
#include <vtkMultiBlockDataSet.h>
#include <vtkMultiPieceDataSet.h>
#include <vtkMultiProcessController.h>

#define PRINTL { int rank; MPI_Comm_rank(MPI_COMM_WORLD, &rank); std::cerr << "In GLOBAL RANK " << rank << ", at line: " <<__LINE__ << std::endl; }
#define PV_NUM_THREADS 1

// Simple macro to print parameters
#define PRINT_PARAM(X) std::cout << "Value of " << #X << " is " << X << std::endl
extern "C" {


vtkCPProcessor* Processor = NULL;
vtkImageData* VTKGrid = NULL;
MPI_Comm pvComm;
vtkMPICommunicatorOpaqueComm* Comm = NULL;
vtkCPDataDescription*  dataDescription = NULL;  //vtkCPDataDescription::New();



void addsquared(double *, double *, int *, MPI_Datatype *);

void addsquared(double *in, double *out, int *len, MPI_Datatype *)
{
        int i;
        for ( i=0; i<*len; i++ )
                out[i] += in[i]*in[i];
}



DLL_ADAPTOR_EXPORT void* create(const char* simulator_name,
                                const char* simulator_version, void* parameters) {

        auto my_parameters = static_cast<MyParameters*>(parameters);
        const std::string version = my_parameters->getParameter("basename");
        return static_cast<void*>(new MyData);
}




void fillGrid(int mpi_rank,  const char* variable_name, int nx, int ny, int nz, int ngx, int ngy, int ngz, double avrg_data[], double avrg_sqr_data[], int norm_samples)
{

  dataDescription->GetInputDescriptionByName("input")->SetGrid(VTKGrid);
  // For structured grids we need to specify the global data extents

  // Create a field associated with points
  vtkDoubleArray* field_array_mean = vtkDoubleArray::New();
  vtkDoubleArray* field_array_var = vtkDoubleArray::New();
  int ntuples = nx*ny*nz;
  field_array_mean->SetNumberOfComponents(1);
  field_array_mean->SetNumberOfTuples(ntuples);
  field_array_var->SetNumberOfComponents(1);
  field_array_var->SetNumberOfTuples(ntuples);
  field_array_mean->SetName( (std::string(variable_name)+"_mean").c_str());
  field_array_var->SetName( (std::string(variable_name)+"_var").c_str() );
  int index = 0;
  int idx = 0;



// ignoring ghost cells (ngy is number of ghost cells in z direction)
// ignoring ghost cells (ngy is number of ghost cells in z direction)
for (int z = ngz; z < nz + ngz; ++z) {
        // ignoring ghost cells (ngy is number of ghost cells in y direction)
        for (int y = ngy; y < ny + ngy; ++y) {
                // ignoring ghost cells (ngx is number of ghost cells in x direction)
                for (int x = ngx; x < nx + ngx; ++x) {
                        index = z * (nx + 2 * ngx) * (ny + 2 * ngy) + y * (nx + 2 * ngx) + x;
                        double tmp = avrg_data[index]/double(norm_samples);
                        field_array_mean->SetValue(idx, tmp);
                        //  tmp *=(avrg_data[index]/double(nsamples));
                        tmp =  avrg_sqr_data[index]/double(norm_samples) -tmp*tmp;
                        field_array_var->SetValue(idx, tmp);
                        idx += 1;
                }
        }

}


        VTKGrid->GetPointData()->AddArray(field_array_mean);
        VTKGrid->GetPointData()->AddArray(field_array_var);
        field_array_mean->Delete();
        field_array_var->Delete();
}


/**
 * CatalystCoProcess
 * @param nx, ny, nz are number of cells in respective direction
 * @param ngx, ngy, ngz are number of ghost cells in respective direction
 */
DLL_ADAPTOR_EXPORT void CatalystCoProcess(void* data, void* parameters, double time,
                                          const char* variable_name,  double* variable_data, int nx, int ny, int nz,
                                          int ngx, int ngy, int ngz, double ax, double ay, double az, double bx,
                                          double by, double bz, int gpu_number )
{



                auto my_parameters = static_cast<MyParameters*>(parameters);

                int mpi_rank;
                MPI_Comm_rank(my_parameters->getMPIComm(), &mpi_rank);
                int mpi_size;
                MPI_Comm_size(my_parameters->getMPIComm(), &mpi_size);

                       //check if we can run all in parallel:
                int nsamples = std::stoi(my_parameters->getParameter("samples"));
                if(mpi_size < nsamples) {
                        std::cerr<< "warning: not enough mpi nodes,  reduce sample size to number of mpi nodes: "<< mpi_size<<std::endl;
                }



                int norm_samples = nsamples;
                const size_t ndata = (ngx*2+nx)*(ny+2*ngy)*(nz+2*ngz);
                double avrg_data[ndata];
                double avrg_sqr_data[ndata];

                MPI_Reduce(variable_data, avrg_data, ndata, MPI_DOUBLE, MPI_SUM, 0, my_parameters->getMPIComm());
                MPI_Op op;
                MPI_Op_create( (MPI_User_function *)addsquared, 1, &op);
                MPI_Reduce(variable_data, avrg_sqr_data, ndata, MPI_DOUBLE, op,0, my_parameters->getMPIComm());


                if( mpi_rank < PV_NUM_THREADS )
                {
                  MPI_Bcast(avrg_data, ndata,MPI_DOUBLE,0, pvComm);
                  MPI_Bcast(avrg_sqr_data, ndata,MPI_DOUBLE,0, pvComm);


                        if (VTKGrid == NULL)
                            {
                                int extend[6]  = {0,nx-1,0,ny-1,0,nz-1};
                                    VTKGrid = vtkImageData::New();
                                     VTKGrid->SetOrigin(0, 0, 0);
                                    VTKGrid->SetExtent(extend);
                            }

                        fillGrid(mpi_rank,  variable_name,  nx,  ny,  nz, ngx,  ngy,  ngz, avrg_data, avrg_sqr_data, norm_samples);

                        }

        }





DLL_ADAPTOR_EXPORT void* make_parameters() {
        //      std::cout << "In make_parameters" << std::endl;
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
        my_parameters->setMPIComm(communicator);
        int mpi_rank;
        MPI_Comm_rank(my_parameters->getMPIComm(), &mpi_rank);

        int mpi_size;
        MPI_Comm_size(my_parameters->getMPIComm(), &mpi_size);
        //check if we can run all in parallel:
        int nSamples = std::stoi(my_parameters->getParameter("samples"));


        //create the communicator for catalyst: includes all the firs sample ranks
        if(mpi_rank < PV_NUM_THREADS)
        {
                MPI_Comm_split(my_parameters->getMPIComm(),0, mpi_rank, &pvComm);
        }else{
                MPI_Comm_split(my_parameters->getMPIComm(), MPI_UNDEFINED, mpi_rank, &pvComm );
        }


        if(mpi_rank < PV_NUM_THREADS)
        {
                if (Processor == NULL)
                {

                        Processor = vtkCPProcessor::New();
                        Comm = new vtkMPICommunicatorOpaqueComm(&pvComm );
                        Processor->Initialize(*Comm);
                        std::cout << "rank " << mpi_rank << " : initialized processor with comm "<<Comm->GetHandle() << std::endl;
                }
                else
                {
                        Processor->RemoveAllPipelines();
                }

                //default script
                const char *script_default = "../pythonScripts/gridwriter.py";

                vtkNew<vtkCPPythonScriptPipeline> pipeline;


                // png etc script
                const std::string script_str = my_parameters->getParameter("catalystscript");
                const char *script_loc = script_str.c_str();

                if(script_str =="none")
                {
                        std::cout<<"only default pipeline script: "<< script_default<<std::endl;
                        pipeline->Initialize(script_default);
                        Processor->AddPipeline(pipeline);
                }
                else
                {

                        std::cout<<"pipeline script: "<< script_loc<<std::endl;
                        pipeline->Initialize(script_loc);
                        Processor->AddPipeline(pipeline);
                }

        }

        //  make sure everything is set up
        MPI_Barrier(my_parameters->getMPIComm());
}


DLL_ADAPTOR_EXPORT void new_timestep(void* data, void* parameters, double time,
                                     int timestep_number) {

        auto my_parameters = static_cast<MyParameters*>(parameters);
        int mpi_rank;
        MPI_Comm_rank(my_parameters->getMPIComm(), &mpi_rank);
        std::cout<<"mpi rank : "<<mpi_rank<< " at time "<< time<<std::endl;

        if(mpi_rank < PV_NUM_THREADS) {

                dataDescription = vtkCPDataDescription::New();
                dataDescription->SetTimeData(time, timestep_number); //my_data->getCurrentTime(), my_data->getCurrentTimestep());
                dataDescription->AddInput("input");
        }

}


DLL_ADAPTOR_EXPORT void end_timestep(void* data, void* parameters, double time,
                                     int timestep_number) {

        auto my_parameters = static_cast<MyParameters*>(parameters);
        int mpi_rank;
        MPI_Comm_rank(my_parameters->getMPIComm(), &mpi_rank);
        //    std::cout<<"mpi rank : "<<mpi_rank<< " at 1 end time "<< time<<std::endl;


        if(mpi_rank < PV_NUM_THREADS)
         {
          dataDescription->GetInputDescriptionByName("input")->SetGrid(VTKGrid);

//  dataDescription->GetInputDescriptionByName("input")->SetGrid(VTKGrid);
                dataDescription->ForceOutputOn();
                if(Processor->RequestDataDescription(dataDescription)!=0 )
                {
                        Processor->CoProcess(dataDescription);
                }
                dataDescription->Delete();
        }
        //std::cout<<"mpi rank : "<<mpi_rank<< " at 2 end time "<< time<<std::endl;
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


        if (Comm)
        {
                delete Comm;
                Comm = NULL;
        }
             if(pvComm)
        {
                MPI_Comm_free(&pvComm);
        }

        delete static_cast<MyData*>(data);
}

} //end DLL_ADAPTOR_EXPORT
//extern c
