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

#define PRINTL { int rank; MPI_Comm_rank(MPI_COMM_WORLD, &rank); std::cerr << "In GLOBAL RANK " << rank << ", at line: " <<__LINE__ << std::endl; }
#define PRINTL2 { int rank; int rank2; int rank3;  MPI_Comm_rank(MPI_COMM_WORLD, &rank); MPI_Comm_rank(spatialComm, &rank3); MPI_Comm_rank(coproc_comm, &rank2); std::cout << "In GLOBAL RANK " << rank << " in spatial rank "<< rank3 <<" in sample rank "<< rank2<< ", at line: " <<__LINE__ << std::endl; }


// Simple macro to print parameters
#define PRINT_PARAM(X) std::cout << "Value of " << #X << " is " << X << std::endl
extern "C" {


vtkCPProcessor* Processor = NULL;
vtkMultiBlockDataSet* VTKGrid = NULL;
vtkImageData* VTKImage = NULL;
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




void fillGrid(int mpi_rank, int numProcS, int multiXproc,int multiYproc, int multiZproc, const char* variable_name, int nx, int ny, int nz, int ngx, int ngy, int ngz, double* avrg_data, double* avrg_sqr_data, int norm_samples)
{
PRINTL
    vtkMultiPieceDataSet* multiPiece = vtkMultiPieceDataSet::SafeDownCast(VTKGrid->GetBlock(0));
    vtkDataSet* dataSet = vtkDataSet::SafeDownCast(multiPiece->GetPiece(getStatisticalRank(mpi_rank, numProcS)));
PRINTL
    if (dataSet->GetPointData()->GetArray((std::string(variable_name)+"_mean").c_str()) == NULL )
    {      // Create a field associated with points
          vtkDoubleArray* field_array_mean = vtkDoubleArray::New();
          vtkDoubleArray* field_array_var = vtkDoubleArray::New();

          int ntuples = multiXproc*multiYproc*multiZproc*nx*ny*nz;
          field_array_mean->SetNumberOfComponents(1);
          field_array_mean->SetNumberOfTuples(ntuples);
          field_array_var->SetNumberOfComponents(1);
          field_array_var->SetNumberOfTuples(ntuples);
          field_array_mean->SetName( (std::string(variable_name)+"_mean").c_str());
          field_array_var->SetName( (std::string(variable_name)+"_var").c_str() );
          dataSet->GetPointData()->AddArray(field_array_mean);
          dataSet->GetPointData()->AddArray(field_array_var);
          PRINTL
    }
PRINTL
            vtkDoubleArray* field_array_mean = vtkDoubleArray::SafeDownCast(dataSet->GetPointData()->GetArray((std::string(variable_name)+"_mean").c_str()));
            vtkDoubleArray* field_array_var = vtkDoubleArray::SafeDownCast(dataSet->GetPointData()->GetArray( (std::string(variable_name)+"_var").c_str()));
PRINTL
          int index = 0;
          int idx = 0;

          int x_dom = getSpatialRank(mpi_rank, numProcS)%multiXproc;
          int y_dom = (getSpatialRank(mpi_rank, numProcS)/multiXproc)%multiYproc;
          int z_dom = getSpatialRank(mpi_rank, numProcS)/multiYproc;

          // ignoring ghost cells (ngy is number of ghost cells in z direction)
          for (int z = ngz + z_dom*nz; z < nz + ngz + z_dom*nz; ++z) {
                  // ignoring ghost cells (ngy is number of ghost cells in y direction)
                  for (int y = ngy + y_dom*ny; y < ny + ngy+y_dom*ny; ++y) {
                          // ignoring ghost cells (ngx is number of ghost cells in x direction)
                          for (int x = ngx+x_dom*nx; x < nx + ngx+x_dom*nx; ++x) {
                                  index = z * (nx + 2 * ngx) * (ny + 2 * ngy) + y * (nx + 2 * ngx) + x;
                                  double tmp = avrg_data[index]/double(norm_samples);
                                  field_array_mean->SetValue(idx, tmp);
                                  tmp =  avrg_sqr_data[index]/double(norm_samples) -tmp*tmp;
                                  field_array_var->SetValue(idx, tmp);
                                  idx += 1;
                          }
                  }

          }
PRINTL
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

PRINTL
                auto my_data = static_cast<MyData*>(data);
                auto my_parameters = static_cast<MyParameters*>(parameters);

                std::string mb = my_parameters->getParameter("multiblock");
                const int multiXproc = std::stoi(mb.substr(0,1) );
                const int multiYproc = std::stoi(mb.substr(2,1) );
                const int multiZproc = std::stoi(mb.substr(4,1) );
                const int numProcS = multiXproc*multiYproc*multiZproc;
PRINTL
                int mpi_rank;
                MPI_Comm_rank(my_parameters->getMPIComm(), &mpi_rank);
                int mpi_size;
                MPI_Comm_size(my_parameters->getMPIComm(), &mpi_size);
                int mpi_size2;
                MPI_Comm_size(spatialComm, &mpi_size2);
            //  int mpi_size3;
          //      MPI_Comm_size( coproc_comm, &mpi_size3);
std::cout<< "  ===================================== "<< mpi_size2<< " "<<mpi_size2<<std::endl;


                //check if we can run all in parallel:
                int nsamples = std::stoi(my_parameters->getParameter("samples"));
                if(mpi_size < nsamples) {
                        std::cerr<< "warning: not enough mpi nodes,  reduce sample size to number of mpi nodes: "<< mpi_size<<std::endl;
                }


                std::cout<<"mpi rank : "<<mpi_rank<< " at variable "<< variable_name;
                  std::cout<<"spatial rank : "<<getSpatialRank(mpi_rank,numProcS);
                        std::cout<<"sample rank : "<<getStatisticalRank(mpi_rank,numProcS) <<std::endl;
PRINTL

                int norm_samples = nsamples;
                const size_t ndata = (ngx*2+nx)*(ny+2*ngy)*(nz+2*ngz);
                double avrg_data[ndata];
                double avrg_sqr_data[ndata];
PRINTL
                MPI_Reduce(variable_data, avrg_data, ndata, MPI_DOUBLE, MPI_SUM, 0, spatialComm); //getSpatialRank(mpi_rank, numProcS)
PRINTL
                double sqr_variable_data[ndata];
                //get squared sum to use for variance, reuse variable_data to save space
                for (int i = 0; i< ndata; ++i) {
                        sqr_variable_data[i] = variable_data[i]*variable_data[i];
                }
PRINTL
                MPI_Reduce(&sqr_variable_data, avrg_sqr_data, ndata, MPI_DOUBLE, MPI_SUM, 0, spatialComm);

                if( getStatisticalRank(mpi_rank, numProcS) == 0 )
                {
PRINTL
                int extend[6]  = {0, multiXproc*(nx-1),0,multiYproc*(ny-1),0,multiZproc*(nz-1)};

                if(VTKImage == NULL)
                {
                        VTKImage = vtkImageData::New();
                        VTKImage->SetExtent(extend);
                }

                if (VTKGrid == NULL)
                {
                        VTKGrid = vtkMultiBlockDataSet::New();
                        vtkNew<vtkMultiPieceDataSet> multiPiece;
                        multiPiece->SetNumberOfPieces(numProcS);
                        multiPiece->SetPiece( getStatisticalRank(mpi_rank, numProcS), VTKImage);
                        VTKGrid->SetNumberOfBlocks(1);
                        VTKGrid->SetBlock(0, multiPiece.GetPointer());

                }
PRINTL
                fillGrid(mpi_rank, numProcS, multiXproc,multiYproc, multiZproc, variable_name,  nx,  ny,  nz, ngx,  ngy,  ngz, avrg_data, avrg_sqr_data, norm_samples);
PRINTL
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
PRINTL
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


        MPI_Comm tmp_comm;
        MPI_Comm_dup(my_parameters->getMPIComm(), &tmp_comm);

        //create the spatial communicators:
        MPI_Comm_split(tmp_comm, getSpatialRank(mpi_rank, numProcS), mpi_rank, &spatialComm);

        //create the communicator for catalyst: includes all the firs sample ranks
        if( getStatisticalRank(mpi_rank, numProcS) == 0)
        {
                MPI_Comm_split(my_parameters->getMPIComm(), 0, mpi_rank, &coproc_comm);
        }else{
                MPI_Comm_split(my_parameters->getMPIComm(), MPI_UNDEFINED, mpi_rank, &coproc_comm);
        }

    //    MPI_Comm_free(&tmp_comm);

        if(getStatisticalRank(mpi_rank, numProcS) == 0)
        {
PRINTL

              if (Processor == NULL) //TODO how many tome can this be done?
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
                                PRINTL
                        }
                        else
                        {
                          PRINTL
                                std::cout<<"pipeline script: "<< script_loc<<std::endl;
                                pipeline->Initialize(script_loc);
                                Processor->AddPipeline(pipeline);
                        }

      }
      PRINTL
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
                dataDescription->GetInputDescriptionByName("input")->SetGrid(VTKGrid);
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
        if (VTKImage)
        {
                VTKImage->Delete();
                VTKImage = NULL;
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
