
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
      renderView1.ViewSize = [839, 869]
      renderView1.AxesGrid = 'GridAxes3DActor'
      renderView1.CenterOfRotation = [7.5, 7.5, 7.5]
      renderView1.StereoType = 0
      renderView1.CameraPosition = [45.3155688962638, -10.357901739093238, -23.180648181548435]
      renderView1.CameraFocalPoint = [7.500000000000024, 7.499999999999972, 7.499999999999999]
      renderView1.CameraViewUp = [-0.24823361983428102, 0.6723905085646985, -0.6973313946582901]
      renderView1.CameraParallelScale = 13.454876207783263
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
          filename='RenderView1_%t.png', freq=1, fittoscreen=1, magnification=1, width=839, height=869, cinema={})
      renderView1.ViewTime = datadescription.GetTime()

      # Create a new 'Render View'
      renderView10 = CreateView('RenderView')
      renderView10.ViewSize = [839, 869]
      renderView10.AxesGrid = 'GridAxes3DActor'
      renderView10.CenterOfRotation = [7.5, 7.5, 7.5]
      renderView10.StereoType = 0
      renderView10.CameraPosition = [-36.007811172860855, 8.045542525175595, 35.73113225874897]
      renderView10.CameraFocalPoint = [7.5, 7.5, 7.5]
      renderView10.CameraViewUp = [0.0275762405735752, 0.9993507476470088, 0.023186938849119834]
      renderView10.CameraParallelScale = 13.454876207783263
      renderView10.Background = [0.32, 0.34, 0.43]

      # init the 'GridAxes3DActor' selected for 'AxesGrid'
      renderView10.AxesGrid.XTitleFontFile = ''
      renderView10.AxesGrid.YTitleFontFile = ''
      renderView10.AxesGrid.ZTitleFontFile = ''
      renderView10.AxesGrid.XLabelFontFile = ''
      renderView10.AxesGrid.YLabelFontFile = ''
      renderView10.AxesGrid.ZLabelFontFile = ''

      # register the view with coprocessor
      # and provide it with information such as the filename to use,
      # how frequently to write the images, etc.
      coprocessor.RegisterView(renderView10,
          filename='RenderView1_%t.png', freq=1, fittoscreen=1, magnification=1, width=839, height=869, cinema={})
      renderView10.ViewTime = datadescription.GetTime()

      # Create a new 'Render View'
      renderView2 = CreateView('RenderView')
      renderView2.ViewSize = [839, 869]
      renderView2.AxesGrid = 'GridAxes3DActor'
      renderView2.CenterOfRotation = [7.5, 7.5, 7.5]
      renderView2.StereoType = 0
      renderView2.CameraPosition = [-31.76637953375385, 19.072842989385727, 39.35035041824952]
      renderView2.CameraFocalPoint = [7.500000000000004, 7.500000000000001, 7.499999999999995]
      renderView2.CameraViewUp = [0.1634793151001737, 0.9746725240249027, -0.15260401189124684]
      renderView2.CameraParallelScale = 13.454876207783263
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
          filename='RenderView1_%t.png', freq=1, fittoscreen=1, magnification=1, width=839, height=869, cinema={})
      renderView2.ViewTime = datadescription.GetTime()

      # Create a new 'Render View'
      renderView3 = CreateView('RenderView')
      renderView3.ViewSize = [839, 869]
      renderView3.AxesGrid = 'GridAxes3DActor'
      renderView3.CenterOfRotation = [7.5, 7.5, 7.5]
      renderView3.StereoType = 0
      renderView3.CameraPosition = [-36.04225582585141, 12.933264017721777, 35.154577885422526]
      renderView3.CameraFocalPoint = [7.5, 7.5, 7.5]
      renderView3.CameraViewUp = [0.07369461446524138, 0.9941244711584494, -0.0792820259753303]
      renderView3.CameraParallelScale = 13.454876207783263
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
          filename='RenderView12_%t.png', freq=1, fittoscreen=1, magnification=1, width=839, height=869, cinema={})
      renderView3.ViewTime = datadescription.GetTime()

      # Create a new 'Render View'
      renderView4 = CreateView('RenderView')
      renderView4.ViewSize = [839, 869]
      renderView4.AxesGrid = 'GridAxes3DActor'
      renderView4.CenterOfRotation = [7.5, 7.5, 7.5]
      renderView4.StereoType = 0
      renderView4.CameraPosition = [-31.168248663109452, 11.989958475256673, 41.77580628562185]
      renderView4.CameraFocalPoint = [7.500000000000001, 7.500000000000001, 7.500000000000001]
      renderView4.CameraViewUp = [0.07036796588795895, 0.996210726744453, -0.05111298559153004]
      renderView4.CameraParallelScale = 13.454876207783263
      renderView4.Background = [0.32, 0.34, 0.43]

      # init the 'GridAxes3DActor' selected for 'AxesGrid'
      renderView4.AxesGrid.XTitleFontFile = ''
      renderView4.AxesGrid.YTitleFontFile = ''
      renderView4.AxesGrid.ZTitleFontFile = ''
      renderView4.AxesGrid.XLabelFontFile = ''
      renderView4.AxesGrid.YLabelFontFile = ''
      renderView4.AxesGrid.ZLabelFontFile = ''

      # register the view with coprocessor
      # and provide it with information such as the filename to use,
      # how frequently to write the images, etc.
      coprocessor.RegisterView(renderView4,
          filename='RenderView13_%t.png', freq=1, fittoscreen=1, magnification=1, width=839, height=869, cinema={})
      renderView4.ViewTime = datadescription.GetTime()

      # Create a new 'Render View'
      renderView5 = CreateView('RenderView')
      renderView5.ViewSize = [839, 869]
      renderView5.AxesGrid = 'GridAxes3DActor'
      renderView5.CenterOfRotation = [7.5, 7.5, 7.5]
      renderView5.StereoType = 0
      renderView5.CameraPosition = [34.09207471411244, 9.726914919574376, 51.97613394452246]
      renderView5.CameraFocalPoint = [7.5, 7.5, 7.5]
      renderView5.CameraViewUp = [0.02118277739620224, 0.9978122796150011, -0.06262543086716335]
      renderView5.CameraParallelScale = 13.454876207783263
      renderView5.Background = [0.32, 0.34, 0.43]

      # init the 'GridAxes3DActor' selected for 'AxesGrid'
      renderView5.AxesGrid.XTitleFontFile = ''
      renderView5.AxesGrid.YTitleFontFile = ''
      renderView5.AxesGrid.ZTitleFontFile = ''
      renderView5.AxesGrid.XLabelFontFile = ''
      renderView5.AxesGrid.YLabelFontFile = ''
      renderView5.AxesGrid.ZLabelFontFile = ''

      # register the view with coprocessor
      # and provide it with information such as the filename to use,
      # how frequently to write the images, etc.
      coprocessor.RegisterView(renderView5,
          filename='RenderView14_%t.png', freq=1, fittoscreen=1, magnification=1, width=839, height=869, cinema={})
      renderView5.ViewTime = datadescription.GetTime()

      # Create a new 'Render View'
      renderView6 = CreateView('RenderView')
      renderView6.ViewSize = [839, 869]
      renderView6.AxesGrid = 'GridAxes3DActor'
      renderView6.CenterOfRotation = [7.5, 7.5, 7.5]
      renderView6.StereoType = 0
      renderView6.CameraPosition = [-37.166045415016235, 21.150398195971288, 30.05737339288857]
      renderView6.CameraFocalPoint = [7.4999999999999964, 7.499999999999994, 7.499999999999994]
      renderView6.CameraViewUp = [0.09097810271688046, 0.9215265799673003, -0.37750728104211173]
      renderView6.CameraParallelScale = 13.454876207783263
      renderView6.Background = [0.32, 0.34, 0.43]

      # init the 'GridAxes3DActor' selected for 'AxesGrid'
      renderView6.AxesGrid.XTitleFontFile = ''
      renderView6.AxesGrid.YTitleFontFile = ''
      renderView6.AxesGrid.ZTitleFontFile = ''
      renderView6.AxesGrid.XLabelFontFile = ''
      renderView6.AxesGrid.YLabelFontFile = ''
      renderView6.AxesGrid.ZLabelFontFile = ''

      # register the view with coprocessor
      # and provide it with information such as the filename to use,
      # how frequently to write the images, etc.
      coprocessor.RegisterView(renderView6,
          filename='RenderView15_%t.png', freq=1, fittoscreen=1, magnification=1, width=839, height=869, cinema={})
      renderView6.ViewTime = datadescription.GetTime()

      # Create a new 'Render View'
      renderView7 = CreateView('RenderView')
      renderView7.ViewSize = [839, 869]
      renderView7.AxesGrid = 'GridAxes3DActor'
      renderView7.CenterOfRotation = [7.5, 7.5, 7.5]
      renderView7.StereoType = 0
      renderView7.CameraPosition = [45.80319853317598, 9.390246161650513, 42.42156969392313]
      renderView7.CameraFocalPoint = [7.5, 7.5, 7.5]
      renderView7.CameraViewUp = [0.003045744560930302, 0.9983477889937366, -0.05737957521093411]
      renderView7.CameraParallelScale = 13.454876207783263
      renderView7.Background = [0.32, 0.34, 0.43]

      # init the 'GridAxes3DActor' selected for 'AxesGrid'
      renderView7.AxesGrid.XTitleFontFile = ''
      renderView7.AxesGrid.YTitleFontFile = ''
      renderView7.AxesGrid.ZTitleFontFile = ''
      renderView7.AxesGrid.XLabelFontFile = ''
      renderView7.AxesGrid.YLabelFontFile = ''
      renderView7.AxesGrid.ZLabelFontFile = ''

      # register the view with coprocessor
      # and provide it with information such as the filename to use,
      # how frequently to write the images, etc.
      coprocessor.RegisterView(renderView7,
          filename='RenderView61_%t.png', freq=1, fittoscreen=1, magnification=1, width=839, height=869, cinema={})
      renderView7.ViewTime = datadescription.GetTime()

      # Create a new 'Render View'
      renderView8 = CreateView('RenderView')
      renderView8.ViewSize = [839, 869]
      renderView8.AxesGrid = 'GridAxes3DActor'
      renderView8.CenterOfRotation = [7.5, 7.5, 7.5]
      renderView8.StereoType = 0
      renderView8.CameraPosition = [57.20495960224892, 7.708294337835728, -7.318828655419994]
      renderView8.CameraFocalPoint = [7.500000000000004, 7.499999999999992, 7.499999999999992]
      renderView8.CameraViewUp = [-0.10268587755654802, 0.937941283851751, -0.331242748746249]
      renderView8.CameraParallelScale = 13.454876207783263
      renderView8.Background = [0.32, 0.34, 0.43]

      # init the 'GridAxes3DActor' selected for 'AxesGrid'
      renderView8.AxesGrid.XTitleFontFile = ''
      renderView8.AxesGrid.YTitleFontFile = ''
      renderView8.AxesGrid.ZTitleFontFile = ''
      renderView8.AxesGrid.XLabelFontFile = ''
      renderView8.AxesGrid.YLabelFontFile = ''
      renderView8.AxesGrid.ZLabelFontFile = ''

      # register the view with coprocessor
      # and provide it with information such as the filename to use,
      # how frequently to write the images, etc.
      coprocessor.RegisterView(renderView8,
          filename='RenderView41_%t.png', freq=1, fittoscreen=1, magnification=1, width=839, height=869, cinema={})
      renderView8.ViewTime = datadescription.GetTime()

      # Create a new 'Render View'
      renderView9 = CreateView('RenderView')
      renderView9.ViewSize = [839, 869]
      renderView9.AxesGrid = 'GridAxes3DActor'
      renderView9.CenterOfRotation = [7.5, 7.5, 7.5]
      renderView9.StereoType = 0
      renderView9.CameraPosition = [-38.81925986721616, 9.572779761650851, 30.74766284433884]
      renderView9.CameraFocalPoint = [7.500000000000011, 7.500000000000001, 7.500000000000014]
      renderView9.CameraViewUp = [0.18850749851518855, 0.9376619196588085, 0.2919846698463883]
      renderView9.CameraParallelScale = 13.454876207783263
      renderView9.Background = [0.32, 0.34, 0.43]

      # init the 'GridAxes3DActor' selected for 'AxesGrid'
      renderView9.AxesGrid.XTitleFontFile = ''
      renderView9.AxesGrid.YTitleFontFile = ''
      renderView9.AxesGrid.ZTitleFontFile = ''
      renderView9.AxesGrid.XLabelFontFile = ''
      renderView9.AxesGrid.YLabelFontFile = ''
      renderView9.AxesGrid.ZLabelFontFile = ''

      # register the view with coprocessor
      # and provide it with information such as the filename to use,
      # how frequently to write the images, etc.
      coprocessor.RegisterView(renderView9,
          filename='RenderView4321_%t.png', freq=1, fittoscreen=1, magnification=1, width=839, height=869, cinema={})
      renderView9.ViewTime = datadescription.GetTime()

      # ----------------------------------------------------------------
      # restore active view
      SetActiveView(renderView10)
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

      # get color transfer function/color map for 'E_mean'
      e_meanLUT = GetColorTransferFunction('E_mean')
      e_meanLUT.RGBPoints = [6.384373773961045, 0.231373, 0.298039, 0.752941, 6.397468058702769, 0.865003, 0.865003, 0.865003, 6.410562343444494, 0.705882, 0.0156863, 0.14902]
      e_meanLUT.ScalarRangeInitialized = 1.0

      # get opacity transfer function/opacity map for 'E_mean'
      e_meanPWF = GetOpacityTransferFunction('E_mean')
      e_meanPWF.Points = [6.384373773961045, 0.0, 0.5, 0.0, 6.410562343444494, 1.0, 0.5, 0.0]
      e_meanPWF.ScalarRangeInitialized = 1

      # trace defaults for the display properties.
      inputDisplay.Representation = 'Volume'
      inputDisplay.ColorArrayName = ['POINTS', 'E_mean']
      inputDisplay.LookupTable = e_meanLUT
      inputDisplay.InterpolateScalarsBeforeMapping = 0
      inputDisplay.RenderPointsAsSpheres = 1
      inputDisplay.Interpolation = 'Flat'
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
      inputDisplay.ScalarOpacityFunction = e_meanPWF
      inputDisplay.VolumeRenderingMode = 'GPU Based'
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

      # get color legend/bar for e_meanLUT in view renderView1
      e_meanLUTColorBar = GetScalarBar(e_meanLUT, renderView1)
      e_meanLUTColorBar.Title = 'E_mean'
      e_meanLUTColorBar.ComponentTitle = ''
      e_meanLUTColorBar.TitleFontFile = ''
      e_meanLUTColorBar.LabelFontFile = ''

      # set color bar visibility
      e_meanLUTColorBar.Visibility = 1

      # show color legend
      inputDisplay.SetScalarBarVisibility(renderView1, True)

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView10'
      # ----------------------------------------------------------------

      # show data from input
      inputDisplay_1 = Show(input, renderView10)

      # get color transfer function/color map for 'rho_var'
      rho_varLUT = GetColorTransferFunction('rho_var')
      rho_varLUT.RGBPoints = [7.327471962526033e-15, 0.231373, 0.298039, 0.752941, 0.05300996129263258, 0.865003, 0.865003, 0.865003, 0.10601992258525783, 0.705882, 0.0156863, 0.14902]
      rho_varLUT.ScalarRangeInitialized = 1.0

      # get opacity transfer function/opacity map for 'rho_var'
      rho_varPWF = GetOpacityTransferFunction('rho_var')
      rho_varPWF.Points = [7.327471962526033e-15, 0.0, 0.5, 0.0, 0.10601992258525783, 1.0, 0.5, 0.0]
      rho_varPWF.ScalarRangeInitialized = 1

      # trace defaults for the display properties.
      inputDisplay_1.Representation = 'Volume'
      inputDisplay_1.ColorArrayName = ['POINTS', 'rho_var']
      inputDisplay_1.LookupTable = rho_varLUT
      inputDisplay_1.OSPRayScaleArray = 'rho_var'
      inputDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
      inputDisplay_1.SelectOrientationVectors = 'None'
      inputDisplay_1.ScaleFactor = 1.5
      inputDisplay_1.SelectScaleArray = 'None'
      inputDisplay_1.GlyphType = 'Arrow'
      inputDisplay_1.GlyphTableIndexArray = 'None'
      inputDisplay_1.GaussianRadius = 0.075
      inputDisplay_1.SetScaleArray = ['POINTS', 'rho_var']
      inputDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
      inputDisplay_1.OpacityArray = ['POINTS', 'rho_var']
      inputDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
      inputDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
      inputDisplay_1.SelectionCellLabelFontFile = ''
      inputDisplay_1.SelectionPointLabelFontFile = ''
      inputDisplay_1.PolarAxes = 'PolarAxesRepresentation'
      inputDisplay_1.ScalarOpacityUnitDistance = 1.7320508075688776
      inputDisplay_1.ScalarOpacityFunction = rho_varPWF
      inputDisplay_1.VolumeRenderingMode = 'GPU Based'
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

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView2'
      # ----------------------------------------------------------------

      # show data from input
      inputDisplay_2 = Show(input, renderView2)

      # get color transfer function/color map for 'E_var'
      e_varLUT = GetColorTransferFunction('E_var')
      e_varLUT.RGBPoints = [3.126388037344441e-13, 0.231373, 0.298039, 0.752941, 1.183453138509094e-05, 0.865003, 0.865003, 0.865003, 2.3669062457543077e-05, 0.705882, 0.0156863, 0.14902]
      e_varLUT.ScalarRangeInitialized = 1.0

      # get opacity transfer function/opacity map for 'E_var'
      e_varPWF = GetOpacityTransferFunction('E_var')
      e_varPWF.Points = [3.126388037344441e-13, 0.0, 0.5, 0.0, 2.3669062457543077e-05, 1.0, 0.5, 0.0]
      e_varPWF.ScalarRangeInitialized = 1

      # trace defaults for the display properties.
      inputDisplay_2.Representation = 'Volume'
      inputDisplay_2.ColorArrayName = ['POINTS', 'E_var']
      inputDisplay_2.LookupTable = e_varLUT
      inputDisplay_2.OSPRayScaleArray = 'E_mean'
      inputDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
      inputDisplay_2.SelectOrientationVectors = 'E_mean'
      inputDisplay_2.ScaleFactor = 1.5
      inputDisplay_2.SelectScaleArray = 'E_mean'
      inputDisplay_2.GlyphType = 'Arrow'
      inputDisplay_2.GlyphTableIndexArray = 'E_mean'
      inputDisplay_2.GaussianRadius = 0.075
      inputDisplay_2.SetScaleArray = ['POINTS', 'E_mean']
      inputDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
      inputDisplay_2.OpacityArray = ['POINTS', 'E_mean']
      inputDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
      inputDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
      inputDisplay_2.SelectionCellLabelFontFile = ''
      inputDisplay_2.SelectionPointLabelFontFile = ''
      inputDisplay_2.PolarAxes = 'PolarAxesRepresentation'
      inputDisplay_2.ScalarOpacityUnitDistance = 1.7320508075688776
      inputDisplay_2.ScalarOpacityFunction = e_varPWF
      inputDisplay_2.VolumeRenderingMode = 'GPU Based'
      inputDisplay_2.Slice = 7

      # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
      inputDisplay_2.OSPRayScaleFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

      # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
      inputDisplay_2.ScaleTransferFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

      # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
      inputDisplay_2.OpacityTransferFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

      # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
      inputDisplay_2.DataAxesGrid.XTitleFontFile = ''
      inputDisplay_2.DataAxesGrid.YTitleFontFile = ''
      inputDisplay_2.DataAxesGrid.ZTitleFontFile = ''
      inputDisplay_2.DataAxesGrid.XLabelFontFile = ''
      inputDisplay_2.DataAxesGrid.YLabelFontFile = ''
      inputDisplay_2.DataAxesGrid.ZLabelFontFile = ''

      # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
      inputDisplay_2.PolarAxes.PolarAxisTitleFontFile = ''
      inputDisplay_2.PolarAxes.PolarAxisLabelFontFile = ''
      inputDisplay_2.PolarAxes.LastRadialAxisTextFontFile = ''
      inputDisplay_2.PolarAxes.SecondaryRadialAxesTextFontFile = ''

      # setup the color legend parameters for each legend in this view

      # get color legend/bar for e_varLUT in view renderView2
      e_varLUTColorBar = GetScalarBar(e_varLUT, renderView2)
      e_varLUTColorBar.Position = [0.867699642431466, 0.01380897583429229]
      e_varLUTColorBar.Title = 'E_var'
      e_varLUTColorBar.ComponentTitle = ''
      e_varLUTColorBar.TitleFontFile = ''
      e_varLUTColorBar.LabelFontFile = ''

      # set color bar visibility
      e_varLUTColorBar.Visibility = 1

      # show color legend
      inputDisplay_2.SetScalarBarVisibility(renderView2, True)

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView3'
      # ----------------------------------------------------------------

      # show data from input
      inputDisplay_3 = Show(input, renderView3)

      # get color transfer function/color map for 'mx_mean'
      mx_meanLUT = GetColorTransferFunction('mx_mean')
      mx_meanLUT.RGBPoints = [0.1966843694485616, 0.231373, 0.298039, 0.752941, 0.27797292425157505, 0.865003, 0.865003, 0.865003, 0.35926147905458855, 0.705882, 0.0156863, 0.14902]
      mx_meanLUT.ScalarRangeInitialized = 1.0

      # get opacity transfer function/opacity map for 'mx_mean'
      mx_meanPWF = GetOpacityTransferFunction('mx_mean')
      mx_meanPWF.Points = [0.1966843694485616, 0.0, 0.5, 0.0, 0.35926147905458855, 1.0, 0.5, 0.0]
      mx_meanPWF.ScalarRangeInitialized = 1

      # trace defaults for the display properties.
      inputDisplay_3.Representation = 'Volume'
      inputDisplay_3.ColorArrayName = ['POINTS', 'mx_mean']
      inputDisplay_3.LookupTable = mx_meanLUT
      inputDisplay_3.OSPRayScaleArray = 'E_mean'
      inputDisplay_3.OSPRayScaleFunction = 'PiecewiseFunction'
      inputDisplay_3.SelectOrientationVectors = 'E_mean'
      inputDisplay_3.ScaleFactor = 1.5
      inputDisplay_3.SelectScaleArray = 'E_mean'
      inputDisplay_3.GlyphType = 'Arrow'
      inputDisplay_3.GlyphTableIndexArray = 'E_mean'
      inputDisplay_3.GaussianRadius = 0.075
      inputDisplay_3.SetScaleArray = ['POINTS', 'E_mean']
      inputDisplay_3.ScaleTransferFunction = 'PiecewiseFunction'
      inputDisplay_3.OpacityArray = ['POINTS', 'E_mean']
      inputDisplay_3.OpacityTransferFunction = 'PiecewiseFunction'
      inputDisplay_3.DataAxesGrid = 'GridAxesRepresentation'
      inputDisplay_3.SelectionCellLabelFontFile = ''
      inputDisplay_3.SelectionPointLabelFontFile = ''
      inputDisplay_3.PolarAxes = 'PolarAxesRepresentation'
      inputDisplay_3.ScalarOpacityUnitDistance = 1.7320508075688776
      inputDisplay_3.ScalarOpacityFunction = mx_meanPWF
      inputDisplay_3.VolumeRenderingMode = 'GPU Based'
      inputDisplay_3.Slice = 7

      # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
      inputDisplay_3.OSPRayScaleFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

      # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
      inputDisplay_3.ScaleTransferFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

      # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
      inputDisplay_3.OpacityTransferFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

      # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
      inputDisplay_3.DataAxesGrid.XTitleFontFile = ''
      inputDisplay_3.DataAxesGrid.YTitleFontFile = ''
      inputDisplay_3.DataAxesGrid.ZTitleFontFile = ''
      inputDisplay_3.DataAxesGrid.XLabelFontFile = ''
      inputDisplay_3.DataAxesGrid.YLabelFontFile = ''
      inputDisplay_3.DataAxesGrid.ZLabelFontFile = ''

      # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
      inputDisplay_3.PolarAxes.PolarAxisTitleFontFile = ''
      inputDisplay_3.PolarAxes.PolarAxisLabelFontFile = ''
      inputDisplay_3.PolarAxes.LastRadialAxisTextFontFile = ''
      inputDisplay_3.PolarAxes.SecondaryRadialAxesTextFontFile = ''

      # setup the color legend parameters for each legend in this view

      # get color legend/bar for mx_meanLUT in view renderView3
      mx_meanLUTColorBar = GetScalarBar(mx_meanLUT, renderView3)
      mx_meanLUTColorBar.Title = 'mx_mean'
      mx_meanLUTColorBar.ComponentTitle = ''
      mx_meanLUTColorBar.TitleFontFile = ''
      mx_meanLUTColorBar.LabelFontFile = ''

      # set color bar visibility
      mx_meanLUTColorBar.Visibility = 1

      # show color legend
      inputDisplay_3.SetScalarBarVisibility(renderView3, True)

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView4'
      # ----------------------------------------------------------------

      # show data from input
      inputDisplay_4 = Show(input, renderView4)

      # get color transfer function/color map for 'mx_var'
      mx_varLUT = GetColorTransferFunction('mx_var')
      mx_varLUT.RGBPoints = [1.8304802118507268e-13, 0.231373, 0.298039, 0.752941, 0.0018752632407424905, 0.865003, 0.865003, 0.865003, 0.003750526481301933, 0.705882, 0.0156863, 0.14902]
      mx_varLUT.ScalarRangeInitialized = 1.0

      # get opacity transfer function/opacity map for 'mx_var'
      mx_varPWF = GetOpacityTransferFunction('mx_var')
      mx_varPWF.Points = [1.8304802118507268e-13, 0.0, 0.5, 0.0, 0.003750526481301933, 1.0, 0.5, 0.0]
      mx_varPWF.ScalarRangeInitialized = 1

      # trace defaults for the display properties.
      inputDisplay_4.Representation = 'Volume'
      inputDisplay_4.ColorArrayName = ['POINTS', 'mx_var']
      inputDisplay_4.LookupTable = mx_varLUT
      inputDisplay_4.OSPRayScaleArray = 'E_mean'
      inputDisplay_4.OSPRayScaleFunction = 'PiecewiseFunction'
      inputDisplay_4.SelectOrientationVectors = 'E_mean'
      inputDisplay_4.ScaleFactor = 1.5
      inputDisplay_4.SelectScaleArray = 'E_mean'
      inputDisplay_4.GlyphType = 'Arrow'
      inputDisplay_4.GlyphTableIndexArray = 'E_mean'
      inputDisplay_4.GaussianRadius = 0.075
      inputDisplay_4.SetScaleArray = ['POINTS', 'E_mean']
      inputDisplay_4.ScaleTransferFunction = 'PiecewiseFunction'
      inputDisplay_4.OpacityArray = ['POINTS', 'E_mean']
      inputDisplay_4.OpacityTransferFunction = 'PiecewiseFunction'
      inputDisplay_4.DataAxesGrid = 'GridAxesRepresentation'
      inputDisplay_4.SelectionCellLabelFontFile = ''
      inputDisplay_4.SelectionPointLabelFontFile = ''
      inputDisplay_4.PolarAxes = 'PolarAxesRepresentation'
      inputDisplay_4.ScalarOpacityUnitDistance = 1.7320508075688776
      inputDisplay_4.ScalarOpacityFunction = mx_varPWF
      inputDisplay_4.VolumeRenderingMode = 'GPU Based'
      inputDisplay_4.Slice = 7

      # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
      inputDisplay_4.OSPRayScaleFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

      # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
      inputDisplay_4.ScaleTransferFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

      # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
      inputDisplay_4.OpacityTransferFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

      # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
      inputDisplay_4.DataAxesGrid.XTitleFontFile = ''
      inputDisplay_4.DataAxesGrid.YTitleFontFile = ''
      inputDisplay_4.DataAxesGrid.ZTitleFontFile = ''
      inputDisplay_4.DataAxesGrid.XLabelFontFile = ''
      inputDisplay_4.DataAxesGrid.YLabelFontFile = ''
      inputDisplay_4.DataAxesGrid.ZLabelFontFile = ''

      # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
      inputDisplay_4.PolarAxes.PolarAxisTitleFontFile = ''
      inputDisplay_4.PolarAxes.PolarAxisLabelFontFile = ''
      inputDisplay_4.PolarAxes.LastRadialAxisTextFontFile = ''
      inputDisplay_4.PolarAxes.SecondaryRadialAxesTextFontFile = ''

      # setup the color legend parameters for each legend in this view

      # get color legend/bar for mx_varLUT in view renderView4
      mx_varLUTColorBar = GetScalarBar(mx_varLUT, renderView4)
      mx_varLUTColorBar.Title = 'mx_var'
      mx_varLUTColorBar.ComponentTitle = ''
      mx_varLUTColorBar.TitleFontFile = ''
      mx_varLUTColorBar.LabelFontFile = ''

      # set color bar visibility
      mx_varLUTColorBar.Visibility = 1

      # show color legend
      inputDisplay_4.SetScalarBarVisibility(renderView4, True)

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView5'
      # ----------------------------------------------------------------

      # show data from input
      inputDisplay_5 = Show(input, renderView5)

      # get color transfer function/color map for 'my_mean'
      my_meanLUT = GetColorTransferFunction('my_mean')
      my_meanLUT.RGBPoints = [-0.0005318617114623177, 0.231373, 0.298039, 0.752941, -2.9579154056703005e-05, 0.865003, 0.865003, 0.865003, 0.00047270340334891166, 0.705882, 0.0156863, 0.14902]
      my_meanLUT.ScalarRangeInitialized = 1.0

      # get opacity transfer function/opacity map for 'my_mean'
      my_meanPWF = GetOpacityTransferFunction('my_mean')
      my_meanPWF.Points = [-0.0005318617114623177, 0.0, 0.5, 0.0, 0.00047270340334891166, 1.0, 0.5, 0.0]
      my_meanPWF.ScalarRangeInitialized = 1

      # trace defaults for the display properties.
      inputDisplay_5.Representation = 'Volume'
      inputDisplay_5.ColorArrayName = ['POINTS', 'my_mean']
      inputDisplay_5.LookupTable = my_meanLUT
      inputDisplay_5.OSPRayScaleArray = 'my_mean'
      inputDisplay_5.OSPRayScaleFunction = 'PiecewiseFunction'
      inputDisplay_5.SelectOrientationVectors = 'None'
      inputDisplay_5.ScaleFactor = 1.5
      inputDisplay_5.SelectScaleArray = 'None'
      inputDisplay_5.GlyphType = 'Arrow'
      inputDisplay_5.GlyphTableIndexArray = 'None'
      inputDisplay_5.GaussianRadius = 0.075
      inputDisplay_5.SetScaleArray = ['POINTS', 'my_mean']
      inputDisplay_5.ScaleTransferFunction = 'PiecewiseFunction'
      inputDisplay_5.OpacityArray = ['POINTS', 'my_mean']
      inputDisplay_5.OpacityTransferFunction = 'PiecewiseFunction'
      inputDisplay_5.DataAxesGrid = 'GridAxesRepresentation'
      inputDisplay_5.SelectionCellLabelFontFile = ''
      inputDisplay_5.SelectionPointLabelFontFile = ''
      inputDisplay_5.PolarAxes = 'PolarAxesRepresentation'
      inputDisplay_5.ScalarOpacityUnitDistance = 1.7320508075688776
      inputDisplay_5.ScalarOpacityFunction = my_meanPWF
      inputDisplay_5.VolumeRenderingMode = 'GPU Based'
      inputDisplay_5.Slice = 7

      # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
      inputDisplay_5.OSPRayScaleFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

      # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
      inputDisplay_5.ScaleTransferFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

      # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
      inputDisplay_5.OpacityTransferFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

      # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
      inputDisplay_5.DataAxesGrid.XTitleFontFile = ''
      inputDisplay_5.DataAxesGrid.YTitleFontFile = ''
      inputDisplay_5.DataAxesGrid.ZTitleFontFile = ''
      inputDisplay_5.DataAxesGrid.XLabelFontFile = ''
      inputDisplay_5.DataAxesGrid.YLabelFontFile = ''
      inputDisplay_5.DataAxesGrid.ZLabelFontFile = ''

      # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
      inputDisplay_5.PolarAxes.PolarAxisTitleFontFile = ''
      inputDisplay_5.PolarAxes.PolarAxisLabelFontFile = ''
      inputDisplay_5.PolarAxes.LastRadialAxisTextFontFile = ''
      inputDisplay_5.PolarAxes.SecondaryRadialAxesTextFontFile = ''

      # setup the color legend parameters for each legend in this view

      # get color legend/bar for my_meanLUT in view renderView5
      my_meanLUTColorBar = GetScalarBar(my_meanLUT, renderView5)
      my_meanLUTColorBar.Title = 'my_mean'
      my_meanLUTColorBar.ComponentTitle = ''
      my_meanLUTColorBar.TitleFontFile = ''
      my_meanLUTColorBar.LabelFontFile = ''

      # set color bar visibility
      my_meanLUTColorBar.Visibility = 1

      # show color legend
      inputDisplay_5.SetScalarBarVisibility(renderView5, True)

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView6'
      # ----------------------------------------------------------------

      # show data from input
      inputDisplay_6 = Show(input, renderView6)

      # get color transfer function/color map for 'my_var'
      my_varLUT = GetColorTransferFunction('my_var')
      my_varLUT.RGBPoints = [3.792124236755382e-15, 0.231373, 0.298039, 0.752941, 9.817798570548125e-08, 0.865003, 0.865003, 0.865003, 1.9635596761883828e-07, 0.705882, 0.0156863, 0.14902]
      my_varLUT.ScalarRangeInitialized = 1.0

      # get opacity transfer function/opacity map for 'my_var'
      my_varPWF = GetOpacityTransferFunction('my_var')
      my_varPWF.Points = [3.792124236755382e-15, 0.0, 0.5, 0.0, 1.9635596761883828e-07, 1.0, 0.5, 0.0]
      my_varPWF.ScalarRangeInitialized = 1

      # trace defaults for the display properties.
      inputDisplay_6.Representation = 'Volume'
      inputDisplay_6.ColorArrayName = ['POINTS', 'my_var']
      inputDisplay_6.LookupTable = my_varLUT
      inputDisplay_6.OSPRayScaleArray = 'my_var'
      inputDisplay_6.OSPRayScaleFunction = 'PiecewiseFunction'
      inputDisplay_6.SelectOrientationVectors = 'None'
      inputDisplay_6.ScaleFactor = 1.5
      inputDisplay_6.SelectScaleArray = 'None'
      inputDisplay_6.GlyphType = 'Arrow'
      inputDisplay_6.GlyphTableIndexArray = 'None'
      inputDisplay_6.GaussianRadius = 0.075
      inputDisplay_6.SetScaleArray = ['POINTS', 'my_var']
      inputDisplay_6.ScaleTransferFunction = 'PiecewiseFunction'
      inputDisplay_6.OpacityArray = ['POINTS', 'my_var']
      inputDisplay_6.OpacityTransferFunction = 'PiecewiseFunction'
      inputDisplay_6.DataAxesGrid = 'GridAxesRepresentation'
      inputDisplay_6.SelectionCellLabelFontFile = ''
      inputDisplay_6.SelectionPointLabelFontFile = ''
      inputDisplay_6.PolarAxes = 'PolarAxesRepresentation'
      inputDisplay_6.ScalarOpacityUnitDistance = 1.7320508075688776
      inputDisplay_6.ScalarOpacityFunction = my_varPWF
      inputDisplay_6.VolumeRenderingMode = 'GPU Based'
      inputDisplay_6.Slice = 7

      # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
      inputDisplay_6.OSPRayScaleFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

      # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
      inputDisplay_6.ScaleTransferFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

      # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
      inputDisplay_6.OpacityTransferFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

      # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
      inputDisplay_6.DataAxesGrid.XTitleFontFile = ''
      inputDisplay_6.DataAxesGrid.YTitleFontFile = ''
      inputDisplay_6.DataAxesGrid.ZTitleFontFile = ''
      inputDisplay_6.DataAxesGrid.XLabelFontFile = ''
      inputDisplay_6.DataAxesGrid.YLabelFontFile = ''
      inputDisplay_6.DataAxesGrid.ZLabelFontFile = ''

      # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
      inputDisplay_6.PolarAxes.PolarAxisTitleFontFile = ''
      inputDisplay_6.PolarAxes.PolarAxisLabelFontFile = ''
      inputDisplay_6.PolarAxes.LastRadialAxisTextFontFile = ''
      inputDisplay_6.PolarAxes.SecondaryRadialAxesTextFontFile = ''

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView7'
      # ----------------------------------------------------------------

      # show data from input
      inputDisplay_7 = Show(input, renderView7)

      # get color transfer function/color map for 'mz_mean'
      mz_meanLUT = GetColorTransferFunction('mz_mean')
      mz_meanLUT.RGBPoints = [-0.0003734129861518945, 0.231373, 0.298039, 0.752941, 5.109169672523427e-05, 0.865003, 0.865003, 0.865003, 0.00047559637960236306, 0.705882, 0.0156863, 0.14902]
      mz_meanLUT.ScalarRangeInitialized = 1.0

      # get opacity transfer function/opacity map for 'mz_mean'
      mz_meanPWF = GetOpacityTransferFunction('mz_mean')
      mz_meanPWF.Points = [-0.0003734129861518945, 0.0, 0.5, 0.0, 0.00047559637960236306, 1.0, 0.5, 0.0]
      mz_meanPWF.ScalarRangeInitialized = 1

      # trace defaults for the display properties.
      inputDisplay_7.Representation = 'Volume'
      inputDisplay_7.ColorArrayName = ['POINTS', 'mz_mean']
      inputDisplay_7.LookupTable = mz_meanLUT
      inputDisplay_7.OSPRayScaleArray = 'mz_mean'
      inputDisplay_7.OSPRayScaleFunction = 'PiecewiseFunction'
      inputDisplay_7.SelectOrientationVectors = 'None'
      inputDisplay_7.ScaleFactor = 1.5
      inputDisplay_7.SelectScaleArray = 'None'
      inputDisplay_7.GlyphType = 'Arrow'
      inputDisplay_7.GlyphTableIndexArray = 'None'
      inputDisplay_7.GaussianRadius = 0.075
      inputDisplay_7.SetScaleArray = ['POINTS', 'mz_mean']
      inputDisplay_7.ScaleTransferFunction = 'PiecewiseFunction'
      inputDisplay_7.OpacityArray = ['POINTS', 'mz_mean']
      inputDisplay_7.OpacityTransferFunction = 'PiecewiseFunction'
      inputDisplay_7.DataAxesGrid = 'GridAxesRepresentation'
      inputDisplay_7.SelectionCellLabelFontFile = ''
      inputDisplay_7.SelectionPointLabelFontFile = ''
      inputDisplay_7.PolarAxes = 'PolarAxesRepresentation'
      inputDisplay_7.ScalarOpacityUnitDistance = 1.7320508075688776
      inputDisplay_7.ScalarOpacityFunction = mz_meanPWF
      inputDisplay_7.Slice = 7

      # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
      inputDisplay_7.OSPRayScaleFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

      # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
      inputDisplay_7.ScaleTransferFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

      # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
      inputDisplay_7.OpacityTransferFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

      # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
      inputDisplay_7.DataAxesGrid.XTitleFontFile = ''
      inputDisplay_7.DataAxesGrid.YTitleFontFile = ''
      inputDisplay_7.DataAxesGrid.ZTitleFontFile = ''
      inputDisplay_7.DataAxesGrid.XLabelFontFile = ''
      inputDisplay_7.DataAxesGrid.YLabelFontFile = ''
      inputDisplay_7.DataAxesGrid.ZLabelFontFile = ''

      # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
      inputDisplay_7.PolarAxes.PolarAxisTitleFontFile = ''
      inputDisplay_7.PolarAxes.PolarAxisLabelFontFile = ''
      inputDisplay_7.PolarAxes.LastRadialAxisTextFontFile = ''
      inputDisplay_7.PolarAxes.SecondaryRadialAxesTextFontFile = ''

      # setup the color legend parameters for each legend in this view

      # get color legend/bar for mz_meanLUT in view renderView7
      mz_meanLUTColorBar = GetScalarBar(mz_meanLUT, renderView7)
      mz_meanLUTColorBar.Title = 'mz_mean'
      mz_meanLUTColorBar.ComponentTitle = ''
      mz_meanLUTColorBar.TitleFontFile = ''
      mz_meanLUTColorBar.LabelFontFile = ''

      # set color bar visibility
      mz_meanLUTColorBar.Visibility = 1

      # show color legend
      inputDisplay_7.SetScalarBarVisibility(renderView7, True)

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView8'
      # ----------------------------------------------------------------

      # show data from input
      inputDisplay_8 = Show(input, renderView8)

      # get color transfer function/color map for 'mz_var'
      mz_varLUT = GetColorTransferFunction('mz_var')
      mz_varLUT.RGBPoints = [5.744363760126085e-16, 0.231373, 0.298039, 0.752941, 6.663907762671332e-08, 0.865003, 0.865003, 0.865003, 1.3327815467899028e-07, 0.705882, 0.0156863, 0.14902]
      mz_varLUT.ScalarRangeInitialized = 1.0

      # get opacity transfer function/opacity map for 'mz_var'
      mz_varPWF = GetOpacityTransferFunction('mz_var')
      mz_varPWF.Points = [5.744363760126085e-16, 0.0, 0.5, 0.0, 1.3327815467899028e-07, 1.0, 0.5, 0.0]
      mz_varPWF.ScalarRangeInitialized = 1

      # trace defaults for the display properties.
      inputDisplay_8.Representation = 'Volume'
      inputDisplay_8.ColorArrayName = ['POINTS', 'mz_var']
      inputDisplay_8.LookupTable = mz_varLUT
      inputDisplay_8.OSPRayScaleArray = 'mz_var'
      inputDisplay_8.OSPRayScaleFunction = 'PiecewiseFunction'
      inputDisplay_8.SelectOrientationVectors = 'None'
      inputDisplay_8.ScaleFactor = 1.5
      inputDisplay_8.SelectScaleArray = 'None'
      inputDisplay_8.GlyphType = 'Arrow'
      inputDisplay_8.GlyphTableIndexArray = 'None'
      inputDisplay_8.GaussianRadius = 0.075
      inputDisplay_8.SetScaleArray = ['POINTS', 'mz_var']
      inputDisplay_8.ScaleTransferFunction = 'PiecewiseFunction'
      inputDisplay_8.OpacityArray = ['POINTS', 'mz_var']
      inputDisplay_8.OpacityTransferFunction = 'PiecewiseFunction'
      inputDisplay_8.DataAxesGrid = 'GridAxesRepresentation'
      inputDisplay_8.SelectionCellLabelFontFile = ''
      inputDisplay_8.SelectionPointLabelFontFile = ''
      inputDisplay_8.PolarAxes = 'PolarAxesRepresentation'
      inputDisplay_8.ScalarOpacityUnitDistance = 1.7320508075688776
      inputDisplay_8.ScalarOpacityFunction = mz_varPWF
      inputDisplay_8.VolumeRenderingMode = 'GPU Based'
      inputDisplay_8.Slice = 7

      # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
      inputDisplay_8.OSPRayScaleFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

      # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
      inputDisplay_8.ScaleTransferFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

      # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
      inputDisplay_8.OpacityTransferFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

      # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
      inputDisplay_8.DataAxesGrid.XTitleFontFile = ''
      inputDisplay_8.DataAxesGrid.YTitleFontFile = ''
      inputDisplay_8.DataAxesGrid.ZTitleFontFile = ''
      inputDisplay_8.DataAxesGrid.XLabelFontFile = ''
      inputDisplay_8.DataAxesGrid.YLabelFontFile = ''
      inputDisplay_8.DataAxesGrid.ZLabelFontFile = ''

      # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
      inputDisplay_8.PolarAxes.PolarAxisTitleFontFile = ''
      inputDisplay_8.PolarAxes.PolarAxisLabelFontFile = ''
      inputDisplay_8.PolarAxes.LastRadialAxisTextFontFile = ''
      inputDisplay_8.PolarAxes.SecondaryRadialAxesTextFontFile = ''

      # setup the color legend parameters for each legend in this view

      # get color legend/bar for mz_varLUT in view renderView8
      mz_varLUTColorBar = GetScalarBar(mz_varLUT, renderView8)
      mz_varLUTColorBar.Title = 'mz_var'
      mz_varLUTColorBar.ComponentTitle = ''
      mz_varLUTColorBar.TitleFontFile = ''
      mz_varLUTColorBar.LabelFontFile = ''

      # set color bar visibility
      mz_varLUTColorBar.Visibility = 1

      # show color legend
      inputDisplay_8.SetScalarBarVisibility(renderView8, True)

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView9'
      # ----------------------------------------------------------------

      # show data from input
      inputDisplay_9 = Show(input, renderView9)

      # get color transfer function/color map for 'rho_mean'
      rho_meanLUT = GetColorTransferFunction('rho_mean')
      rho_meanLUT.RGBPoints = [1.0016140251131045, 0.231373, 0.298039, 0.752941, 1.4894833747421563, 0.865003, 0.865003, 0.865003, 1.9773527243712083, 0.705882, 0.0156863, 0.14902]
      rho_meanLUT.ScalarRangeInitialized = 1.0

      # get opacity transfer function/opacity map for 'rho_mean'
      rho_meanPWF = GetOpacityTransferFunction('rho_mean')
      rho_meanPWF.Points = [1.0016140251131045, 0.0, 0.5, 0.0, 1.9773527243712083, 1.0, 0.5, 0.0]
      rho_meanPWF.ScalarRangeInitialized = 1

      # trace defaults for the display properties.
      inputDisplay_9.Representation = 'Volume'
      inputDisplay_9.ColorArrayName = ['POINTS', 'rho_mean']
      inputDisplay_9.LookupTable = rho_meanLUT
      inputDisplay_9.OSPRayScaleArray = 'rho_mean'
      inputDisplay_9.OSPRayScaleFunction = 'PiecewiseFunction'
      inputDisplay_9.SelectOrientationVectors = 'None'
      inputDisplay_9.ScaleFactor = 1.5
      inputDisplay_9.SelectScaleArray = 'None'
      inputDisplay_9.GlyphType = 'Arrow'
      inputDisplay_9.GlyphTableIndexArray = 'None'
      inputDisplay_9.GaussianRadius = 0.075
      inputDisplay_9.SetScaleArray = ['POINTS', 'rho_mean']
      inputDisplay_9.ScaleTransferFunction = 'PiecewiseFunction'
      inputDisplay_9.OpacityArray = ['POINTS', 'rho_mean']
      inputDisplay_9.OpacityTransferFunction = 'PiecewiseFunction'
      inputDisplay_9.DataAxesGrid = 'GridAxesRepresentation'
      inputDisplay_9.SelectionCellLabelFontFile = ''
      inputDisplay_9.SelectionPointLabelFontFile = ''
      inputDisplay_9.PolarAxes = 'PolarAxesRepresentation'
      inputDisplay_9.ScalarOpacityUnitDistance = 1.7320508075688776
      inputDisplay_9.ScalarOpacityFunction = rho_meanPWF
      inputDisplay_9.VolumeRenderingMode = 'GPU Based'
      inputDisplay_9.Slice = 7

      # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
      inputDisplay_9.OSPRayScaleFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

      # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
      inputDisplay_9.ScaleTransferFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

      # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
      inputDisplay_9.OpacityTransferFunction.Points = [1.9984014443252818e-13, 0.0, 0.5, 0.0, 0.2761551785771892, 1.0, 0.5, 0.0]

      # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
      inputDisplay_9.DataAxesGrid.XTitleFontFile = ''
      inputDisplay_9.DataAxesGrid.YTitleFontFile = ''
      inputDisplay_9.DataAxesGrid.ZTitleFontFile = ''
      inputDisplay_9.DataAxesGrid.XLabelFontFile = ''
      inputDisplay_9.DataAxesGrid.YLabelFontFile = ''
      inputDisplay_9.DataAxesGrid.ZLabelFontFile = ''

      # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
      inputDisplay_9.PolarAxes.PolarAxisTitleFontFile = ''
      inputDisplay_9.PolarAxes.PolarAxisLabelFontFile = ''
      inputDisplay_9.PolarAxes.LastRadialAxisTextFontFile = ''
      inputDisplay_9.PolarAxes.SecondaryRadialAxesTextFontFile = ''

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
  freqs = {'input': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}
  coprocessor.SetUpdateFrequencies(freqs)
  if requestSpecificArrays:
    arrays = [['rho_var', 0]]
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
