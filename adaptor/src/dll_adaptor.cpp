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

        std::cout << "In create" << std::endl;
        /*auto my_parameters = static_cast<MyParameters*>(parameters);
        auto script_loc = my_parameters->getParameter("pipelineScript");
        const char *script_char = script_loc.c_str();*/

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

        std::string script_loc = "/home/ramona/MasterthesisLOCAL/coding/alsvinn_insitu/scripts/gridwriter.py";
        const char *script_char = "/home/ramona/MasterthesisLOCAL/coding/alsvinn_insitu/scripts/gridwriter.py";

        std::cout<< "Python script : "<< script_loc<<std::endl;
        std::cout<< "Python script : "<< script_char<<std::endl;


       if(script_loc !="")
        {
          vtkNew<vtkCPPythonScriptPipeline> pipeline;

          pipeline->Initialize(script_char);

          Processor->AddPipeline(pipeline.GetPointer());


        }

        //@Todo: should be able to load multiple script for pipeline:
        /*
        scripts are passed in as command line arguments
        for(int i=0;i<numScripts;i++)
        {
        vtkCPPythonScriptPipeline* pipeline =
        vtkCPPythonScriptPipeline::New();
        pipeline->Initialize(scripts[i]);
        Processor->AddPipeline(pipeline);
        pipeline->Delete();
        }
        */

        PRINT_PARAM(simulator_name);
        PRINT_PARAM(simulator_version);
        PRINT_PARAM(parameters);

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
* CoProcesses
*
* @param nx, ny, nz are number of ghost cells in respective direction
*/
    DLL_ADAPTOR_EXPORT void CatalystCoProcess(void* data, void* parameters, double time,
        const char* variable_name,  double* variable_data, int nx, int ny, int nz,
        int ngx, int ngy, int ngz, double ax, double ay, double az, double bx,
        double by, double bz, int gpu_number ) {

        std::cout << "================ CatalystCoProcess" << std::endl;

        auto my_data = static_cast<MyData*>(data);
        auto my_parameters = static_cast<MyParameters*>(parameters);
        auto timeStep = my_data->getCurrentTimestep();

        vtkCPDataDescription* dataDescription = vtkCPDataDescription::New();
        dataDescription->SetTimeData(time, timeStep);
        dataDescription->AddInput("input");

        // the last time step shuld always be output
        if(my_data->getEndTimestep()){
              dataDescription->ForceOutputOn();
              std::cout << "force" << std::endl;
        }



        if (Processor->RequestDataDescription(dataDescription)!=0)
        {
          if (VTKGrid == NULL)
          {
            VTKGrid = vtkImageData::New();
            VTKGrid->SetExtent(ngx, ngx+nx, ngy, ngy+ny, ngz, ngz+nz);
          }

            dataDescription->GetInputDescriptionByName("input")->SetGrid(VTKGrid);
            // For structured grids we need to specify the global data extents
            dataDescription->GetInputDescriptionByName("input")->SetWholeExtent(ngx, ngx+nx, ngy, ngy+ny, ngz, ngz+nz);

            // Create a field associated with points
            vtkDoubleArray* field_array = vtkDoubleArray::New();
            field_array->SetName(variable_name);
            field_array->SetArray(variable_data, VTKGrid->GetNumberOfPoints(), 1);
            VTKGrid->GetPointData()->AddArray(field_array);
            field_array->Delete();
            Processor->CoProcess(dataDescription);
            }
            dataDescription->Delete();
  std::cout << "In ccp 5" << std::endl;

    }

    DLL_ADAPTOR_EXPORT void* make_parameters() {
        std::cout << "In make_parameters" << std::endl;

        return static_cast<void*>(new MyParameters());
      }


    DLL_ADAPTOR_EXPORT void delete_parameters(void* parameters) {
        std::cout << "In delete_parameters" << std::endl;
    //    PRINT_PARAM(parameters);
        delete static_cast<MyParameters*>(parameters);
    }

    DLL_ADAPTOR_EXPORT bool needs_data_on_host(void* data, void* parameters) {
        std::cout << "in needs_data_on_host" << std::endl;

    //    PRINT_PARAM(data);
    //    PRINT_PARAM(parameters);

        return true;

    }

    DLL_ADAPTOR_EXPORT void set_parameter(void* parameters, const char* key,
        const char* value) {

        std::cout << "In set_parameter" << std::endl;

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
        std::cout << "in new_timestep" << std::endl;

        PRINT_PARAM(data);
        PRINT_PARAM(parameters);
        PRINT_PARAM(time);
        PRINT_PARAM(timestep_number);

        auto my_data = static_cast<MyData*>(data);
        my_data->setCurrentTimestep(timestep_number);

    }


    DLL_ADAPTOR_EXPORT void end_timestep(void* data, void* parameters, double time,
        int timestep_number) {
        std::cout << "in end_timestep" << std::endl;

        PRINT_PARAM(data);
        PRINT_PARAM(parameters);
        PRINT_PARAM(time);
        PRINT_PARAM(timestep_number);

    //    auto my_data = static_cast<MyData*>(data);
    //    if(false) my_data->setEndTimeStep(true);

    }

}//extern c
