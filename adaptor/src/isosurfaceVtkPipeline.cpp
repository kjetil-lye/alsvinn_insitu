#include "isosurfaceVtkPipeline.hpp"

#include <vtkCPDataDescription.h>
#include <vtkCPInputDataDescription.h>
#include <vtkCommunicator.h>
#include <vtkCompleteArrays.h>
#include <vtkDataArray.h>
#include <vtkMultiProcessController.h>
#include <vtkNew.h>
#include <vtkObjectFactory.h>
#include <vtkPVArrayCalculator.h>
#include <vtkPVTrivialProducer.h>
#include <vtkPointData.h>
#include <vtkSMProxyManager.h>
#include <vtkThreshold.h>

#include <vtkXMLImageDataWriter.h>
#include <vtkSmartPointer.h>
#include <vtkImageData.h>
#include <sstream>
#include <string>

vtkStandardNewMacro(isosurfaceVtkPipeline);

//----------------------------------------------------------------------------
isosurfaceVtkPipeline::isosurfaceVtkPipeline()
{
  this->OutputFrequency = 1;
}

//----------------------------------------------------------------------------
isosurfaceVtkPipeline::~isosurfaceVtkPipeline()
{
}

//----------------------------------------------------------------------------
void isosurfaceVtkPipeline::Initialize(int outputFrequency, std::string& fileName)
{
  this->OutputFrequency = outputFrequency;
  this->FileName = fileName;
}

//----------------------------------------------------------------------------
int isosurfaceVtkPipeline::RequestDataDescription(vtkCPDataDescription* dataDescription)
{
  if (!dataDescription)
  {
    vtkWarningMacro("dataDescription is NULL.");
    return 0;
  }

  if (this->FileName.empty())
  {
    vtkWarningMacro("No output file name given to output results to.");
    return 0;
  }

  if (dataDescription->GetForceOutput() == true ||
    (this->OutputFrequency != 0 && dataDescription->GetTimeStep() % this->OutputFrequency == 0))
  {
    dataDescription->GetInputDescriptionByName("input")->AllFieldsOn();
    dataDescription->GetInputDescriptionByName("input")->GenerateMeshOn();
    return 1;
  }
  return 0;
}

//----------------------------------------------------------------------------
int isosurfaceVtkPipeline::CoProcess(vtkCPDataDescription* dataDescription)
{
  const double ISO_VAL =   1;
  const double ISO_BOUNDS = 0.1;


  if (!dataDescription)
  {
    vtkWarningMacro("DataDescription is NULL");
    return 0;
  }

  vtkImageData* grid = vtkImageData::SafeDownCast(
    dataDescription->GetInputDescriptionByName("input")->GetGrid());
  if (grid == NULL)
  {
    vtkWarningMacro("DataDescription is missing input vtkImageData grid.");
    return 0;
  }
  if (this->RequestDataDescription(dataDescription) == 0)
  {
    return 1;
  }

  vtkNew<vtkPVTrivialProducer> producer;
  producer->SetOutput(grid);


  // If process 0 doesn't have any points or cells, the writer may
  // have problems in parallel so we use completeArrays to fill in
  // the missing information.
//  vtkNew<vtkCompleteArrays> completeArrays;
//  completeArrays->SetInputConnection(threshold->GetOutputPort());

  vtkSmartPointer<vtkXMLImageDataWriter> writer =
    vtkSmartPointer<vtkXMLImageDataWriter>::New();
//  writer->SetFileName("imagedata.vti");
  writer->SetInputData(grid);
  //writer->Write();
  std::ostringstream o;
  o << dataDescription->GetTimeStep();
  std::string name = "./"+ this->FileName + o.str() + ".vti";
  writer->SetFileName(name.c_str());
  writer->Update();

/*

//extract points with certain values

//@assumption same numbe rof cells in each dimension
// create new grid of a smaller dimension

int* dims = grid->GetDimensions();
std::cout << "Dims: " << " x: " << dims[0] << " y: " << dims[1] << " z: " << dims[2] << std::endl;

  std::cout << "Number of points: " << grid->GetNumberOfPoints() << std::endl;
  std::cout << "Number of cells: " << grid->GetNumberOfCells() << std::endl;

int dimsIso = 0;

// at least two dimesions for the isosurface
if( (dims[0]>1 && dims[1]>1 )|| ( dims[2]>1 && dims[0]>1) || (dims[0] >1 && dims[2]) )
{
  int dimsIsoY = 1;
  vtkSmartPointer<vtkImageData> isosurfaceImage = vtkSmartPointer<vtkImageData>::New();

// 3 dims
  if( dims[0]>1 && dims[1]>1 && dims[2]>1){

    isosurfaceImage->SetDimensions(dims[0], dims[1], 1);
    dimsIso = dims[1];

  }else{    // 2dims
   isosurfaceImage->SetDimensions(dims[0], 1, 1);
   dimsIso = 0;
}
isosurfaceImage->AllocateScalars(VTK_DOUBLE,1);

int* dims1 = isosurfaceImage->GetDimensions();
std::cout << "Dims: " << " x: " << dims1[0] << " y: " << dims1[1] << " z: " << dims1[2] << std::endl;


for (int z = 0; z < dims[2]; z++)
{
for (int y = 0; y < dims[1]; y++)
  {
  for (int x = 0; x < dims[0]; x++)
    {
      std::cout << "loop: " << " x: " << x << " y: " <<y << " z: " << z << std::endl;

      double* iso_val = static_cast<double*>(isosurfaceImage->GetScalarPointer(x,dimsIso,0));

      iso_val[0] =0.0;
        std::cout << "after isoval"  << std::endl;
        std::cout<< " type "<< grid->GetScalarTypeAsString()<<std::endl;
      double* old_val = static_cast<double*>(grid->GetScalarPointer(x,y,z));


      std::cout << "old val " << old_val[0]  << std::endl;

    if( ISO_VAL-ISO_BOUNDS < old_val[0] && old_val[0] > ISO_VAL+ISO_BOUNDS){
      iso_val[0] = 1.0;
            std::cout << "in bounds"  << std::endl;
    }


    }

  }

}
std::cout << "after loop: "   << std::endl;


vtkSmartPointer<vtkXMLImageDataWriter> writer2 =
  vtkSmartPointer<vtkXMLImageDataWriter>::New();
//  writer->SetFileName("imagedata.vti");
writer2->SetInputData(isosurfaceImage);
//writer->Write();
std::string name = "./iso" + o.str() + ".vti";
writer2->SetFileName(name.c_str());
writer2->Update();


}
*/




  return 1;
}

//----------------------------------------------------------------------------
void isosurfaceVtkPipeline::PrintSelf(ostream& os, vtkIndent indent)
{
  this->Superclass::PrintSelf(os, indent);
  os << indent << "OutputFrequency: " << this->OutputFrequency << "\n";
  os << indent << "FileName: " << this->FileName << "\n";
}
