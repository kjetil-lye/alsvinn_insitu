
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
# paraview version 5.6.0
#--------------------------------------------------------------

from paraview.simple import *
from paraview import coprocessing

# ----------------------- CoProcessor definition -----------------------

def CreateCoProcessor():
  def _CreatePipeline(coprocessor, datadescription):
    class Pipeline:
      # state file generated using paraview version 5.6.0

      # ----------------------------------------------------------------
      # setup views used in the visualization
      # ----------------------------------------------------------------

      # trace generated using paraview version 5.6.0
      #
      # To ensure correct image size when batch processing, please search 
      # for and uncomment the line `# renderView*.ViewSize = [*,*]`

      #### disable automatic camera reset on 'Show'
      paraview.simple._DisableFirstRenderCameraReset()

      # Create a new 'Render View'
      renderView1 = CreateView('RenderView')
      renderView1.ViewSize = [1505, 709]
      renderView1.AnnotationColor = [0.0, 0.0, 0.0]
      renderView1.InteractionMode = '2D'
      renderView1.AxesGrid = 'GridAxes3DActor'
      renderView1.OrientationAxesVisibility = 0
      renderView1.OrientationAxesLabelColor = [0.0, 0.0, 0.0]
      renderView1.OrientationAxesOutlineColor = [0.0, 0.0, 0.0]
      renderView1.CenterOfRotation = [31.5, 31.5, 0.0]
      renderView1.StereoType = 0
      renderView1.CameraPosition = [37.73125023694214, 31.08458331753719, 10000.0]
      renderView1.CameraFocalPoint = [37.73125023694214, 31.08458331753719, 0.0]
      renderView1.CameraParallelScale = 36.816303483266516
      renderView1.Background = [1.0, 1.0, 1.0]

      # init the 'GridAxes3DActor' selected for 'AxesGrid'
      renderView1.AxesGrid.XTitleColor = [0.0, 0.0, 0.0]
      renderView1.AxesGrid.XTitleFontFile = ''
      renderView1.AxesGrid.YTitleColor = [0.0, 0.0, 0.0]
      renderView1.AxesGrid.YTitleFontFile = ''
      renderView1.AxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
      renderView1.AxesGrid.ZTitleFontFile = ''
      renderView1.AxesGrid.GridColor = [0.0, 0.0, 0.0]
      renderView1.AxesGrid.XLabelColor = [0.0, 0.0, 0.0]
      renderView1.AxesGrid.XLabelFontFile = ''
      renderView1.AxesGrid.YLabelColor = [0.0, 0.0, 0.0]
      renderView1.AxesGrid.YLabelFontFile = ''
      renderView1.AxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
      renderView1.AxesGrid.ZLabelFontFile = ''

      # register the view with coprocessor
      # and provide it with information such as the filename to use,
      # how frequently to write the images, etc.
      coprocessor.RegisterView(renderView1,
          filename='image_0_%t.png', freq=1, fittoscreen=0, magnification=1, width=1505, height=709, cinema={})
      renderView1.ViewTime = datadescription.GetTime()

      # Create a new 'Render View'
      renderView2 = CreateView('RenderView')
      renderView2.ViewSize = [748, 709]
      renderView2.AnnotationColor = [0.0, 0.0, 0.0]
      renderView2.AxesGrid = 'GridAxes3DActor'
      renderView2.OrientationAxesVisibility = 0
      renderView2.OrientationAxesLabelColor = [0.0, 0.0, 0.0]
      renderView2.OrientationAxesOutlineColor = [0.0, 0.0, 0.0]
      renderView2.CenterOfRotation = [31.5, 31.5, 0.0]
      renderView2.StereoType = 0
      renderView2.CameraPosition = [41.77762163404877, 32.540771811042916, 172.11920087683927]
      renderView2.CameraFocalPoint = [41.77762163404877, 32.540771811042916, 0.0]
      renderView2.CameraParallelScale = 44.54772721475249
      renderView2.Background = [1.0, 1.0, 1.0]

      # init the 'GridAxes3DActor' selected for 'AxesGrid'
      renderView2.AxesGrid.XTitleColor = [0.0, 0.0, 0.0]
      renderView2.AxesGrid.XTitleFontFile = ''
      renderView2.AxesGrid.YTitleColor = [0.0, 0.0, 0.0]
      renderView2.AxesGrid.YTitleFontFile = ''
      renderView2.AxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
      renderView2.AxesGrid.ZTitleFontFile = ''
      renderView2.AxesGrid.GridColor = [0.0, 0.0, 0.0]
      renderView2.AxesGrid.XLabelColor = [0.0, 0.0, 0.0]
      renderView2.AxesGrid.XLabelFontFile = ''
      renderView2.AxesGrid.YLabelColor = [0.0, 0.0, 0.0]
      renderView2.AxesGrid.YLabelFontFile = ''
      renderView2.AxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
      renderView2.AxesGrid.ZLabelFontFile = ''

      # register the view with coprocessor
      # and provide it with information such as the filename to use,
      # how frequently to write the images, etc.
      coprocessor.RegisterView(renderView2,
          filename='image_1_%t.png', freq=1, fittoscreen=0, magnification=1, width=748, height=709, cinema={})
      renderView2.ViewTime = datadescription.GetTime()

      # ----------------------------------------------------------------
      # restore active view
      SetActiveView(renderView2)
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

      # get color transfer function/color map for 'rho'
      rhoLUT = GetColorTransferFunction('rho')
      rhoLUT.RGBPoints = [0.868352553707457, 0.231373, 0.298039, 0.752941, 1.5854047828808844, 0.865003, 0.865003, 0.865003, 2.3024570120543117, 0.705882, 0.0156863, 0.14902]
      rhoLUT.ScalarRangeInitialized = 1.0

      # get opacity transfer function/opacity map for 'rho'
      rhoPWF = GetOpacityTransferFunction('rho')
      rhoPWF.Points = [0.868352553707457, 0.0, 0.5, 0.0, 2.3024570120543117, 1.0, 0.5, 0.0]
      rhoPWF.ScalarRangeInitialized = 1

      # trace defaults for the display properties.
      inputDisplay.Representation = 'Slice'
      inputDisplay.AmbientColor = [0.0, 0.0, 0.0]
      inputDisplay.ColorArrayName = ['POINTS', 'rho']
      inputDisplay.LookupTable = rhoLUT
      inputDisplay.OSPRayScaleArray = 'E'
      inputDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
      inputDisplay.SelectOrientationVectors = 'E'
      inputDisplay.ScaleFactor = 6.300000000000001
      inputDisplay.SelectScaleArray = 'E'
      inputDisplay.GlyphType = 'Arrow'
      inputDisplay.GlyphTableIndexArray = 'E'
      inputDisplay.GaussianRadius = 0.315
      inputDisplay.SetScaleArray = ['POINTS', 'E']
      inputDisplay.ScaleTransferFunction = 'PiecewiseFunction'
      inputDisplay.OpacityArray = ['POINTS', 'E']
      inputDisplay.OpacityTransferFunction = 'PiecewiseFunction'
      inputDisplay.DataAxesGrid = 'GridAxesRepresentation'
      inputDisplay.SelectionCellLabelFontFile = ''
      inputDisplay.SelectionPointLabelFontFile = ''
      inputDisplay.PolarAxes = 'PolarAxesRepresentation'
      inputDisplay.ScalarOpacityUnitDistance = 5.627236668865498
      inputDisplay.ScalarOpacityFunction = rhoPWF

      # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
      inputDisplay.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
      inputDisplay.DataAxesGrid.XTitleFontFile = ''
      inputDisplay.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
      inputDisplay.DataAxesGrid.YTitleFontFile = ''
      inputDisplay.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
      inputDisplay.DataAxesGrid.ZTitleFontFile = ''
      inputDisplay.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
      inputDisplay.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
      inputDisplay.DataAxesGrid.XLabelFontFile = ''
      inputDisplay.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
      inputDisplay.DataAxesGrid.YLabelFontFile = ''
      inputDisplay.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
      inputDisplay.DataAxesGrid.ZLabelFontFile = ''

      # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
      inputDisplay.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
      inputDisplay.PolarAxes.PolarAxisTitleFontFile = ''
      inputDisplay.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
      inputDisplay.PolarAxes.PolarAxisLabelFontFile = ''
      inputDisplay.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
      inputDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
      inputDisplay.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
      inputDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''

      # setup the color legend parameters for each legend in this view

      # get color legend/bar for rhoLUT in view renderView1
      rhoLUTColorBar = GetScalarBar(rhoLUT, renderView1)
      rhoLUTColorBar.WindowLocation = 'AnyLocation'
      rhoLUTColorBar.Position = [0.8460427807486638, 0.09308885754583959]
      rhoLUTColorBar.Title = 'rho'
      rhoLUTColorBar.ComponentTitle = ''
      rhoLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
      rhoLUTColorBar.TitleFontFile = ''
      rhoLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
      rhoLUTColorBar.LabelFontFile = ''
      rhoLUTColorBar.ScalarBarLength = 0.3299999999999996

      # set color bar visibility
      rhoLUTColorBar.Visibility = 1

      # show color legend
      inputDisplay.SetScalarBarVisibility(renderView1, True)

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView2'
      # ----------------------------------------------------------------

      # show data from input
      inputDisplay_1 = Show(input, renderView2)

      # get color transfer function/color map for 'E'
      eLUT = GetColorTransferFunction('E')
      eLUT.RGBPoints = [4.770884151343821, 0.231373, 0.298039, 0.752941, 6.368454258441024, 0.865003, 0.865003, 0.865003, 7.966024365538227, 0.705882, 0.0156863, 0.14902]
      eLUT.ScalarRangeInitialized = 1.0

      # get opacity transfer function/opacity map for 'E'
      ePWF = GetOpacityTransferFunction('E')
      ePWF.Points = [4.770884151343821, 0.0, 0.5, 0.0, 7.966024365538227, 1.0, 0.5, 0.0]
      ePWF.ScalarRangeInitialized = 1

      # trace defaults for the display properties.
      inputDisplay_1.Representation = 'Slice'
      inputDisplay_1.AmbientColor = [0.0, 0.0, 0.0]
      inputDisplay_1.ColorArrayName = ['POINTS', 'E']
      inputDisplay_1.LookupTable = eLUT
      inputDisplay_1.OSPRayScaleArray = 'E'
      inputDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
      inputDisplay_1.SelectOrientationVectors = 'E'
      inputDisplay_1.ScaleFactor = 6.300000000000001
      inputDisplay_1.SelectScaleArray = 'E'
      inputDisplay_1.GlyphType = 'Arrow'
      inputDisplay_1.GlyphTableIndexArray = 'E'
      inputDisplay_1.GaussianRadius = 0.315
      inputDisplay_1.SetScaleArray = ['POINTS', 'E']
      inputDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
      inputDisplay_1.OpacityArray = ['POINTS', 'E']
      inputDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
      inputDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
      inputDisplay_1.SelectionCellLabelFontFile = ''
      inputDisplay_1.SelectionPointLabelFontFile = ''
      inputDisplay_1.PolarAxes = 'PolarAxesRepresentation'
      inputDisplay_1.ScalarOpacityUnitDistance = 5.627236668865498
      inputDisplay_1.ScalarOpacityFunction = ePWF

      # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
      inputDisplay_1.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
      inputDisplay_1.DataAxesGrid.XTitleFontFile = ''
      inputDisplay_1.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
      inputDisplay_1.DataAxesGrid.YTitleFontFile = ''
      inputDisplay_1.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
      inputDisplay_1.DataAxesGrid.ZTitleFontFile = ''
      inputDisplay_1.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
      inputDisplay_1.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
      inputDisplay_1.DataAxesGrid.XLabelFontFile = ''
      inputDisplay_1.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
      inputDisplay_1.DataAxesGrid.YLabelFontFile = ''
      inputDisplay_1.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
      inputDisplay_1.DataAxesGrid.ZLabelFontFile = ''

      # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
      inputDisplay_1.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
      inputDisplay_1.PolarAxes.PolarAxisTitleFontFile = ''
      inputDisplay_1.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
      inputDisplay_1.PolarAxes.PolarAxisLabelFontFile = ''
      inputDisplay_1.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
      inputDisplay_1.PolarAxes.LastRadialAxisTextFontFile = ''
      inputDisplay_1.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
      inputDisplay_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

      # setup the color legend parameters for each legend in this view

      # get color legend/bar for eLUT in view renderView2
      eLUTColorBar = GetScalarBar(eLUT, renderView2)
      eLUTColorBar.WindowLocation = 'AnyLocation'
      eLUTColorBar.Position = [0.7806500612930161, 0.14809590973201694]
      eLUTColorBar.Title = 'E'
      eLUTColorBar.ComponentTitle = ''
      eLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
      eLUTColorBar.TitleFontFile = ''
      eLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
      eLUTColorBar.LabelFontFile = ''
      eLUTColorBar.ScalarBarLength = 0.33000000000000007

      # set color bar visibility
      eLUTColorBar.Visibility = 1

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
    arrays = [['E', 0], ['mx', 0], ['my', 0], ['rho', 0]]
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
