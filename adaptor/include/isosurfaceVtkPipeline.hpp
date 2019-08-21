//#ifndef isosurfaceVtkPipeline_H
//#define isosurfaceVtkPipeline_H

#include <string>
#include <vtkCPPipeline.h>

class vtkCPDataDescription;
class vtkCPPythonHelper;

class isosurfaceVtkPipeline : public vtkCPPipeline
{
public:

  static isosurfaceVtkPipeline* New();
  vtkTypeMacro(isosurfaceVtkPipeline, vtkCPPipeline);
  virtual void PrintSelf(ostream& os, vtkIndent indent);

  virtual void Initialize(int outputFrequency, std::string& fileName);

  virtual int RequestDataDescription(vtkCPDataDescription* dataDescription);

  virtual int CoProcess(vtkCPDataDescription* dataDescription);

protected:
  isosurfaceVtkPipeline();
  virtual ~isosurfaceVtkPipeline();

private:
  isosurfaceVtkPipeline(const isosurfaceVtkPipeline&) VTK_DELETE_FUNCTION;
  void operator=(const isosurfaceVtkPipeline&) VTK_DELETE_FUNCTION;

  int OutputFrequency;
  std::string FileName;
};
//#endif
