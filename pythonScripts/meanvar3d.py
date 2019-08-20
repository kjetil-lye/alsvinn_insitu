
#--------------------------------------------------------------

# Global timestep output options
timeStepToStartOutputAt=0
forceOutputAtFirstCall=False

# Global screenshot output options
imageFileNamePadding=0
rescale_lookuptable=False

# Whether or not to request specific arrays from the adaptor.
requestSpecificArrays=False

# a root directory under which all Catalyst output goes
rootDirectory=''

# makes a cinema D index table
make_cinema_table=False

#--------------------------------------------------------------
# Code generated from cpstate.py to create the CoProcessor.
# paraview version 5.6.1
#--------------------------------------------------------------

from paraview.simple import *
from paraview import coprocessing

# ----------------------- CoProcessor definition -----------------------

def CreateCoProcessor():
  def _CreatePipeline(coprocessor, datadescription):
    class Pipeline:
      # state file generated using paraview version 5.6.1

      # ----------------------------------------------------------------
      # setup views used in the visualization
      # ----------------------------------------------------------------

      # trace generated using paraview version 5.6.1
      #
      # To ensure correct image size when batch processing, please search 
      # for and uncomment the line `# renderView*.ViewSize = [*,*]`

      #### disable automatic camera reset on 'Show'
      paraview.simple._DisableFirstRenderCameraReset()

      # Create a new 'Render View'
      renderView1 = CreateView('RenderView')
      renderView1.ViewSize = [1584, 779]
      renderView1.AxesGrid = 'GridAxes3DActor'
      renderView1.CenterOfRotation = [3.5, 3.5, 3.5]
      renderView1.StereoType = 0
      renderView1.CameraPosition = [-17.219494382964726, 2.4177885578681693, 14.369353229214568]
      renderView1.CameraFocalPoint = [3.5, 3.5, 3.5]
      renderView1.CameraViewUp = [-0.03163149444460238, 0.9987328613689163, 0.03914230679275929]
      renderView1.CameraParallelScale = 6.06217782649107
      renderView1.Background = [0.32, 0.34, 0.43]

      # init the 'GridAxes3DActor' selected for 'AxesGrid'
      renderView1.AxesGrid.XTitleFontFile = ''
      renderView1.AxesGrid.YTitleFontFile = ''
      renderView1.AxesGrid.ZTitleFontFile = ''
      renderView1.AxesGrid.XLabelFontFile = ''
      renderView1.AxesGrid.YLabelFontFile = ''
      renderView1.AxesGrid.ZLabelFontFile = ''

      # register the view with coprocessor
      # and provide it with information such as the filename to use,
      # how frequently to write the images, etc.
      coprocessor.RegisterView(renderView1,
          filename='rho_mean_%t.png', freq=1, fittoscreen=1, magnification=1, width=1584, height=779, cinema={})
      renderView1.ViewTime = datadescription.GetTime()

      # Create a new 'Render View'
      renderView2 = CreateView('RenderView')
      renderView2.ViewSize = [1584, 779]
      renderView2.AxesGrid = 'GridAxes3DActor'
      renderView2.CenterOfRotation = [3.5, 3.5, 3.5]
      renderView2.StereoType = 0
      renderView2.CameraPosition = [-7.048161202762422, 3.95207463781137, 24.40797437522362]
      renderView2.CameraFocalPoint = [3.5, 3.5, 3.5]
      renderView2.CameraViewUp = [0.02413248500909191, 0.9996641992104772, -0.009439914414942461]
      renderView2.CameraParallelScale = 6.06217782649107
      renderView2.Background = [0.32, 0.34, 0.43]

      # init the 'GridAxes3DActor' selected for 'AxesGrid'
      renderView2.AxesGrid.XTitleFontFile = ''
      renderView2.AxesGrid.YTitleFontFile = ''
      renderView2.AxesGrid.ZTitleFontFile = ''
      renderView2.AxesGrid.XLabelFontFile = ''
      renderView2.AxesGrid.YLabelFontFile = ''
      renderView2.AxesGrid.ZLabelFontFile = ''

      # register the view with coprocessor
      # and provide it with information such as the filename to use,
      # how frequently to write the images, etc.
      coprocessor.RegisterView(renderView2,
          filename='rho_var_%t.png', freq=1, fittoscreen=1, magnification=1, width=1584, height=779, cinema={})
      renderView2.ViewTime = datadescription.GetTime()

      # ----------------------------------------------------------------
      # restore active view
      SetActiveView(renderView1)
      # ----------------------------------------------------------------

      # ----------------------------------------------------------------
      # setup the data processing pipelines
      # ----------------------------------------------------------------

      # create a new 'XML Partitioned Image Data Reader'
      # create a producer from a simulation input
      input = coprocessor.CreateProducer(datadescription, 'input')

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView1'
      # ----------------------------------------------------------------

      # show data from input
      inputDisplay = Show(input, renderView1)

      # get color transfer function/color map for 'rho_mean'
      rho_meanLUT = GetColorTransferFunction('rho_mean')
      rho_meanLUT.RGBPoints = [0.998567552707725, 0.231373, 0.298039, 0.752941, 1.4839643851239754, 0.865003, 0.865003, 0.865003, 1.969361217540226, 0.705882, 0.0156863, 0.14902]
      rho_meanLUT.ScalarRangeInitialized = 1.0

      # get opacity transfer function/opacity map for 'rho_mean'
      rho_meanPWF = GetOpacityTransferFunction('rho_mean')
      rho_meanPWF.Points = [0.998567552707725, 0.0, 0.5, 0.0, 1.969361217540226, 1.0, 0.5, 0.0]
      rho_meanPWF.ScalarRangeInitialized = 1

      # trace defaults for the display properties.
      inputDisplay.Representation = 'Volume'
      inputDisplay.ColorArrayName = ['POINTS', 'rho_mean']
      inputDisplay.LookupTable = rho_meanLUT
      inputDisplay.OSPRayScaleArray = 'rho_mean'
      inputDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
      inputDisplay.SelectOrientationVectors = 'None'
      inputDisplay.ScaleFactor = 0.7000000000000001
      inputDisplay.SelectScaleArray = 'None'
      inputDisplay.GlyphType = 'Arrow'
      inputDisplay.GlyphTableIndexArray = 'None'
      inputDisplay.GaussianRadius = 0.035
      inputDisplay.SetScaleArray = ['POINTS', 'rho_mean']
      inputDisplay.ScaleTransferFunction = 'PiecewiseFunction'
      inputDisplay.OpacityArray = ['POINTS', 'rho_mean']
      inputDisplay.OpacityTransferFunction = 'PiecewiseFunction'
      inputDisplay.DataAxesGrid = 'GridAxesRepresentation'
      inputDisplay.SelectionCellLabelFontFile = ''
      inputDisplay.SelectionPointLabelFontFile = ''
      inputDisplay.PolarAxes = 'PolarAxesRepresentation'
      inputDisplay.ScalarOpacityUnitDistance = 1.7320508075688772
      inputDisplay.ScalarOpacityFunction = rho_meanPWF
      inputDisplay.Slice = 3

      # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
      inputDisplay.DataAxesGrid.XTitleFontFile = ''
      inputDisplay.DataAxesGrid.YTitleFontFile = ''
      inputDisplay.DataAxesGrid.ZTitleFontFile = ''
      inputDisplay.DataAxesGrid.XLabelFontFile = ''
      inputDisplay.DataAxesGrid.YLabelFontFile = ''
      inputDisplay.DataAxesGrid.ZLabelFontFile = ''

      # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
      inputDisplay.PolarAxes.PolarAxisTitleFontFile = ''
      inputDisplay.PolarAxes.PolarAxisLabelFontFile = ''
      inputDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
      inputDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

      # setup the color legend parameters for each legend in this view

      # get color legend/bar for rho_meanLUT in view renderView1
      rho_meanLUTColorBar = GetScalarBar(rho_meanLUT, renderView1)
      rho_meanLUTColorBar.Title = 'rho_mean'
      rho_meanLUTColorBar.ComponentTitle = ''
      rho_meanLUTColorBar.TitleFontFile = ''
      rho_meanLUTColorBar.LabelFontFile = ''

      # set color bar visibility
      rho_meanLUTColorBar.Visibility = 1

      # show color legend
      inputDisplay.SetScalarBarVisibility(renderView1, True)

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView2'
      # ----------------------------------------------------------------

      # show data from input
      inputDisplay_1 = Show(input, renderView2)

      # get color transfer function/color map for 'rho_var'
      rho_varLUT = GetColorTransferFunction('rho_var')
      rho_varLUT.RGBPoints = [1.1303253888428344e-09, 0.231373, 0.298039, 0.752941, 0.09906810967287527, 0.865003, 0.865003, 0.865003, 0.19813621821542515, 0.705882, 0.0156863, 0.14902]
      rho_varLUT.ScalarRangeInitialized = 1.0

      # get opacity transfer function/opacity map for 'rho_var'
      rho_varPWF = GetOpacityTransferFunction('rho_var')
      rho_varPWF.Points = [1.1303253888428344e-09, 0.0, 0.5, 0.0, 0.19813621821542515, 1.0, 0.5, 0.0]
      rho_varPWF.ScalarRangeInitialized = 1

      # trace defaults for the display properties.
      inputDisplay_1.Representation = 'Volume'
      inputDisplay_1.ColorArrayName = ['POINTS', 'rho_var']
      inputDisplay_1.LookupTable = rho_varLUT
      inputDisplay_1.OSPRayScaleArray = 'rho_mean'
      inputDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
      inputDisplay_1.SelectOrientationVectors = 'None'
      inputDisplay_1.ScaleFactor = 0.7000000000000001
      inputDisplay_1.SelectScaleArray = 'None'
      inputDisplay_1.GlyphType = 'Arrow'
      inputDisplay_1.GlyphTableIndexArray = 'None'
      inputDisplay_1.GaussianRadius = 0.035
      inputDisplay_1.SetScaleArray = ['POINTS', 'rho_mean']
      inputDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
      inputDisplay_1.OpacityArray = ['POINTS', 'rho_mean']
      inputDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
      inputDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
      inputDisplay_1.SelectionCellLabelFontFile = ''
      inputDisplay_1.SelectionPointLabelFontFile = ''
      inputDisplay_1.PolarAxes = 'PolarAxesRepresentation'
      inputDisplay_1.ScalarOpacityUnitDistance = 1.7320508075688772
      inputDisplay_1.ScalarOpacityFunction = rho_varPWF
      inputDisplay_1.Slice = 3

      # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
      inputDisplay_1.DataAxesGrid.XTitleFontFile = ''
      inputDisplay_1.DataAxesGrid.YTitleFontFile = ''
      inputDisplay_1.DataAxesGrid.ZTitleFontFile = ''
      inputDisplay_1.DataAxesGrid.XLabelFontFile = ''
      inputDisplay_1.DataAxesGrid.YLabelFontFile = ''
      inputDisplay_1.DataAxesGrid.ZLabelFontFile = ''

      # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
      inputDisplay_1.PolarAxes.PolarAxisTitleFontFile = ''
      inputDisplay_1.PolarAxes.PolarAxisLabelFontFile = ''
      inputDisplay_1.PolarAxes.LastRadialAxisTextFontFile = ''
      inputDisplay_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

      # setup the color legend parameters for each legend in this view

      # get color legend/bar for rho_varLUT in view renderView2
      rho_varLUTColorBar = GetScalarBar(rho_varLUT, renderView2)
      rho_varLUTColorBar.Title = 'rho_var'
      rho_varLUTColorBar.ComponentTitle = ''
      rho_varLUTColorBar.TitleFontFile = ''
      rho_varLUTColorBar.LabelFontFile = ''

      # set color bar visibility
      rho_varLUTColorBar.Visibility = 1

      # show color legend
      inputDisplay_1.SetScalarBarVisibility(renderView2, True)

      # ----------------------------------------------------------------
      # setup color maps and opacity mapes used in the visualization
      # note: the Get..() functions create a new object, if needed
      # ----------------------------------------------------------------

      # ----------------------------------------------------------------
      # finally, restore active source
      SetActiveSource(input)
      # ----------------------------------------------------------------
    return Pipeline()

  class CoProcessor(coprocessing.CoProcessor):
    def CreatePipeline(self, datadescription):
      self.Pipeline = _CreatePipeline(self, datadescription)

  coprocessor = CoProcessor()
  # these are the frequencies at which the coprocessor updates.
  freqs = {'input': [1, 1]}
  coprocessor.SetUpdateFrequencies(freqs)
  if requestSpecificArrays:
    arrays = [['rho_mean', 0], ['rho_var', 0]]
    coprocessor.SetRequestedArrays('input', arrays)
  coprocessor.SetInitialOutputOptions(timeStepToStartOutputAt,forceOutputAtFirstCall)

  if rootDirectory:
      coprocessor.SetRootDirectory(rootDirectory)

  if make_cinema_table:
      coprocessor.EnableCinemaDTable()

  return coprocessor


#--------------------------------------------------------------
# Global variable that will hold the pipeline for each timestep
# Creating the CoProcessor object, doesn't actually create the ParaView pipeline.
# It will be automatically setup when coprocessor.UpdateProducers() is called the
# first time.
coprocessor = CreateCoProcessor()

#--------------------------------------------------------------
# Enable Live-Visualizaton with ParaView and the update frequency
coprocessor.EnableLiveVisualization(False, 1)

# ---------------------- Data Selection method ----------------------

def RequestDataDescription(datadescription):
    "Callback to populate the request for current timestep"
    global coprocessor

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
    coprocessor.WriteImages(datadescription, rescale_lookuptable=rescale_lookuptable,
        image_quality=0, padding_amount=imageFileNamePadding)

    # Live Visualization, if enabled.
    coprocessor.DoLiveVisualization(datadescription, "localhost", 22222)
