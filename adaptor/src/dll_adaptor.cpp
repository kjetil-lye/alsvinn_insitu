#include "dll_adaptor.hpp"
#include "parameters.hpp"
#include "data.hpp"
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

        //default script
        const char *script_default = "/home/ramona/MasterthesisLOCAL/coding/alsvinn_insitu/scripts/gridwriter.py";
        auto my_parameters = static_cast<MyParameters*>(parameters);
        const std::string script_str = my_parameters->getParameter("pipelineScript");
        const char *script_loc = script_str.c_str();

        vtkNew<vtkCPPythonScriptPipeline> pipeline;
       if(script_str =="none")
        {
            pipeline->Initialize(script_default);
            std::cout<<"pipeline script: "<< script_default<<std::endl;
        }
        else{
            pipeline->Initialize(script_loc);
            std::cout<<"pipeline script: "<< script_loc<<std::endl;
        }
        Processor->AddPipeline(pipeline.GetPointer());


  /* @TOO DO WE NEED MULTIPLE SCRIPTS?
        for(int i=0;i<numScripts;i++)
        {
            vtkCPPythonScriptPipeline* pipeline =d
            vtkCPPythonScriptPipeline::New();
            pipeline->Initialize(scripts[i]);
            Processor->AddPipeline(pipeline);
            pipeline->Delete();
        }
*/

        const int endTime = std::stoi(my_parameters->getParameter("endTime"));
        MyData *my_data = new MyData;
        my_data-> setEndTimeStep(endTime);

        return   static_cast<void*>(my_data);

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

        auto my_data = static_cast<MyData*>(data);
        auto my_parameters = static_cast<MyParameters*>(parameters);
        auto timeStep = my_data->getCurrentTimestep();
        const std::string description_namestr = my_parameters->getParameter("basename");
        const char *description_name = description_namestr.c_str();

        vtkCPDataDescription* dataDescription = vtkCPDataDescription::New();
        dataDescription->SetTimeData(time, timeStep);
        dataDescription->AddInput("input");

        // the last time step shuld always be output
        if(my_data->getEndTimestep()){
              dataDescription->ForceOutputOn();
              std::cout << "force" << std::endl;
        }
        std::cout << "description_name " <<description_name<< std::endl;
        std::cout << "variable_name: " <<variable_name<< std::endl;

        //since we take the number of outputs from the alsvinn simulation and not form the PythonScriptProcessor ->RequestDataDescription(dataDescription)!=0)
        //either we are looking at new variable or new timestep or the last time step
    //    if (Processor ->RequestDataDescription(dataDescription)!=0 )
      if(my_data->getNewVariable(variable_name) || my_data->getNewTimestep() || my_data->getEndTimestep() )
        {
      //   int extend[6]  = {0, ngx+nx, 0, ngy+ny, 0, 0}; //0, nx, 0, ny, 0,0 };
        int extend[6]  = {0,nx,0,ny,0,nz};//{ngx, nx+ngx, ngy, ny+ngy, ngz, 0}; //nz+ngz };
          for (size_t i = 0; i < 6; i++)
          		std::cout << extend[i] << ' ';
          std::cout<<std::endl;


         std::cout <<"size of vairable data " << sizeof(variable_data)/sizeof(variable_data[0]) <<std::endl;


          if (VTKGrid == NULL)
          {
            VTKGrid = vtkImageData::New();
            VTKGrid->SetExtent(extend); //ngx, ngx+nx, ngy, ngy+ny, ngz, ngz+nz);
          }


            dataDescription->GetInputDescriptionByName("input")->SetGrid(VTKGrid);
            // For structured grids we need to specify the global data extents
            dataDescription->GetInputDescriptionByName("input")->SetWholeExtent(extend); //ngx, ngx+nx, ngy, ngy+ny, ngz, ngz+nz);

    /*     const int maxIndex = nx*ny*nz; // (nz+ngz-1)*(nx+2*ngx)*(ny+2*ngy)+(ny+ngy-1)*(nx*2*ngx)+(nx+ngx-1); //nx*ny*nz
            // Create a field associated with points
            vtkDoubleArray* field_array = vtkDoubleArray::New();

            field_array->SetNumberOfComponents(1);
            field_array->SetNumberOfTuples(maxIndex);
            field_array->SetName(variable_name);
              std::cout << "h " <<3<< std::endl;
            int index = 0;
            for (int z = ngz; z < nz + ngz; ++z) {
                // ignoring ghost cells (ngy is number of ghost cells in y direction)
                for (int y = ngy; y < ny + ngy; ++y) {
                    // ignoring ghost cells (ngx is number of ghost cells in x direction)
                    for (int x = ngx; x < nx + ngx; ++x) {
                         index = z * (nx + 2 * ngx) * (ny + 2 * ngy) + y * (nx + 2 * ngx) + x;
                        field_array->SetValue(index, variable_data[index]);
                        std::cout << "z " <<z<< std::endl;
                        std::cout << "x " <<x<< std::endl;
                        std::cout << "y " <<y<< std::endl;
                        std::cout << "index " <<index<< std::endl;
                          std::cout << "maxindex " <<maxIndex<< " " <<127*127 <<std::endl;
                    }
                }

            }*/




              vtkDoubleArray* field_array = vtkDoubleArray::New();
              field_array->SetName(variable_name);
              field_array->SetArray(variable_data, VTKGrid->GetNumberOfPoints(), 1);
              VTKGrid->GetPointData()->AddArray(field_array);
              field_array->Delete();

            Processor->CoProcess(dataDescription);
          }

            dataDescription->Delete();
            my_data->setNewTimestep(false);
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

        auto my_data = static_cast<MyData*>(data);
        my_data->setCurrentTimestep(timestep_number);
        my_data->setNewTimestep(true);

    }


    DLL_ADAPTOR_EXPORT void end_timestep(void* data, void* parameters, double time,
        int timestep_number) {
        PRINT_PARAM(timestep_number);
    }

}//extern c
