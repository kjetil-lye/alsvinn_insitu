
#--------------------------------------------------------------

# Global timestep output options
timeStepToStartOutputAt=0
forceOutputAtFirstCall=False

# Global screenshot output options
imageFileNamePadding=2
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
outputfrequency= 1
# ----------------------- CoProcessor definition -----------------------

def getImageSize(nx,nz,ny):
    hdw = 1600
    hdh = 900
    d = 2 #never 1d
    if(not(nx ==1 or ny ==1 or nz ==1)):
        d=3
    w = min(hdw, (d-1)*max(nx,ny,nz))
    h = min(hdh, (d-1)*max(nx,ny,nz))
    return w,h

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


      input = coprocessor.CreateProducer(datadescription, 'input')
      grid = input.GetClientSideObject().GetOutputDataObject(0)
      fieldname = 'rho' #grid.

      pixelw,pixelh = getImageSize(16,16,16)

      #### disable automatic camera reset on 'Show'
      paraview.simple._DisableFirstRenderCameraReset()

      # Create a new 'Render View'
      renderView1 = CreateView('RenderView')
      renderView1.ViewSize = [pixelw, pixelh]
      renderView1.AxesGrid = 'GridAxes3DActor'
      renderView1.CenterOfRotation = [7.5, 7.5, 7.5]
      renderView1.StereoType = 0
      renderView1.CameraPosition = [-60, 6.8, 53.2]
      renderView1.CameraFocalPoint = [7.500000000000001, 7.5000000000000036, 7.499999999999998]
      renderView1.CameraViewUp = [0.06238037400182964, 0.9924092871535368, 0.10598346904494559]
      renderView1.CameraParallelScale = 21.461294939791173
      renderView1.Background = [0., 0., 0.]

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
          filename=fieldname+'_mean_%t.png', freq=1, fittoscreen=1, magnification=1, width=pixelw, height=pixelh, cinema={})
      renderView1.ViewTime = datadescription.GetTime()

      # Create a new 'Render View'
      renderView2 = CreateView('RenderView')
      renderView2.ViewSize = [pixelw, pixelh]
      renderView2.AxesGrid = 'GridAxes3DActor'
      renderView2.CenterOfRotation = [7.5, 7.5, 7.5]
      renderView2.StereoType = 0
      renderView2.CameraPosition = [-60, 6.8, 53.2]
      renderView2.CameraFocalPoint = [7.500000000000001, 7.5000000000000036, 7.499999999999998]
      renderView2.CameraViewUp = [0.06238037400182964, 0.9924092871535368, 0.10598346904494559]
      renderView2.CameraParallelScale = 21.461294939791173
      renderView2.Background = [0., 0., 0.]

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
          filename=fieldname+'_var_%t.png', freq=1, fittoscreen=1, magnification=1, width=pixelw, height=pixelh, cinema={})
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

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView1'
      # ----------------------------------------------------------------

      # show data from input
      inputDisplay = Show(input, renderView1)

      # get color transfer function/color map for 'rho_var'
      rho_varLUT = GetColorTransferFunction('rho_var')
      rho_varLUT.RGBPoints = [1.0729195309977513e-12, 0.231373, 0.298039, 0.752941, 0.0820329561829567, 0.865003, 0.865003, 0.865003, 0.18127562157276733, 0.705882, 0.0156863, 0.14902]
      rho_varLUT.Discretize = 0
      rho_varLUT.ScalarRangeInitialized = 1.0

      # get opacity transfer function/opacity map for 'rho_var'
      rho_varPWF = GetOpacityTransferFunction('rho_var')
      rho_varPWF.Points = [1.0729195309977513e-12, 0.0, 0.5, 0.0, 0.18127562157276733, 1.0, 0.5, 0.0]
      rho_varPWF.ScalarRangeInitialized = 1

      # trace defaults for the display properties.
      inputDisplay.Representation = 'Volume'
      inputDisplay.ColorArrayName = ['POINTS', 'rho_var']
      inputDisplay.LookupTable = rho_varLUT
      inputDisplay.OSPRayScaleArray = 'E_mean'
      inputDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
      inputDisplay.SelectOrientationVectors = 'E_mean'
      inputDisplay.ScaleFactor = 1.5
      inputDisplay.SelectScaleArray = 'E_mean'
      inputDisplay.GlyphType = 'Arrow'
      inputDisplay.GlyphTableIndexArray = 'E_mean'
      inputDisplay.GaussianRadius = 0.075
      inputDisplay.SetScaleArray = ['POINTS', 'E_mean']
      inputDisplay.ScaleTransferFunction = 'PiecewiseFunction'
      inputDisplay.OpacityArray = ['POINTS', 'E_mean']
      inputDisplay.OpacityTransferFunction = 'PiecewiseFunction'
      inputDisplay.DataAxesGrid = 'GridAxesRepresentation'
      inputDisplay.SelectionCellLabelFontFile = ''
      inputDisplay.SelectionPointLabelFontFile = ''
      inputDisplay.PolarAxes = 'PolarAxesRepresentation'
      inputDisplay.ScalarOpacityUnitDistance = 1.7320508075688776
      inputDisplay.ScalarOpacityFunction = rho_varPWF
      inputDisplay.Slice = 7

      # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
      inputDisplay.OSPRayScaleFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

      # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
      inputDisplay.ScaleTransferFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

      # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
      inputDisplay.OpacityTransferFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

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

      # get color legend/bar for rho_varLUT in view renderView1
      rho_varLUTColorBar = GetScalarBar(rho_varLUT, renderView1)
      rho_varLUTColorBar.Title = 'rho_var'
      rho_varLUTColorBar.ComponentTitle = ''
      rho_varLUTColorBar.TitleFontFile = ''
      rho_varLUTColorBar.LabelFontFile = ''

      # set color bar visibility
      rho_varLUTColorBar.Visibility = 1

      # show color legend
      inputDisplay.SetScalarBarVisibility(renderView1, False)

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView2'
      # ----------------------------------------------------------------

      # show data from input
      inputDisplay_1 = Show(input, renderView2)

      # get color transfer function/color map for 'rho_mean'
      rho_meanLUT = GetColorTransferFunction('rho_mean')
      rho_meanLUT.RGBPoints = [0.9800109818173648, 0.231373, 0.298039, 0.752941, 1.5202749651501892, 0.865003, 0.865003, 0.865003, 2.060538948483014, 0.705882, 0.0156863, 0.14902]
      rho_meanLUT.Discretize = 0
      rho_meanLUT.ScalarRangeInitialized = 1.0

      # get opacity transfer function/opacity map for 'rho_mean'
      rho_meanPWF = GetOpacityTransferFunction('rho_mean')
      rho_meanPWF.Points = [0.9800109818173648, 0.0, 0.5, 0.0, 2.060538948483014, 1.0, 0.5, 0.0]
      rho_meanPWF.ScalarRangeInitialized = 1

      # trace defaults for the display properties.
      inputDisplay_1.Representation = 'Volume'
      inputDisplay_1.ColorArrayName = ['POINTS', 'rho_mean']
      inputDisplay_1.LookupTable = rho_meanLUT
      inputDisplay_1.OSPRayScaleArray = 'E_mean'
      inputDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
      inputDisplay_1.SelectOrientationVectors = 'E_mean'
      inputDisplay_1.ScaleFactor = 1.5
      inputDisplay_1.SelectScaleArray = 'E_mean'
      inputDisplay_1.GlyphType = 'Arrow'
      inputDisplay_1.GlyphTableIndexArray = 'E_mean'
      inputDisplay_1.GaussianRadius = 0.075
      inputDisplay_1.SetScaleArray = ['POINTS', 'E_mean']
      inputDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
      inputDisplay_1.OpacityArray = ['POINTS', 'E_mean']
      inputDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
      inputDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
      inputDisplay_1.SelectionCellLabelFontFile = ''
      inputDisplay_1.SelectionPointLabelFontFile = ''
      inputDisplay_1.PolarAxes = 'PolarAxesRepresentation'
      inputDisplay_1.ScalarOpacityUnitDistance = 1.7320508075688776
      inputDisplay_1.ScalarOpacityFunction = rho_meanPWF
      inputDisplay_1.Slice = 7

      # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
      inputDisplay_1.OSPRayScaleFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

      # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
      inputDisplay_1.ScaleTransferFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

      # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
      inputDisplay_1.OpacityTransferFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

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

      # get color legend/bar for rho_meanLUT in view renderView2
      rho_meanLUTColorBar = GetScalarBar(rho_meanLUT, renderView2)
      rho_meanLUTColorBar.Title = 'rho_mean'
      rho_meanLUTColorBar.ComponentTitle = ''
      rho_meanLUTColorBar.TitleFontFile = ''
      rho_meanLUTColorBar.LabelFontFile = ''

      # set color bar visibility
      rho_meanLUTColorBar.Visibility = 1

      # show color legend
      inputDisplay_1.SetScalarBarVisibility(renderView2, False)

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
    arrays = [['E_mean', 0], ['E_var', 0], ['mx_mean', 0], ['mx_var', 0], ['my_mean', 0], ['my_var', 0], ['mz_mean', 0], ['mz_var', 0], ['rho_mean', 0], ['rho_var', 0]]
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
