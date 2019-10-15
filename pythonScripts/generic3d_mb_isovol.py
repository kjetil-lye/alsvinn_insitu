
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
  tablergb['E_mean']= [6.175167263107935, 0.231373, 0.298039, 0.752941, 6.3820795895076285, 0.865003, 0.865003, 0.865003, 6.5889919159073225, 0.705882, 0.0156863, 0.14902]
  tablergb['E_var'] =  [0.006406833824861735, 0.231373, 0.298039, 0.752941, 0.10546426461862524, 0.865003, 0.865003, 0.865003, 0.20452169541238874, 0.705882, 0.0156863, 0.14902]

  tablergb['mx_mean']=  [-0.9941379935606395, 0.231373, 0.298039, 0.752941, -0.2405257997968545, 0.865003, 0.865003, 0.865003, 0.5130863939669305, 0.705882, 0.0156863, 0.14902]      
  tablergb['mx_var']=  [0.0002905588124187397, 0.231373, 0.298039, 0.752941, 0.06859629769975875, 0.865003, 0.865003, 0.865003, 0.13690203658709876, 0.705882, 0.0156863, 0.14902]
  
  tablergb['my_mean']=[-0.054708057439109975, 0.231373, 0.298039, 0.752941, -0.0015030679511929962, 0.865003, 0.865003, 0.865003, 0.05170192153672398, 0.705882, 0.0156863, 0.14902]
  tablergb['my_var']=[1.8395258250537413e-05, 0.231373, 0.298039, 0.752941, 0.04095404715759955, 0.865003, 0.865003, 0.865003, 0.08188969905694857, 0.705882, 0.0156863, 0.14902]

  
  tablergb['mz_mean']= [-0.04911304730547963, 0.231373, 0.298039, 0.752941, 0.006872064415233019, 0.865003, 0.865003, 0.865003, 0.06285717613594566, 0.705882, 0.0156863, 0.14902]
  tablergb['mz_var']= [1.699780687823863e-05, 0.231373, 0.298039, 0.752941, 0.04100551305432937, 0.865003, 0.865003, 0.865003, 0.0819940283017805, 0.705882, 0.0156863, 0.14902]
  
  tablergb['rho_mean']= [0.9966069237092963, 0.231373, 0.298039, 0.752941, 1.507953338722982, 0.865003, 0.865003, 0.865003, 2.0192997537366675, 0.705882, 0.0156863, 0.14902]
  tablergb['rho_var'] = [0.0001050731243075198, 0.231373, 0.298039, 0.752941, 0.0889805880393506, 0.865003, 0.865003, 0.865003, 0.1778561029543937, 0.705882, 0.0156863, 0.14902]

  return tablergb[vname]



def getPWFPoints(vname):
    tablepwf = {}
    tablepwf['E_mean'] = [6.175167263107935, 0.0, 0.5, 0.0, 6.5889919159073225, 1.0, 0.5, 0.0]
    tablepwf['E_var']= [0.006406833824861735, 0.0, 0.5, 0.0, 0.20452169541238874, 1.0, 0.5, 0.0]

    tablepwf['mx_mean']= [-0.9941379935606395, 0.0, 0.5, 0.0, 0.5130863939669305, 1.0, 0.5, 0.0]
    tablepwf['mx_var']= [0.0002905588124187397, 0.0, 0.5, 0.0, 0.13690203658709876, 1.0, 0.5, 0.0]

    tablepwf['my_mean']=  [-0.054708057439109975, 0.0, 0.5, 0.0, 0.05170192153672398, 1.0, 0.5, 0.0]
    tablepwf['my_var']= [1.8395258250537413e-05, 0.0, 0.5, 0.0, 0.08188969905694857, 1.0, 0.5, 0.0]
    
    tablepwf['mz_mean'] = [-0.04911304730547963, 0.0, 0.5, 0.0, 0.06285717613594566, 1.0, 0.5, 0.0]
    tablepwf['mz_var']=  [1.699780687823863e-05, 0.0, 0.5, 0.0, 0.0819940283017805, 1.0, 0.5, 0.0]
    
    tablepwf['rho_mean']=[0.9966069237092963, 0.0, 0.5, 0.0, 2.0192997537366675, 1.0, 0.5, 0.0]
    tablepwf['rho_var']= [0.0001050731243075198, 0.0, 0.5, 0.0, 0.1778561029543937, 1.0, 0.5, 0.0]

    return tablepwf[vname]


def getThresholdRange(vname):
    tablepwf = {}

    tablepwf['rho_var']= [0.9512946706386292, 1000]
    tablepwf['rho_mean']=[1.1, 1000]

    tablepwf['E_var']= [0.01, 1000]
    tablepwf['E_mean'] = [5.75, 1000]

    tablepwf['mx_mean']=[-100, 0]
    tablepwf['mx_var']=[0.01, 1000 ]

    tablepwf['my_mean']=[-100, 100.0]
    tablepwf['my_var']=[0.01, 1000 ]

    tablepwf['mz_mean']=[-100,100.0]
    tablepwf['mz_var']=[0.01, 1000 ]

    return tablepwf[vname]

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
