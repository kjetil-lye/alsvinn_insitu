
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

from paraview.simple import *
from paraview import coprocessing
outputfrequency= 1


        # =================================OUTPUT DEFINITIONS================================
def getFields():
    return [['E_mean', 0], ['E_var', 0], ['mx_mean', 0], ['mx_var', 0], ['my_mean', 0], ['my_var', 0], ['mz_mean', 0], ['mz_var', 0], ['rho_mean', 0], ['rho_var', 0]]

def getImageSize(nx,nz,ny):
    hdw = 1920
    hdh = 1080
    d = 2 #never 1d
    if(not(nx ==1 or ny ==1 or nz ==1)):
        d=3
    w = min(hdw, (d-1)*max(nx,ny,nz))
    h = min(hdh, (d-1)*max(nx,ny,nz))
    return w,h

def getRGBPoints(vname):
    #same order as getFields()
  tablergb = {}
  tablergb['E_mean']=[6.384373773961045, 0.231373, 0.298039, 0.752941, 6.397468058702769, 0.865003, 0.865003, 0.865003, 6.410562343444494, 0.705882, 0.0156863, 0.14902]
  tablergb['rho_var'] = [7.327471962526033e-15, 0.231373, 0.298039, 0.752941, 0.05300996129263258, 0.865003, 0.865003, 0.865003, 0.10601992258525783, 0.705882, 0.0156863, 0.14902]
  tablergb['E_var'] = [3.126388037344441e-13, 0.231373, 0.298039, 0.752941, 1.183453138509094e-05, 0.865003, 0.865003, 0.865003, 2.3669062457543077e-05, 0.705882, 0.0156863, 0.14902]
  tablergb['mx_mean']=[0.1966843694485616, 0.231373, 0.298039, 0.752941, 0.27797292425157505, 0.865003, 0.865003, 0.865003, 0.35926147905458855, 0.705882, 0.0156863, 0.14902]

  tablergb['mx_var']=[1.8304802118507268e-13, 0.231373, 0.298039, 0.752941, 0.0018752632407424905, 0.865003, 0.865003, 0.865003, 0.003750526481301933, 0.705882, 0.0156863, 0.14902]

  tablergb['my_mean']=[-0.0005318617114623177, 0.231373, 0.298039, 0.752941, -2.9579154056703005e-05, 0.865003, 0.865003, 0.865003, 0.00047270340334891166, 0.705882, 0.0156863, 0.14902]

  tablergb['my_var']=[3.792124236755382e-15, 0.231373, 0.298039, 0.752941, 9.817798570548125e-08, 0.865003, 0.865003, 0.865003, 1.9635596761883828e-07, 0.705882, 0.0156863, 0.14902]

  tablergb['mz_mean']=[-0.0003734129861518945, 0.231373, 0.298039, 0.752941, 5.109169672523427e-05, 0.865003, 0.865003, 0.865003, 0.00047559637960236306, 0.705882, 0.0156863, 0.14902]

  tablergb['mz_var']=[5.744363760126085e-16, 0.231373, 0.298039, 0.752941, 6.663907762671332e-08, 0.865003, 0.865003, 0.865003, 1.3327815467899028e-07, 0.705882, 0.0156863, 0.14902]

  tablergb['rho_mean']=[1.0016140251131045, 0.231373, 0.298039, 0.752941, 1.4894833747421563, 0.865003, 0.865003, 0.865003, 1.9773527243712083, 0.705882, 0.0156863, 0.14902]

  return tablergb[vname]



def getPWFPoints(vname):
    tablepwf = {}
    tablepwf['E_mean'] =[6.384373773961045, 0.0, 0.5, 0.0, 6.410562343444494, 1.0, 0.5, 0.0]
    tablepwf['rho_var']=[7.327471962526033e-15, 0.0, 0.5, 0.0, 0.10601992258525783, 1.0, 0.5, 0.0]
    tablepwf['E_var']=[3.126388037344441e-13, 0.0, 0.5, 0.0, 2.3669062457543077e-05, 1.0, 0.5, 0.0]

    tablepwf['mx_mean']=[0.1966843694485616, 0.0, 0.5, 0.0, 0.35926147905458855, 1.0, 0.5, 0.0]

    tablepwf['mx_var']=[1.8304802118507268e-13, 0.0, 0.5, 0.0, 0.003750526481301933, 1.0, 0.5, 0.0]

    tablepwf['my_mean']=[-0.0005318617114623177, 0.0, 0.5, 0.0, 0.00047270340334891166, 1.0, 0.5, 0.0]

    tablepwf['my_var']=[3.792124236755382e-15, 0.0, 0.5, 0.0, 1.9635596761883828e-07, 1.0, 0.5, 0.0]

    tablepwf['mz_mean']=[-0.0003734129861518945, 0.0, 0.5, 0.0, 0.00047559637960236306, 1.0, 0.5, 0.0]

    tablepwf['mz_var']=[5.744363760126085e-16, 0.0, 0.5, 0.0, 1.3327815467899028e-07, 1.0, 0.5, 0.0]

    tablepwf['rho_mean']=[1.0016140251131045, 0.0, 0.5, 0.0, 1.9773527243712083, 1.0, 0.5, 0.0]

    return tablepwf[vname]


