#include "dll_adaptor.hpp"
#include "parameters.hpp"
#include "data.hpp"
#include "histogram.hpp"
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
#include<vtkBlankStructuredGrid.h>
#include <vtkFieldData.h>
#include <vtkNew.h>
#include <vtkPointData.h>
#include <vtkPoints.h>
#include <vtkMPI.h>
#include <iterator>

#include<cmath>

#define ADAPTOR_HISTORGAM 1
#define ADAPTOR_USE_VTKCPPROCESSOR 0

#define PRINTL { int rank; MPI_Comm_rank(MPI_COMM_WORLD, &rank); std::cout << "In rank " << rank << ", at line: " <<__LINE__ << std::endl; }
// Simple macro to print parameters
#define PRINT_PARAM(X) std::cout << "Value of " << #X << " is " << X << std::endl
extern "C" {

void CatalystCoProcesHistogram(void* data, void* parameters, double time,
                                          const char* variable_name,  double* variable_data, int nx, int ny, int nz,
                                          int ngx, int ngy, int ngz, double ax, double ay, double az, double bx,
                                          double by, double bz, int gpu_number );
/*
int getRankIndex(int nx, int ny, int nz, int ngx, int ngy, int ngz, double x, double y, double z);
void make_histogramVTK(const char* variable_name, const int pntidx,  double* values, const int values_size,
                      const double min, const double max, const int nbins,
                      vtkFloatArray* bins, vtkIntArray* hist);

void write_histogram( const char* variable_name, const std::string pntidx,   const int values_size,double* values, const double min, const double max, const int nbins, const std::string path);

void write_2pt_histogram( const char* variable_name,  const int values_size, const std::string name, double* values1,  const double min1, const double max1, double* values2, const double min2, const double max2, const int nbins, const std::string path);
*/

vtkCPProcessor* Processor = NULL;
vtkImageData* VTKGrid = NULL;
vtkBlankStructuredGrid* histGrid = NULL;
MPI_Comm coproc_comm;
vtkMPICommunicatorOpaqueComm* Comm = NULL;
vtkCPDataDescription*  dataDescription = NULL ; //vtkCPDataDescription::New();

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

        if(ADAPTOR_HISTORGAM)
        {

         CatalystCoProcesHistogram(data, parameters, time, variable_name,  variable_data, nx,  ny,  nz,
                                                     ngx,  ngy,  ngz,  ax,  ay,  az,  bx,
                                                     by,  bz,  gpu_number );

        }
        else
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

                // make nsamples per group, to use for normalzation:
                if(nsamples%mpi_size!=0) {
                        std::cerr<< "warning: nsmaples not divisible by mpi_size : "<< nsamples/mpi_size<<std::endl;
                }

//                std::cout<<"mpi rank : "<<mpi_rank<< " at variable "<< variable_name<<std::endl;

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


                if(mpi_rank == 0)
                {
                        auto my_data = static_cast<MyData*>(data);

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

                                VTKGrid->GetPointData()->AddArray(field_array_mean);
                                VTKGrid->GetPointData()->AddArray(field_array_var);
                                field_array_mean->Delete();
                                field_array_var->Delete();
                }//end rank 0

      }//endif(ADAPTOR_HISTORGAM)
}


void CatalystCoProcesHistogram(void* data, void* parameters, double time,
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

                  // make nsamples per group, to use for normalzation:
                  if(nsamples%mpi_size!=0) {
                          std::cerr<< "warning: nsmaples not divisible by mpi_size : "<< nsamples/mpi_size<<std::endl;
                  }

                  int norm_samples = nsamples;
                  const size_t ndata = (ngx*2+nx)*(ny+2*ngy)*(nz+2*ngz);
                  double avrg_data[ndata];
                  double avrg_sqr_data[ndata];


                  //historgram calculcation for specifc points only;
                  const int nii = std::stoi(my_parameters->getParameter("hist_npoints"));
                  const bool twoPoint = std::stoi(my_parameters->getParameter("hist_2points"));
                  double px[nii];
                  double py[nii];
                  double pz[nii];
                  getPoints(px,py,pz, nii);
                  double *pnt_values;
                  const int pnt_values_size = nii*nsamples;


                          if(mpi_rank ==0)
                          {
                                  pnt_values = (double*)malloc(sizeof(double) * (pnt_values_size));
                          }

                          //collect data points from all frames to store all frame values for specifc points
                          for ( int i =0; i<nii; i++)
                          {
                                  int idx = getRankIndex(nx, ny, nz,  ngx, ngy, ngz, px[i], py[i], pz[i]);

                //                  std::cout<< "rank, pt " << mpi_rank << " "<< idx<<" " <<*(variable_data+idx)<<std::endl;
                                  MPI_Gather(variable_data+idx, 1,  MPI_DOUBLE,  pnt_values+(i*nsamples), 1, MPI_DOUBLE, 0,  my_parameters->getMPIComm());
                          }



                  MPI_Reduce(variable_data, avrg_data, ndata, MPI_DOUBLE, MPI_SUM, 0, my_parameters->getMPIComm());

                  double sqr_variable_data[ndata];
                  //get squared sum to use for variance, reuse variable_data to save space
                  for (int i = 0; i< ndata; ++i) {
                          sqr_variable_data[i] = variable_data[i]*variable_data[i];
                  }


                  MPI_Reduce(&sqr_variable_data, avrg_sqr_data, ndata, MPI_DOUBLE, MPI_SUM, 0, my_parameters->getMPIComm());


                  if(mpi_rank == 0)
                  {

                              //collect data points from all frames to store all frame values for specifc points
                            const std::string path = my_parameters->getParameter("hist_folder");
                           //historgram calculcation for specifc points only;
                            const int nbins = std::stoi(my_parameters->getParameter("hist_nbins"));

                                  for ( int i =0; i<nii; i++)
                                   {
                                        std::string pntname = std::to_string( px[i]).substr(0,4)+"x"+ std::to_string( py[i]).substr(0,4)+"y"+ std::to_string( pz[i]).substr(0,4)+"z_"+std::to_string(time).substr(0,4);
                                         auto minmax = std::minmax_element(pnt_values+(i*nsamples),pnt_values+(i+1)*nsamples );

                                    if(!twoPoint)
                                        {
                                            write_histogram(  variable_name, pntname, nsamples, pnt_values+(i*nsamples), *(minmax.first),  *(minmax.second),  nbins, path);
                                          }
                                        else if(twoPoint && i <nii-1)
                                          {
                                            pntname += "_"+ std::to_string( px[i+1]).substr(0,4)+"x"+ std::to_string( py[i+1]).substr(0,4)+"y"+ std::to_string( pz[i+1]).substr(0,4)+"z_"+std::to_string(time).substr(0,4);
                                            auto minmax2  = std::minmax_element(pnt_values+(i+1)*nsamples, pnt_values+(i+2)*nsamples);
                                            write_2pt_histogram( variable_name, nsamples,pntname, pnt_values+(i*nsamples),*(minmax.first),  *(minmax.second), pnt_values+((i+1)*nsamples), *(minmax2.first),  *(minmax2.second),  nbins, path);

                                          }

                                  }


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

                                  VTKGrid->GetPointData()->AddArray(field_array_mean);
                                  VTKGrid->GetPointData()->AddArray(field_array_var);
                                  field_array_mean->Delete();
                                  field_array_var->Delete();
                          free(pnt_values);
                  }//end rank 0
    } //CatalystCoProcesHistogram



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



}                                                                                                                                                                                                                                                    //extern c
