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

// Simple macro to print parameters
#define PRINT_PARAM(X) std::cout << "Value of " << #X << " is " << X << std::endl
extern "C" {


vtkCPProcessor* Processor = NULL;
vtkMultiBlockDataSet* VTKGrid = NULL;
//vtkImageData* VTKImage = NULL;
MPI_Comm spatialComm;
MPI_Comm coproc_comm;
vtkMPICommunicatorOpaqueComm* Comm = NULL;
vtkCPDataDescription*  dataDescription = NULL;  //vtkCPDataDescription::New();


inline int getSpatialRank(int globalR, int numProcS){
  return globalR%numProcS;
};

inline int getStatisticalRank(int globalR, int numProcS){
  return globalR/numProcS;
};

DLL_ADAPTOR_EXPORT void* create(const char* simulator_name,
                                const char* simulator_version, void* parameters) {

        auto my_parameters = static_cast<MyParameters*>(parameters);
        const std::string version = my_parameters->getParameter("basename");
        return static_cast<void*>(new MyData);
}




void fillGrid(int mpi_rank, int numProcS, int multiXproc,int multiYproc, int multiZproc, const char* variable_name, int nx, int ny, int nz, int ngx, int ngy, int ngz, double avrg_data[], double avrg_sqr_data[], int norm_samples)
{

    vtkMultiPieceDataSet* multiPiece = vtkMultiPieceDataSet::SafeDownCast(VTKGrid->GetBlock(0));
    vtkDataSet* dataSet = vtkDataSet::SafeDownCast(multiPiece->GetPiece(getSpatialRank(mpi_rank, numProcS)));

    std::cout<< " ------------------- "<< mpi_rank <<" "<< getSpatialRank(mpi_rank, numProcS)<<std::endl;

  int x_dom = getSpatialRank(mpi_rank, numProcS)%multiXproc;
  int y_dom = (getSpatialRank(mpi_rank, numProcS)/multiXproc)%multiYproc;
  int z_dom = getSpatialRank(mpi_rank, numProcS)/multiYproc;
  int ntuples = nx*ny*nz; //multiXproc*multiYproc*multiZproc*nx*ny*nz;

  if (!dataSet->GetPointData()->GetArray((std::string(variable_name)+"_mean").c_str()))
    {      // Create a field associated with points
          vtkDoubleArray* field_array_mean = vtkDoubleArray::New();
          vtkDoubleArray* field_array_var = vtkDoubleArray::New();

          field_array_mean->SetNumberOfComponents(1);
          field_array_mean->SetNumberOfTuples(ntuples);
          field_array_var->SetNumberOfComponents(1);
          field_array_var->SetNumberOfTuples(ntuples);
          field_array_mean->SetName( (std::string(variable_name)+"_mean").c_str());
          field_array_var->SetName( (std::string(variable_name)+"_var").c_str() );
          dataSet->GetPointData()->AddArray(field_array_mean);
          dataSet->GetPointData()->AddArray(field_array_var);
          field_array_mean->Delete();
          field_array_var->Delete();
          PRINTL
    }

            vtkDoubleArray* field_array_mean = vtkDoubleArray::SafeDownCast(dataSet->GetPointData()->GetArray((std::string(variable_name)+"_mean").c_str()));
            vtkDoubleArray* field_array_var = vtkDoubleArray::SafeDownCast(dataSet->GetPointData()->GetArray( (std::string(variable_name)+"_var").c_str()));

          int localIndex = 0;
          int globalIndex = 0;


PRINTL
// ignoring ghost cells (ngy is number of ghost cells in z direction)
         for (int z = ngz; z < nz + ngz; ++z) {
                 // ignoring ghost cells (ngy is number of ghost cells in y direction)
                 for (int y = ngy; y < ny + ngy; ++y) {
                         // ignoring ghost cells (ngx is number of ghost cells in x direction)
                         for (int x = ngx; x < nx + ngx; ++x) {

                                  localIndex = z * (nx + 2 * ngx) * (ny + 2 * ngy) + y * (nx + 2 * ngx) + x;
                              /*    if(nz <2)
                                  {
                                    globalIndex =  (y-ngy  )*nx + (x -ngx  ); //z*nx*ny+y*nx +x  (y-ngy + y_dom*ny)*nx + (x -ngx + x_dom*nx);
                                  }else{
                                    globalIndex = (z -ngz )*nx*ny+ (y-ngy  )*nx + (x -ngx  ); //z*nx*ny+y*nx +x
                                  }
*/

globalIndex+=1;

                                  double tmp = avrg_data[localIndex]/double(norm_samples);
                                  field_array_mean->SetValue(globalIndex, tmp);
                                  tmp =  avrg_sqr_data[localIndex]/double(norm_samples) -tmp*tmp;
                                  field_array_var->SetValue(globalIndex, tmp);


                          }
                  }

          }

    //      VTKImage->GetPointData()->AddArray(field_array_mean);
  //        VTKImage->GetPointData()->AddArray(field_array_var);
  //        field_array_mean->Delete();
    //      field_array_var->Delete();

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

  if(std::string(variable_name)=="rho")
  {

                auto my_data = static_cast<MyData*>(data);
                auto my_parameters = static_cast<MyParameters*>(parameters);

                std::string mb = my_parameters->getParameter("multiblock");
                const int multiXproc = std::stoi(mb.substr(0,1) );
                const int multiYproc = std::stoi(mb.substr(2,1) );
                const int multiZproc = std::stoi(mb.substr(4,1) );
                const int numProcS = multiXproc*multiYproc*multiZproc;

                int mpi_rank;
                MPI_Comm_rank(my_parameters->getMPIComm(), &mpi_rank);
                int mpi_size;
                MPI_Comm_size(my_parameters->getMPIComm(), &mpi_size);
                int mpi_spatialRank; // is the same as the sampleRank
                MPI_Comm_rank(spatialComm, &mpi_spatialRank);
                int mpi_spatialSize; // is the same as number of samples
                MPI_Comm_size(spatialComm, &mpi_spatialSize);

//std::cout<< "  ===================================== "<< mpi_spatialRank<< " of "<<mpi_spatialSize<<std::endl;

std::cout<<" ns "<<nx<<" "<<ny<<" "<<nz<<std::endl;
                //check if we can run all in parallel:
                int nsamples = std::stoi(my_parameters->getParameter("samples"));
                if(mpi_size < nsamples) {
                        std::cerr<< "warning: not enough mpi nodes,  reduce sample size to number of mpi nodes: "<< mpi_size<<std::endl;
                }


          //      std::cout<<"mpi rank : "<<mpi_rank<< " at variable "<< variable_name;
          //        std::cout<<"spatial rank : "<<getSpatialRank(mpi_rank,numProcS);
            //            std::cout<<"sample rank : "<<getStatisticalRank(mpi_rank,numProcS) <<std::endl;


                int norm_samples = nsamples;
                const size_t ndata = (ngx*2+nx)*(ny+2*ngy)*(nz+2*ngz);
                double avrg_data[ndata];
                double avrg_sqr_data[ndata];

                MPI_Reduce(variable_data, avrg_data, ndata, MPI_DOUBLE, MPI_SUM, 0, spatialComm); //getSpatialRank(mpi_rank, numProcS)

                double sqr_variable_data[ndata];
                //get squared sum to use for variance, reuse variable_data to save space
                for (int i = 0; i< ndata; ++i) {
                        sqr_variable_data[i] = variable_data[i]*variable_data[i];
                }

                MPI_Reduce(&sqr_variable_data, avrg_sqr_data, ndata, MPI_DOUBLE, MPI_SUM, 0, spatialComm);

                if( mpi_spatialRank == 0 )
                {
                  int mpi_statRank; // is the same as the spatialRank
                  MPI_Comm_rank(coproc_comm, &mpi_statRank);


                if (VTKGrid == NULL)
                {

                          int x_dom = getSpatialRank(mpi_rank, numProcS)%multiXproc;
                          int y_dom = (getSpatialRank(mpi_rank, numProcS)/multiXproc)%multiYproc;
                          int z_dom = getSpatialRank(mpi_rank, numProcS)/multiYproc;

                          int extend[6]; //  = {0, multiXproc*nx-1,0,multiYproc*ny-1,0,multiZproc*nz-1};
                          extend[0] = x_dom*nx;
                          extend[1] = ( x_dom+1)*nx;
                          extend[2] = y_dom*ny;
                          extend[3] = ( y_dom+1)*ny;
                          extend[4] = z_dom*nz;
                          extend[5] = ( z_dom+1)*nz;


                          vtkImageData* VTKImage = vtkImageData::New();
                          VTKImage->SetOrigin(0, 0, 0);
                          VTKImage->SetExtent(extend);

                        VTKGrid = vtkMultiBlockDataSet::New();
                        vtkNew<vtkMultiPieceDataSet> multiPiece;
                        multiPiece->SetNumberOfPieces(numProcS);
                        multiPiece->SetPiece( mpi_statRank, VTKImage);

                        PRINTL
                        VTKGrid->SetNumberOfBlocks(1);
                        VTKGrid->SetBlock(0, multiPiece.GetPointer());
                }

                fillGrid(mpi_rank, numProcS, multiXproc,multiYproc, multiZproc, variable_name,  nx,  ny,  nz, ngx,  ngy,  ngz, avrg_data, avrg_sqr_data, norm_samples);

    dataDescription->GetInputDescriptionByName("input")->SetGrid(VTKGrid);

          }

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
        std::string mb = my_parameters->getParameter("multiblock");
        const int multiXproc = std::stoi(mb.substr(0,1) );
        const int multiYproc = std::stoi(mb.substr(2,1) );
        const int multiZproc = std::stoi(mb.substr(4,1) );
        const int numProcS = multiXproc*multiYproc*multiZproc;


        my_parameters->setMPIComm(communicator);
        int mpi_rank;
        MPI_Comm_rank(my_parameters->getMPIComm(), &mpi_rank);

        int mpi_size;
        MPI_Comm_size(my_parameters->getMPIComm(), &mpi_size);
        //check if we can run all in parallel:
        int nSamples = std::stoi(my_parameters->getParameter("samples"));

        //create the spatial communicators:
        MPI_Comm_split(my_parameters->getMPIComm(), getSpatialRank(mpi_rank, numProcS), mpi_rank, &spatialComm);
        int mpi_spatialRank; // is the same as the sampleRank
        MPI_Comm_rank(spatialComm, &mpi_spatialRank);


        //create the communicator for catalyst: includes all the firs sample ranks
        if(mpi_spatialRank == 0)
        {
                MPI_Comm_split(my_parameters->getMPIComm(),0, mpi_rank, &coproc_comm);
        }else{
                MPI_Comm_split(my_parameters->getMPIComm(), MPI_UNDEFINED, mpi_rank, &coproc_comm);
        }


        if(mpi_spatialRank == 0)
        {
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
                          PRINTL
                                std::cout<<"pipeline script: "<< script_loc<<std::endl;
                                pipeline->Initialize(script_loc);
                                Processor->AddPipeline(pipeline);
                        }

      }

  //  make sure everything is set up
  MPI_Barrier(my_parameters->getMPIComm());
  PRINTL

}


DLL_ADAPTOR_EXPORT void new_timestep(void* data, void* parameters, double time,
                                     int timestep_number) {

        auto my_parameters = static_cast<MyParameters*>(parameters);
        int mpi_rank;
        MPI_Comm_rank(my_parameters->getMPIComm(), &mpi_rank);
        std::cout<<"mpi rank : "<<mpi_rank<< " at time "<< time<<std::endl;

        int mpi_spatialRank; // is the same as the sampleRank
        MPI_Comm_rank(spatialComm, &mpi_spatialRank);

        if(mpi_spatialRank==0) {

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

        int mpi_spatialRank; // is the same as the sampleRank
        MPI_Comm_rank(spatialComm, &mpi_spatialRank);

        if(mpi_spatialRank==0) {
          PRINTL
            //    dataDescription->GetInputDescriptionByName("input")->SetGrid(VTKGrid);
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
PRINTL
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
        if(coproc_comm)
        {

                MPI_Comm_free(&coproc_comm);

        }
        if(spatialComm)
        {
                        MPI_Comm_free(&spatialComm);
        }

        delete static_cast<MyData*>(data);
}

} //end DLL_ADAPTOR_EXPORT
                                                                                                                                                                                                                                            //extern c
