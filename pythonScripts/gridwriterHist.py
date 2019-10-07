from paraview.simple import *

from paraview import coprocessing

# the frequency to output everything
outputfrequency = 1

# trace generated using paraview version 5.6.1
#
# To ensure correct image size when batch processing, please search
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).



#--------------------------------------------------------------
# Code generated from cpstate.py to create the CoProcessor.


# ----------------------- CoProcessor definition -----------------------

def CreateCoProcessor():
  def _CreatePipeline(coprocessor, datadescription):
    class Pipeline:
      adaptorinput = coprocessor.CreateProducer( datadescription, "input")
      grid = adaptorinput.GetClientSideObject().GetOutputDataObject(0)

      filename = None
      if  grid.IsA('vtkImageData') or grid.IsA('vtkUniformGrid'):
        writer = servermanager.writers.XMLPImageDataWriter(Input=adaptorinput)
        filename = 'input_%t.pvti'
      elif  grid.IsA('vtkRectilinearGrid'):
        writer = servermanager.writers.XMLPRectilinearGridWriter(Input=adaptorinput)
        filename = 'input_%t.pvtr'
      elif  grid.IsA('vtkStructuredGrid'):
        writer = servermanager.writers.XMLPStructuredGridWriter(Input=adaptorinput)
        filename = 'input_%t.pvts'
      elif  grid.IsA('vtkPolyData'):
        writer = servermanager.writers.XMLPPolyDataWriter(Input=adaptorinput)
        filename = 'input_%t.pvtp'
      elif  grid.IsA('vtkUnstructuredGrid'):
        writer = servermanager.writers.XMLPUnstructuredGridWriter(Input=adaptorinput)
        filename = 'input_%t.pvtu'
      elif  grid.IsA('vtkUniformGridAMR'):
        writer = servermanager.writers.XMLHierarchicalBoxDataWriter(Input=adaptorinput)
        filename = 'input_%t.vthb'
      elif  grid.IsA('vtkMultiBlockDataSet'):
        writer = servermanager.writers.XMLMultiBlockDataWriter(Input=adaptorinput)
        filename = 'input_%t.vtm'
      elif  grid.IsA('vtkHyperTreeGrid'):
        writer = servermanager.writers.HyperTreeGridWriter(Input=adaptorinput)
        filename = 'input_%t.htg'
      else:
        print("Don't know how to create a writer for a ", grid.GetClassName())

      if filename:
        coprocessor.RegisterWriter(writer, filename, freq=outputfrequency)


      print(" ==========================================================", datadescription.GetUserData().GetNumberOfArrays())
      print(" ==========================================================", datadescription.GetUserData().GetArrayName(1))

      histogram1 = Histogram(Input=datadescription
      histogram1.SelectInputArray = ['FIELD', 'hist_E30']
      histogram1.CustomBinRanges = [0, 6.785086070491616]

    # get active view
      barChartView1 = GetActiveViewOrCreate('XYBarChartView')
    # uncomment following to set a specific view size
    # barChartView1.ViewSize = [415, 779]

    # show data in view
      histogram1Display = Show(histogram1, barChartView1)

    # trace defaults for the display properties.
      histogram1Display.CompositeDataSetIndex = [0]
      histogram1Display.AttributeType = 'Row Data'
      histogram1Display.UseIndexForXAxis = 0
      histogram1Display.XArrayName = 'bin_extents'
      histogram1Display.SeriesVisibility = ['bin_values']
      histogram1Display.SeriesLabel = ['bin_extents', 'bin_extents', 'bin_values', 'bin_values']
      histogram1Display.SeriesColor = ['bin_extents', '0', '0', '0', 'bin_values', '0.89', '0.1', '0.11']
      histogram1Display.SeriesPlotCorner = ['bin_extents', '0', 'bin_values', '0']
      histogram1Display.SeriesLabelPrefix = ''
      barChartView1.Update()
      SetActiveView(barChartView1)
      inputDisplay = Show(input, barChartView1)






    return Pipeline()

  class CoProcessor(coprocessing.CoProcessor):
    def CreatePipeline(self, datadescription):
      self.Pipeline = _CreatePipeline(self, datadescription)


  coprocessor = CoProcessor()
  freqs = {'input': [outputfrequency]}
  coprocessor.SetUpdateFrequencies(freqs)
  return coprocessor

#--------------------------------------------------------------
# Global variables that will hold the pipeline for each timestep
# Creating the CoProcessor object, doesn't actually create the ParaView pipeline.
# It will be automatically setup when coprocessor.UpdateProducers() is called the
# first time.
coprocessor = CreateCoProcessor()

#--------------------------------------------------------------
# Enable Live-Visualizaton with ParaView
coprocessor.EnableLiveVisualization(False)


# ---------------------- Data Selection method ----------------------

def RequestDataDescription(datadescription):
    "Callback to populate the request for current timestep"
    global coprocessor
    if datadescription.GetForceOutput() == True:
        # We are just going to request all fields and meshes from the simulation
        # code/adaptor.
        for i in range(datadescription.GetNumberOfInputDescriptions()):
            datadescription.GetInputDescription(i).AllFieldsOn()
            datadescription.GetInputDescription(i).GenerateMeshOn()
        return
    # setup requests for all inputs based on the requirements of the
    # pipeline.
    coprocessor.LoadRequestedData(datadescription)

# ------------------------ Processing method ------------------------

def DoCoProcessing(datadescription):
    "Callback to do co-processing for current timestep"
    global coprocessor

    # Update the coprocessor by providing it the newly generated simulation data.
    # If the pipeline hasn't been setup yet, this will setup the pipeline.
    coprocessor.UpdateProducers(datadescription)

    # Write output data, if appropriate.
    coprocessor.WriteData(datadescription);

    # Write image capture (Last arg: rescale lookup table), if appropriate.
    coprocessor.WriteImages(datadescription, rescale_lookuptable=False)


    # Live Visualization, if enabled.
    coprocessor.DoLiveVisualization(datadescription, "localhost", 22222)