def getThresholdRange(vname):
    tablepwf = {}
    tablepwf['E_mean'] = [5.75, 1000]
    tablepwf['rho_var']= [0.9512946706386292, 1000]
    tablepwf['E_var']= [5.12946706386292, 1000]

    tablepwf['mx_mean']=[-100, 0]

    tablepwf['mx_var']=[0, 100 ]

    tablepwf['my_mean']=[-100, 0.0]

    tablepwf['my_var']=[0, 100 ]

    tablepwf['mz_mean']=[-100, 0.0]

    tablepwf['mz_var']=[0, 100 ]

    tablepwf['rho_mean']=[1.1, 1000]

    return tablepwf[vname]


        # =================================OUTPUT DEFINITIONS================================
    # =================================OUTPUT DEFINITIONS================================

# ----------------------- CoProcessor definition -----------------------
def CreateCoProcessor():
  def _CreatePipeline(coprocessor, datadescription):
    class Pipeline:


      # To ensure correct image size when batc h processing, please search
      # for and uncomment the line `# renderView*.ViewSize = [*,*]`
      fields = getFields()
      LUT = []
      PWF = []

      for ifield in range(0,len(fields)):
          input = coprocessor.CreateProducer(datadescription, 'input')

        #  grid = input.GetClientSideObject().GetOutputDataObject(0)
          fieldname =  fields[ifield][0]

         # pixelw,pixelh = getImageSize(64,64,64)
          pixelw,pixelh = 1920,1080
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
          renderView1.Background =[0., 0., 0.] #[0.32, 0.34, 0.43]

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

        #  mergeBlocks1 = MergeBlocks(Input=input)

          input = coprocessor.CreateProducer(datadescription, 'input')
          isoVolume1 = IsoVolume(Input=input)
          isoVolume1.InputScalars = ['POINTS', fieldname]
          isoVolume1.ThresholdRange = getThresholdRange(fieldname)

          # show data from input
          inputDisplay =  Show(isoVolume1, renderView1)


            # rescale color and/or opacity maps used to include current data range
    #      inputDisplay.RescaleTransferFunctionToDataRange(True, True)

          # get color transfer function/color map for 'fieldname'
          # get opacity transfer function/opacity map for 'fieldname'
          if(len(LUT)< len(fields)):
              LUT.append( GetColorTransferFunction(fieldname ))
              PWF.append(GetOpacityTransferFunction(fieldname))


          LUT[ifield].RGBPoints = getRGBPoints(fieldname)
    #      LUT[ifield].Discretize = 1
          LUT[ifield].ScalarRangeInitialized = 1.0

          PWF[ifield].Points = getPWFPoints(fieldname)
          PWF[ifield].ScalarRangeInitialized = 1



          # trace defaults for the display properties.
          inputDisplay.Representation = 'Surface'
          inputDisplay.ColorArrayName = ['POINTS', fieldname]
          inputDisplay.SetScaleArray = ['POINTS', fieldname]
          inputDisplay.ScaleTransferFunction = 'PiecewiseFunction'
          inputDisplay.LookupTable = LUT[ifield]
          inputDisplay.OSPRayScaleArray = fieldname
          inputDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
          inputDisplay.SelectOrientationVectors = 'None'
          inputDisplay.ScaleFactor = 1.5
          inputDisplay.SelectScaleArray = 'None'
          inputDisplay.GlyphType = 'Arrow'
          inputDisplay.GlyphTableIndexArray = 'None'
          inputDisplay.GaussianRadius = 0.075
          inputDisplay.SetScaleArray = ['POINTS', fieldname]
          inputDisplay.ScaleTransferFunction = 'PiecewiseFunction'
          inputDisplay.OpacityArray = ['POINTS', fieldname]
          inputDisplay.OpacityTransferFunction = 'PiecewiseFunction'
          inputDisplay.DataAxesGrid = 'GridAxesRepresentation'
          inputDisplay.SelectionCellLabelFontFile = ''
          inputDisplay.SelectionPointLabelFontFile = ''
          inputDisplay.PolarAxes = 'PolarAxesRepresentation'
    #      inputDisplay.ScalarOpacityFunction =  PWF[ifield]


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
          LUTColorBar = GetScalarBar(LUT[ifield], renderView1)
          LUTColorBar.Title = fieldname
          LUTColorBar.ComponentTitle = ''
          LUTColorBar.TitleFontFile = ''
          LUTColorBar.LabelFontFile = ''

          # set color bar visibility
          LUTColorBar.Visibility = 1

          # show color legend
          inputDisplay.SetScalarBarVisibility(renderView1, True)


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
  freqs = {'input': [1]}
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
