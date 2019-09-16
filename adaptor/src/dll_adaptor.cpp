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

#define ADAPTOR_USE_MPI_ON  1

#define ADAPTOR_USE_VTKCPPROCESSOR 0

#define PRINTL { int rank; MPI_Comm_rank(MPI_COMM_WORLD, &rank); std::cout << "In rank " << rank << ", at line: " <<__LINE__ << std::endl; }
// Simple macro to print parameters
#define PRINT_PARAM(X) std::cout << "Value of " << #X << " is " << X << std::endl
extern "C" {

int countBlock;

vtkCPProcessor* Processor = NULL;
vtkMultiBlockDataSet* VTKGrid = NULL;
vtkImageData* VTKImage = NULL;
MPI_Comm coproc_comm;
vtkMPICommunicatorOpaqueComm* Comm = NULL;
vtkCPDataDescription*  dataDescription = NULL;  //vtkCPDataDescription::New();

DLL_ADAPTOR_EXPORT void* create(const char* simulator_name,
                                const char* simulator_version, void* parameters) {

        auto my_parameters = static_cast<MyParameters*>(parameters);
        const std::string version = my_parameters->getParameter("basename");
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
        if (VTKImage)
        {
                VTKImage->Delete();
                VTKImage = NULL;
        }

        if (Comm)
        {
                std::cout << "In delete_data" << std::endl;
                delete Comm;
                Comm = NULL;
        }
        if(coproc_comm)
        {
                std::cout << "In delete_data" << std::endl;
                MPI_Comm_free(&coproc_comm);
        }
        std::cout << "In delete_data" << std::endl;
        delete static_cast<MyData*>(data);
}


void fillVTKImageGrid(vtkImageData* VTKImage,const char* variable_name, int nx, int ny, int nz,   int ngx, int ngy, int ngz, double* avrg_data, double* avrg_sqr_data, int norm_samples)
{
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

          VTKImage->GetPointData()->AddArray(field_array_mean);
          VTKImage->GetPointData()->AddArray(field_array_var);
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

                std::string mb = my_parameters->getParameter("multiblock");
                const int multiXproc = std::stoi(mb.substr(0,1) );
                const int multiYproc = std::stoi(mb.substr(2,1) );
                const int multiZproc = std::stoi(mb.substr(4,1) );

                const int numProc = multiXproc*multiYproc*multiZproc;
                std::cout<< "Running Multiproc per dim x,y,z: "<< multiXproc<<" "<< multiYproc<< " " <<multiZproc <<std::endl;

                int mpi_rank;
                MPI_Comm_rank(my_parameters->getMPIComm(), &mpi_rank);
                int mpi_size;
                MPI_Comm_size(my_parameters->getMPIComm(), &mpi_size);
                //check if we can run all in parallel:
                int nsamples = std::stoi(my_parameters->getParameter("samples"));
                if(mpi_size < nsamples) {
                        std::cerr<< "warning: not enough mpi nodes,  reduce sample size to number of mpi nodes: "<< mpi_size<<std::endl;
                }


                std::cout<<"mpi rank : "<<mpi_rank<< " at variable "<< variable_name<<std::endl;

                int norm_samples = nsamples;
                const size_t ndata = (ngx*2+nx)*(ny+2*ngy)*(nz+2*ngz);
                double avrg_data[ndata];
                double avrg_sqr_data[ndata];

                MPI_Reduce(variable_data, avrg_data, ndata, MPI_DOUBLE, MPI_SUM, 0, my_parameters->getMPIComm());

                double sqr_variable_data[ndata];
                //get squared sum to use for variance, reuse variable_data to save space
                for (int i = 0; i< ndata; ++i) {
                        sqr_variable_data[i] = variable_data[i]*variable_data[i];
                }

                MPI_Reduce(&sqr_variable_data, avrg_sqr_data, ndata, MPI_DOUBLE, MPI_SUM, 0, my_parameters->getMPIComm());


                int extend[6]  = {0,nx-1,0,ny-1,0,nz-1};

                if(VTKImage == NULL)
                {
                        VTKImage = vtkImageData::New();
                        VTKImage->SetExtent(extend);
                }

                if (VTKGrid == NULL)
                {
                        VTKGrid = vtkMultiBlockDataSet::New();
                        vtkNew<vtkMultiPieceDataSet> multiPiece;
                        multiPiece->SetNumberOfPieces(numProc);
                        multiPiece->SetPiece(mpi_rank-nsamples, VTKImage);
                        VTKGrid->SetNumberOfBlocks(1);
                        VTKGrid->SetBlock(0, multiPiece.GetPointer());
                        countBlock = 0;
                }



                fillVTKImageGrid(VTKImage, variable_name,  nx,  ny,  nz, ngx,  ngy,  ngz,  avrg_data, avrg_sqr_data, norm_samples);


            //TODO WHEN?    dataDescription->GetInputDescriptionByName("input")->SetGrid(VTKGrid);
            dataDescription->GetInputDescriptionByName("input")->SetGrid(VTKImage);


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
        PRINT_PARAM(communicator);

        my_parameters->setMPIComm(communicator);
        int mpi_rank;
        MPI_Comm_rank(my_parameters->getMPIComm(), &mpi_rank);

        //      std::cout << "rank " << mpi_rank << " : In set_mpi_comm" << std::endl;

        //create new communicator to use in CatalystCoProcess

        if(mpi_rank == 0)
        {
                MPI_Comm_split(my_parameters->getMPIComm(), 0, mpi_rank, &coproc_comm);
        }else{
                MPI_Comm_split(my_parameters->getMPIComm(), MPI_UNDEFINED, mpi_rank, &coproc_comm);
        }

        if(mpi_rank == 0)
        {
                //const std::string version = my_parameters->getParameter("basename");
                // Initialize catalyst, set processes
                if (Processor == NULL)
                {
                        Processor = vtkCPProcessor::New();
                        Comm = new vtkMPICommunicatorOpaqueComm(&coproc_comm );
                        Processor->Initialize(*Comm);
                        std::cout << "rank " << mpi_rank << " : initialized processor with comm "<<Comm->GetHandle() << std::endl;
                }
                else
                {
                        Processor->RemoveAllPipelines();
                }


                if(ADAPTOR_USE_VTKCPPROCESSOR) //if used with vtkCPProcessor
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
        }
}


DLL_ADAPTOR_EXPORT void new_timestep(void* data, void* parameters, double time,
                                     int timestep_number) {

        auto my_parameters = static_cast<MyParameters*>(parameters);
        int mpi_rank;
        MPI_Comm_rank(my_parameters->getMPIComm(), &mpi_rank);
        std::cout<<"mpi rank : "<<mpi_rank<< " at time "<< time<<std::endl;

        if(mpi_rank==0) {

                auto my_data = static_cast<MyData*>(data);
                my_data->setCurrentTimestep(timestep_number);
                my_data->setCurrentTime(time);
                my_data->setNewTimestep(true);

                if(time >= std::stoi(my_parameters->getParameter("endTime"))) {
                        my_data->setEndTimeStep(true);
                }
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

        if(mpi_rank==0)
        {
                dataDescription->ForceOutputOn();
                if(Processor->RequestDataDescription(dataDescription)!=0 )
                {
                        Processor->CoProcess(dataDescription);
                }
                dataDescription->Delete();
        }
        //std::cout<<"mpi rank : "<<mpi_rank<< " at 2 end time "<< time<<std::endl;


}



                                                                                                                                                                                                                                            //extern c
