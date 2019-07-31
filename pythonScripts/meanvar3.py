
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
      renderView1.ViewSize = [692, 596]
      renderView1.InteractionMode = '2D'
      renderView1.AxesGrid = 'GridAxes3DActor'
      renderView1.OrientationAxesVisibility = 0
      renderView1.CenterOfRotation = [63.5, 63.5, 0.0]
      renderView1.StereoType = 0
      renderView1.CameraPosition = [75.94404515097014, 63.49999999999997, 349.655156264848]
      renderView1.CameraFocalPoint = [75.94404515097014, 63.49999999999997, 0.0]
      renderView1.CameraParallelScale = 74.79125095838069
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
          filename='RenderView1_%t.png', freq=1, fittoscreen=1, magnification=1, width=692, height=596, cinema={})
      renderView1.ViewTime = datadescription.GetTime()

      # Create a new 'Render View'
      renderView2 = CreateView('RenderView')
      renderView2.ViewSize = [691, 279]
      renderView2.AxesGrid = 'GridAxes3DActor'
      renderView2.CenterOfRotation = [63.5, 63.5, 5.083514004945755]
      renderView2.StereoType = 0
      renderView2.CameraPosition = [243.68713807449976, 142.41025406574283, 61.97881239544147]
      renderView2.CameraFocalPoint = [-9.037421514835192, 31.733324408299822, -17.82066376082438]
      renderView2.CameraViewUp = [-0.2643491774274177, -0.08878479730598385, 0.9603315948987532]
      renderView2.CameraParallelScale = 89.94446985486847
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
          filename='RenderView1_%t.png', freq=1, fittoscreen=1, magnification=1, width=691, height=279, cinema={})
      renderView2.ViewTime = datadescription.GetTime()

      # Create a new 'Render View'
      renderView3 = CreateView('RenderView')
      renderView3.ViewSize = [691, 279]
      renderView3.AxesGrid = 'GridAxes3DActor'
      renderView3.CenterOfRotation = [63.5, 63.5, 0.0]
      renderView3.StereoType = 0
      renderView3.CameraPosition = [204.55559679097502, 133.91912718185026, 36.66755045070944]
      renderView3.CameraFocalPoint = [63.50000000000001, 63.50000000000001, -2.674783325039423e-14]
      renderView3.CameraViewUp = [-0.24600576829028553, -0.011893507898991228, 0.9691953912590398]
      renderView3.CameraParallelScale = 89.80256121069154
      renderView3.Background = [0.32, 0.34, 0.43]

      # init the 'GridAxes3DActor' selected for 'AxesGrid'
      renderView3.AxesGrid.XTitleFontFile = ''
      renderView3.AxesGrid.YTitleFontFile = ''
      renderView3.AxesGrid.ZTitleFontFile = ''
      renderView3.AxesGrid.XLabelFontFile = ''
      renderView3.AxesGrid.YLabelFontFile = ''
      renderView3.AxesGrid.ZLabelFontFile = ''

      # register the view with coprocessor
      # and provide it with information such as the filename to use,
      # how frequently to write the images, etc.
      coprocessor.RegisterView(renderView3,
          filename='RenderView1_%t.png', freq=1, fittoscreen=1, magnification=1, width=691, height=279, cinema={})
      renderView3.ViewTime = datadescription.GetTime()

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

      # create a new 'Warp By Scalar'
      warpByScalar1 = WarpByScalar(Input=input)
      warpByScalar1.Scalars = ['POINTS', 'rho_var']
      warpByScalar1.ScaleFactor = 50.0

      # create a new 'Warp By Scalar'
      warpByScalar2 = WarpByScalar(Input=warpByScalar1)
      warpByScalar2.Scalars = ['POINTS', 'rho_var']

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView1'
      # ----------------------------------------------------------------

      # show data from input
      inputDisplay = Show(input, renderView1)

      # get color transfer function/color map for 'rho_mean'
      rho_meanLUT = GetColorTransferFunction('rho_mean')
      rho_meanLUT.RGBPoints = [0.962638512048598, 0.231373, 0.298039, 0.752941, 1.5236999546328764, 0.865003, 0.865003, 0.865003, 2.084761397217155, 0.705882, 0.0156863, 0.14902]
      rho_meanLUT.ScalarRangeInitialized = 1.0

      # get opacity transfer function/opacity map for 'rho_mean'
      rho_meanPWF = GetOpacityTransferFunction('rho_mean')
      rho_meanPWF.Points = [0.962638512048598, 0.0, 0.5, 0.0, 2.084761397217155, 1.0, 0.5, 0.0]
      rho_meanPWF.ScalarRangeInitialized = 1

      # trace defaults for the display properties.
      inputDisplay.Representation = 'Surface'
      inputDisplay.ColorArrayName = ['POINTS', 'rho_mean']
      inputDisplay.LookupTable = rho_meanLUT
      inputDisplay.OSPRayScaleArray = 'rho_mean'
      inputDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
      inputDisplay.SelectOrientationVectors = 'None'
      inputDisplay.ScaleFactor = 12.700000000000001
      inputDisplay.SelectScaleArray = 'None'
      inputDisplay.GlyphType = 'Arrow'
      inputDisplay.GlyphTableIndexArray = 'None'
      inputDisplay.GaussianRadius = 0.635
      inputDisplay.SetScaleArray = ['POINTS', 'rho_mean']
      inputDisplay.ScaleTransferFunction = 'PiecewiseFunction'
      inputDisplay.OpacityArray = ['POINTS', 'rho_mean']
      inputDisplay.OpacityTransferFunction = 'PiecewiseFunction'
      inputDisplay.DataAxesGrid = 'GridAxesRepresentation'
      inputDisplay.SelectionCellLabelFontFile = ''
      inputDisplay.SelectionPointLabelFontFile = ''
      inputDisplay.PolarAxes = 'PolarAxesRepresentation'
      inputDisplay.ScalarOpacityUnitDistance = 7.108580809929175
      inputDisplay.ScalarOpacityFunction = rho_meanPWF

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

      # show data from warpByScalar1
      warpByScalar1Display = Show(warpByScalar1, renderView1)

      # trace defaults for the display properties.
      warpByScalar1Display.Representation = 'Surface'
      warpByScalar1Display.ColorArrayName = ['POINTS', 'rho_mean']
      warpByScalar1Display.LookupTable = rho_meanLUT
      warpByScalar1Display.OSPRayScaleArray = 'rho_mean'
      warpByScalar1Display.OSPRayScaleFunction = 'PiecewiseFunction'
      warpByScalar1Display.SelectOrientationVectors = 'None'
      warpByScalar1Display.ScaleFactor = 12.700000000000001
      warpByScalar1Display.SelectScaleArray = 'None'
      warpByScalar1Display.GlyphType = 'Arrow'
      warpByScalar1Display.GlyphTableIndexArray = 'None'
      warpByScalar1Display.GaussianRadius = 0.5842
      warpByScalar1Display.ShaderPreset = 'Plain circle'
      warpByScalar1Display.SetScaleArray = ['POINTS', 'rho_mean']
      warpByScalar1Display.ScaleTransferFunction = 'PiecewiseFunction'
      warpByScalar1Display.OpacityArray = ['POINTS', 'rho_mean']
      warpByScalar1Display.OpacityTransferFunction = 'PiecewiseFunction'
      warpByScalar1Display.DataAxesGrid = 'GridAxesRepresentation'
      warpByScalar1Display.SelectionCellLabelFontFile = ''
      warpByScalar1Display.SelectionPointLabelFontFile = ''
      warpByScalar1Display.PolarAxes = 'PolarAxesRepresentation'
      warpByScalar1Display.ScalarOpacityFunction = rho_meanPWF
      warpByScalar1Display.ScalarOpacityUnitDistance = 7.10871954685655

      # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
      warpByScalar1Display.DataAxesGrid.XTitleFontFile = ''
      warpByScalar1Display.DataAxesGrid.YTitleFontFile = ''
      warpByScalar1Display.DataAxesGrid.ZTitleFontFile = ''
      warpByScalar1Display.DataAxesGrid.XLabelFontFile = ''
      warpByScalar1Display.DataAxesGrid.YLabelFontFile = ''
      warpByScalar1Display.DataAxesGrid.ZLabelFontFile = ''

      # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
      warpByScalar1Display.PolarAxes.PolarAxisTitleFontFile = ''
      warpByScalar1Display.PolarAxes.PolarAxisLabelFontFile = ''
      warpByScalar1Display.PolarAxes.LastRadialAxisTextFontFile = ''
      warpByScalar1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

      # show data from warpByScalar2
      warpByScalar2Display = Show(warpByScalar2, renderView1)

      # trace defaults for the display properties.
      warpByScalar2Display.Representation = 'Surface'
      warpByScalar2Display.ColorArrayName = ['POINTS', 'rho_mean']
      warpByScalar2Display.LookupTable = rho_meanLUT
      warpByScalar2Display.OSPRayScaleArray = 'rho_mean'
      warpByScalar2Display.OSPRayScaleFunction = 'PiecewiseFunction'
      warpByScalar2Display.SelectOrientationVectors = 'None'
      warpByScalar2Display.ScaleFactor = 12.700000000000001
      warpByScalar2Display.SelectScaleArray = 'None'
      warpByScalar2Display.GlyphType = 'Arrow'
      warpByScalar2Display.GlyphTableIndexArray = 'None'
      warpByScalar2Display.GaussianRadius = 0.635
      warpByScalar2Display.SetScaleArray = ['POINTS', 'rho_mean']
      warpByScalar2Display.ScaleTransferFunction = 'PiecewiseFunction'
      warpByScalar2Display.OpacityArray = ['POINTS', 'rho_mean']
      warpByScalar2Display.OpacityTransferFunction = 'PiecewiseFunction'
      warpByScalar2Display.DataAxesGrid = 'GridAxesRepresentation'
      warpByScalar2Display.SelectionCellLabelFontFile = ''
      warpByScalar2Display.SelectionPointLabelFontFile = ''
      warpByScalar2Display.PolarAxes = 'PolarAxesRepresentation'
      warpByScalar2Display.ScalarOpacityFunction = rho_meanPWF
      warpByScalar2Display.ScalarOpacityUnitDistance = 7.121039869516009

      # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
      warpByScalar2Display.DataAxesGrid.XTitleFontFile = ''
      warpByScalar2Display.DataAxesGrid.YTitleFontFile = ''
      warpByScalar2Display.DataAxesGrid.ZTitleFontFile = ''
      warpByScalar2Display.DataAxesGrid.XLabelFontFile = ''
      warpByScalar2Display.DataAxesGrid.YLabelFontFile = ''
      warpByScalar2Display.DataAxesGrid.ZLabelFontFile = ''

      # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
      warpByScalar2Display.PolarAxes.PolarAxisTitleFontFile = ''
      warpByScalar2Display.PolarAxes.PolarAxisLabelFontFile = ''
      warpByScalar2Display.PolarAxes.LastRadialAxisTextFontFile = ''
      warpByScalar2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

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

      # show color legend
      warpByScalar1Display.SetScalarBarVisibility(renderView1, True)

      # show color legend
      warpByScalar2Display.SetScalarBarVisibility(renderView1, True)

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView2'
      # ----------------------------------------------------------------

      # show data from warpByScalar1
      warpByScalar1Display_1 = Show(warpByScalar1, renderView2)

      # get color transfer function/color map for 'rho_var'
      rho_varLUT = GetColorTransferFunction('rho_var')
      rho_varLUT.RGBPoints = [0.00013907231148335697, 0.231373, 0.298039, 0.752941, 0.11199892413694945, 0.865003, 0.865003, 0.865003, 0.22385877596241555, 0.705882, 0.0156863, 0.14902]
      rho_varLUT.ScalarRangeInitialized = 1.0

      # get opacity transfer function/opacity map for 'rho_var'
      rho_varPWF = GetOpacityTransferFunction('rho_var')
      rho_varPWF.Points = [0.00013907231148335697, 0.0, 0.5, 0.0, 0.22385877596241555, 1.0, 0.5, 0.0]
      rho_varPWF.ScalarRangeInitialized = 1

      # trace defaults for the display properties.
      warpByScalar1Display_1.Representation = 'Surface'
      warpByScalar1Display_1.ColorArrayName = ['POINTS', 'rho_var']
      warpByScalar1Display_1.LookupTable = rho_varLUT
      warpByScalar1Display_1.OSPRayScaleArray = 'rho_mean'
      warpByScalar1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
      warpByScalar1Display_1.SelectOrientationVectors = 'None'
      warpByScalar1Display_1.ScaleFactor = 12.700000000000001
      warpByScalar1Display_1.SelectScaleArray = 'None'
      warpByScalar1Display_1.GlyphType = 'Arrow'
      warpByScalar1Display_1.GlyphTableIndexArray = 'None'
      warpByScalar1Display_1.GaussianRadius = 0.635
      warpByScalar1Display_1.SetScaleArray = ['POINTS', 'rho_mean']
      warpByScalar1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
      warpByScalar1Display_1.OpacityArray = ['POINTS', 'rho_mean']
      warpByScalar1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
      warpByScalar1Display_1.DataAxesGrid = 'GridAxesRepresentation'
      warpByScalar1Display_1.SelectionCellLabelFontFile = ''
      warpByScalar1Display_1.SelectionPointLabelFontFile = ''
      warpByScalar1Display_1.PolarAxes = 'PolarAxesRepresentation'
      warpByScalar1Display_1.ScalarOpacityFunction = rho_varPWF
      warpByScalar1Display_1.ScalarOpacityUnitDistance = 7.119813998060553

      # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
      warpByScalar1Display_1.DataAxesGrid.XTitleFontFile = ''
      warpByScalar1Display_1.DataAxesGrid.YTitleFontFile = ''
      warpByScalar1Display_1.DataAxesGrid.ZTitleFontFile = ''
      warpByScalar1Display_1.DataAxesGrid.XLabelFontFile = ''
      warpByScalar1Display_1.DataAxesGrid.YLabelFontFile = ''
      warpByScalar1Display_1.DataAxesGrid.ZLabelFontFile = ''

      # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
      warpByScalar1Display_1.PolarAxes.PolarAxisTitleFontFile = ''
      warpByScalar1Display_1.PolarAxes.PolarAxisLabelFontFile = ''
      warpByScalar1Display_1.PolarAxes.LastRadialAxisTextFontFile = ''
      warpByScalar1Display_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

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
      warpByScalar1Display_1.SetScalarBarVisibility(renderView2, True)

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView3'
      # ----------------------------------------------------------------

      # show data from warpByScalar2
      warpByScalar2Display_1 = Show(warpByScalar2, renderView3)

      # trace defaults for the display properties.
      warpByScalar2Display_1.Representation = 'Surface'
      warpByScalar2Display_1.ColorArrayName = ['POINTS', 'rho_mean']
      warpByScalar2Display_1.LookupTable = rho_meanLUT
      warpByScalar2Display_1.OSPRayScaleArray = 'rho_mean'
      warpByScalar2Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
      warpByScalar2Display_1.SelectOrientationVectors = 'None'
      warpByScalar2Display_1.ScaleFactor = 12.700000000000001
      warpByScalar2Display_1.SelectScaleArray = 'None'
      warpByScalar2Display_1.GlyphType = 'Arrow'
      warpByScalar2Display_1.GlyphTableIndexArray = 'None'
      warpByScalar2Display_1.GaussianRadius = 0.635
      warpByScalar2Display_1.SetScaleArray = ['POINTS', 'rho_mean']
      warpByScalar2Display_1.ScaleTransferFunction = 'PiecewiseFunction'
      warpByScalar2Display_1.OpacityArray = ['POINTS', 'rho_mean']
      warpByScalar2Display_1.OpacityTransferFunction = 'PiecewiseFunction'
      warpByScalar2Display_1.DataAxesGrid = 'GridAxesRepresentation'
      warpByScalar2Display_1.SelectionCellLabelFontFile = ''
      warpByScalar2Display_1.SelectionPointLabelFontFile = ''
      warpByScalar2Display_1.PolarAxes = 'PolarAxesRepresentation'
      warpByScalar2Display_1.ScalarOpacityFunction = rho_meanPWF
      warpByScalar2Display_1.ScalarOpacityUnitDistance = 7.119813998068832

      # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
      warpByScalar2Display_1.DataAxesGrid.XTitleFontFile = ''
      warpByScalar2Display_1.DataAxesGrid.YTitleFontFile = ''
      warpByScalar2Display_1.DataAxesGrid.ZTitleFontFile = ''
      warpByScalar2Display_1.DataAxesGrid.XLabelFontFile = ''
      warpByScalar2Display_1.DataAxesGrid.YLabelFontFile = ''
      warpByScalar2Display_1.DataAxesGrid.ZLabelFontFile = ''

      # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
      warpByScalar2Display_1.PolarAxes.PolarAxisTitleFontFile = ''
      warpByScalar2Display_1.PolarAxes.PolarAxisLabelFontFile = ''
      warpByScalar2Display_1.PolarAxes.LastRadialAxisTextFontFile = ''
      warpByScalar2Display_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

      # setup the color legend parameters for each legend in this view

      # get color legend/bar for rho_meanLUT in view renderView3
      rho_meanLUTColorBar_1 = GetScalarBar(rho_meanLUT, renderView3)
      rho_meanLUTColorBar_1.Title = 'rho_mean'
      rho_meanLUTColorBar_1.ComponentTitle = ''
      rho_meanLUTColorBar_1.TitleFontFile = ''
      rho_meanLUTColorBar_1.LabelFontFile = ''

      # set color bar visibility
      rho_meanLUTColorBar_1.Visibility = 1

      # show color legend
      warpByScalar2Display_1.SetScalarBarVisibility(renderView3, True)

      # ----------------------------------------------------------------
      # setup color maps and opacity mapes used in the visualization
      # note: the Get..() functions create a new object, if needed
      # ----------------------------------------------------------------

      # ----------------------------------------------------------------
      # finally, restore active source
      SetActiveSource(warpByScalar2)
      # ----------------------------------------------------------------
    return Pipeline()

  class CoProcessor(coprocessing.CoProcessor):
    def CreatePipeline(self, datadescription):
      self.Pipeline = _CreatePipeline(self, datadescription)

  coprocessor = CoProcessor()
  # these are the frequencies at which the coprocessor updates.
  freqs = {'input': [1, 1, 1, 1, 1, 1, 1, 1, 1]}
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
