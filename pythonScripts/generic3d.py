
#--------------------------------------------------------------

# Global timestep output options
timeStepToStartOutputAt=0
forceOutputAtFirstCall=False

# Global screenshot output options
imageFileNamePadding=1
rescale_lookuptable=False

# Whether or not to request specific arrays from the adaptor.
requestSpecificArrays=False

# a root directory under which all Catalyst output goes
rootDirectory=''

# makes a cinema D index table
make_cinema_table=False



from paraview.simple import *
from paraview import coprocessing
outputfrequency= 1


#define outputs here:
def getFields():
    return [['E_mean', 0], ['E_var', 0], ['mx_mean', 0], ['mx_var', 0], ['my_mean', 0], ['my_var', 0], ['mz_mean', 0], ['mz_var', 0], ['rho_mean', 0], ['rho_var', 0]]

def getImageSize(nx,nz,ny):
    hdw = 1600
    hdh = 900
    d = 2 #never 1d
    if(not(nx ==1 or ny ==1 or nz ==1)):
        d=3
    w = min(hdw, (d-1)*max(nx,ny,nz))
    h = min(hdh, (d-1)*max(nx,ny,nz))
    return w,h


# ----------------------- CoProcessor definition -----------------------
def CreateCoProcessor():
  def _CreatePipeline(coprocessor, datadescription):
    class Pipeline:


      # To ensure correct image size when batc h processing, please search
      # for and uncomment the line `# renderView*.ViewSize = [*,*]`
      fields = getFields()
      input = coprocessor.CreateProducer(datadescription, 'input')
      for ifield in range(0,len(fields)):


        #  grid = input.GetClientSideObject().GetOutputDataObject(0)
          fieldname =  fields[ifield][0]
          print(fieldname)

          pixelw,pixelh = getImageSize(64,64,64)

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
              filename=fieldname+'_%t.png', freq=1, fittoscreen=1, magnification=1, width=pixelw, height=pixelh, cinema={})
          renderView1.ViewTime = datadescription.GetTime()


          # ----------------------------------------------------------------
          # restore active view
          SetActiveView(renderView1)
          # ----------------------------------------------------------------


          # show data from input
          inputDisplay = Show(input, renderView1)

          # get color transfer function/color map for 'fieldname'
          LUT = GetColorTransferFunction(fieldname)
          LUT.RGBPoints = [1.0729195309977513e-12, 0.231373, 0.298039, 0.752941, 0.0820329561829567, 0.865003, 0.865003, 0.865003, 0.18127562157276733, 0.705882, 0.0156863, 0.14902]
          LUT.Discretize = 0
          LUT.ScalarRangeInitialized = 1.0

          # get opacity transfer function/opacity map for 'fieldname'
          PWF = GetOpacityTransferFunction(fieldname)
          PWF.Points = [1.0729195309977513e-12, 0.0, 0.5, 0.0, 0.18127562157276733, 1.0, 0.5, 0.0]
          PWF.ScalarRangeInitialized = 1

          # trace defaults for the display properties.
          inputDisplay.Representation = 'Volume'
          inputDisplay.ColorArrayName = ['POINTS', fieldname]
          inputDisplay.LookupTable = LUT
          inputDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
          inputDisplay.ScaleFactor = 1.5
          inputDisplay.GlyphType = 'Arrow'
          inputDisplay.GaussianRadius = 0.075
          inputDisplay.ScaleTransferFunction = 'PiecewiseFunction'
          inputDisplay.OpacityTransferFunction = 'PiecewiseFunction'
          inputDisplay.DataAxesGrid = 'GridAxesRepresentation'
          inputDisplay.SelectionCellLabelFontFile = ''
          inputDisplay.SelectionPointLabelFontFile = ''
          inputDisplay.PolarAxes = 'PolarAxesRepresentation'
          inputDisplay.ScalarOpacityUnitDistance = 1.7320508075688776
          inputDisplay.ScalarOpacityFunction = PWF
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

          # get color legend/bar for LUT in view renderView1
          LUTColorBar = GetScalarBar(LUT, renderView1)
          LUTColorBar.Title = fieldname
          LUTColorBar.ComponentTitle = ''
          LUTColorBar.TitleFontFile = ''
          LUTColorBar.LabelFontFile = ''

          # set color bar visibility
          LUTColorBar.Visibility = 1

          # show color legend
          inputDisplay.SetScalarBarVisibility(renderView1, False)


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
