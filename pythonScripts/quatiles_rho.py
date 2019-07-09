
#--------------------------------------------------------------

# Global timestep output options
timeStepToStartOutputAt=0
forceOutputAtFirstCall=False

# Global screenshot output options
imageFileNamePadding=0
rescale_lookuptable=True

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

      # Create a new 'Box Chart View'
      boxChartView1 = CreateView('BoxChartView')
      boxChartView1.ViewSize = [1462, 497]
      boxChartView1.ChartTitleFontFile = ''

      # register the view with coprocessor
      # and provide it with information such as the filename to use,
      # how frequently to write the images, etc.
      coprocessor.RegisterView(boxChartView1,
          filename='rho_1_%t.png', freq=1, fittoscreen=1, magnification=1, width=1462, height=497, cinema={})
      boxChartView1.ViewTime = datadescription.GetTime()

      # Create a new 'Render View'
      renderView1 = CreateView('RenderView')
      renderView1.ViewSize = [1462, 779]
      renderView1.InteractionMode = '2D'
      renderView1.AxesGrid = 'GridAxes3DActor'
      renderView1.CenterOfRotation = [63.5, 63.5, 0.0]
      renderView1.StereoType = 0
      renderView1.CameraPosition = [63.5, 63.5, 10000.0]
      renderView1.CameraFocalPoint = [63.5, 63.5, 0.0]
      renderView1.CameraParallelScale = 89.80256121069154
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
          filename='quartiles_0_%t.png', freq=1, fittoscreen=0, magnification=1, width=1462, height=779, cinema={})
      renderView1.ViewTime = datadescription.GetTime()

      # ----------------------------------------------------------------
      # restore active view
      SetActiveView(boxChartView1)
      # ----------------------------------------------------------------

      # ----------------------------------------------------------------
      # setup the data processing pipelines
      # ----------------------------------------------------------------

      # create a new 'XML Partitioned Image Data Reader'
      # create a producer from a simulation input
      input = coprocessor.CreateProducer(datadescription, 'input')

      # create a new 'Compute Quartiles'
      computeQuartiles1 = ComputeQuartiles(Input=input)

      # ----------------------------------------------------------------
      # setup the visualization in view 'boxChartView1'
      # ----------------------------------------------------------------

      # show data from computeQuartiles1
      computeQuartiles1Display = Show(computeQuartiles1, boxChartView1)

      # trace defaults for the display properties.
      computeQuartiles1Display.CompositeDataSetIndex = 0
      computeQuartiles1Display.FieldAssociation = 'Row Data'
      computeQuartiles1Display.SeriesVisibility = ['TimeValue', 'E', 'mx', 'my', 'rho']
      computeQuartiles1Display.SeriesColor = ['TimeValue', '0', '0', '0', 'E', '0.889998', '0.100008', '0.110002', 'mx', '0.220005', '0.489998', '0.719997', 'my', '0.300008', '0.689998', '0.289998', 'rho', '0.6', '0.310002', '0.639994']

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView1'
      # ----------------------------------------------------------------

      # show data from input
      inputDisplay = Show(input, renderView1)

      # get color transfer function/color map for 'rho'
      rhoLUT = GetColorTransferFunction('rho')
      rhoLUT.RGBPoints = [0.8517897933891525, 0.231373, 0.298039, 0.752941, 1.5749223079001742, 0.865003, 0.865003, 0.865003, 2.298054822411196, 0.705882, 0.0156863, 0.14902]
      rhoLUT.ScalarRangeInitialized = 1.0

      # get opacity transfer function/opacity map for 'rho'
      rhoPWF = GetOpacityTransferFunction('rho')
      rhoPWF.Points = [0.8517897933891525, 0.0, 0.5, 0.0, 2.298054822411196, 1.0, 0.5, 0.0]
      rhoPWF.ScalarRangeInitialized = 1

      # trace defaults for the display properties.
      inputDisplay.Representation = 'Surface'
      inputDisplay.ColorArrayName = ['POINTS', 'rho']
      inputDisplay.LookupTable = rhoLUT
      inputDisplay.OSPRayScaleArray = 'E'
      inputDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
      inputDisplay.SelectOrientationVectors = 'E'
      inputDisplay.ScaleFactor = 12.700000000000001
      inputDisplay.SelectScaleArray = 'E'
      inputDisplay.GlyphType = 'Arrow'
      inputDisplay.GlyphTableIndexArray = 'E'
      inputDisplay.GaussianRadius = 0.635
      inputDisplay.SetScaleArray = ['POINTS', 'E']
      inputDisplay.ScaleTransferFunction = 'PiecewiseFunction'
      inputDisplay.OpacityArray = ['POINTS', 'E']
      inputDisplay.OpacityTransferFunction = 'PiecewiseFunction'
      inputDisplay.DataAxesGrid = 'GridAxesRepresentation'
      inputDisplay.SelectionCellLabelFontFile = ''
      inputDisplay.SelectionPointLabelFontFile = ''
      inputDisplay.PolarAxes = 'PolarAxesRepresentation'
      inputDisplay.ScalarOpacityUnitDistance = 7.108580809929175
      inputDisplay.ScalarOpacityFunction = rhoPWF

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

      # get color legend/bar for rhoLUT in view renderView1
      rhoLUTColorBar = GetScalarBar(rhoLUT, renderView1)
      rhoLUTColorBar.Title = 'rho'
      rhoLUTColorBar.ComponentTitle = ''
      rhoLUTColorBar.TitleFontFile = ''
      rhoLUTColorBar.LabelFontFile = ''

      # set color bar visibility
      rhoLUTColorBar.Visibility = 1

      # show color legend
      inputDisplay.SetScalarBarVisibility(renderView1, True)

      # ----------------------------------------------------------------
      # setup color maps and opacity mapes used in the visualization
      # note: the Get..() functions create a new object, if needed
      # ----------------------------------------------------------------

      # ----------------------------------------------------------------
      # finally, restore active source
      SetActiveSource(computeQuartiles1)
      # ----------------------------------------------------------------
    return Pipeline()

  class CoProcessor(coprocessing.CoProcessor):
    def CreatePipeline(self, datadescription):
      self.Pipeline = _CreatePipeline(self, datadescription)

  coprocessor = CoProcessor()
  # these are the frequencies at which the coprocessor updates.
  freqs = {'input': [1, 1, 1]}
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
