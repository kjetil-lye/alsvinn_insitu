
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
      renderView1.ViewSize = [1185, 779]
      renderView1.AxesGrid = 'GridAxes3DActor'
      renderView1.CenterOfRotation = [3.5, 3.5, 3.5]
      renderView1.StereoType = 0
      renderView1.CameraPosition = [-13.671005379152112, -12.422554895216518, 3.009807598415387]
      renderView1.CameraFocalPoint = [3.5, 3.5, 3.5]
      renderView1.CameraViewUp = [-0.025254890327717765, -0.003540959385587175, 0.9996747731743383]
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
          filename='rhomean_%t.png', freq=1, fittoscreen=1, magnification=1, width=1185, height=779, cinema={})
      renderView1.ViewTime = datadescription.GetTime()

      # Create a new 'Render View'
      renderView2 = CreateView('RenderView')
      renderView2.ViewSize = [1185, 779]
      renderView2.AxesGrid = 'GridAxes3DActor'
      renderView2.CenterAxesVisibility = 1
      renderView2.CenterOfRotation = [3.5, 3.5, 3.5]
      renderView2.StereoType = 0
      renderView2.CameraPosition = [-13.073797071289516, -13.049730307229542, 3.664760766896179]
      renderView2.CameraFocalPoint = [3.499999999999999, 3.500000000000001, 3.500000000000001]
      renderView2.CameraViewUp = [0.0035851275338588252, 0.006364888879524978, 0.9999733171690719]
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
          filename='mean_%t.png', freq=1, fittoscreen=1, magnification=1, width=1185, height=779, cinema={})
      renderView2.ViewTime = datadescription.GetTime()

      # Create a new 'Render View'
      renderView3 = CreateView('RenderView')
      renderView3.ViewSize = [1185, 779]
      renderView3.AxesGrid = 'GridAxes3DActor'
      renderView3.CenterOfRotation = [3.5, 3.5, 3.5]
      renderView3.StereoType = 0
      renderView3.CameraPosition = [-12.716416356204968, -13.397831892575981, 3.1797085622772867]
      renderView3.CameraFocalPoint = [3.500000000000001, 3.499999999999999, 3.499999999999999]
      renderView3.CameraViewUp = [-0.016119282392850195, -0.0034827477946395144, 0.9998640103548775]
      renderView3.CameraParallelScale = 6.06217782649107
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
          filename='var_%t.png', freq=1, fittoscreen=1, magnification=1, width=1185, height=779, cinema={})
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

      # create a new 'XML Partitioned Image Data Reader'
      # create a producer from a simulation input
      input_1 = coprocessor.CreateProducer(datadescription, 'input')

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView1'
      # ----------------------------------------------------------------

      # show data from input_1
      input_1Display = Show(input_1, renderView1)



      # get color transfer function/color map for 'rho_mean'
      rho_meanLUT = GetColorTransferFunction('rho_mean')
      rho_meanLUT.RescaleOnVisibilityChange = 1
      rho_meanLUT.RGBPoints = [0.998567552707725, 0.054902, 0.109804, 0.121569, 1.047598979586151, 0.07451, 0.172549, 0.180392, 1.0966304064645769, 0.086275, 0.231373, 0.219608, 1.1456618333430029, 0.094118, 0.278431, 0.25098, 1.1946932602214289, 0.109804, 0.34902, 0.278431, 1.2437246870998548, 0.113725, 0.4, 0.278431, 1.2927561139782808, 0.117647, 0.45098, 0.270588, 1.3417875408567066, 0.117647, 0.490196, 0.243137, 1.3908189677351326, 0.113725, 0.521569, 0.203922, 1.4398503946135586, 0.109804, 0.54902, 0.152941, 1.4888818214919846, 0.082353, 0.588235, 0.082353, 1.5379132483704105, 0.109804, 0.631373, 0.05098, 1.5869446752488363, 0.211765, 0.678431, 0.082353, 1.6359761021272625, 0.317647, 0.721569, 0.113725, 1.6850075290056883, 0.431373, 0.760784, 0.160784, 1.7340389558841143, 0.556863, 0.8, 0.239216, 1.7830703827625403, 0.666667, 0.839216, 0.294118, 1.832101809640966, 0.784314, 0.878431, 0.396078, 1.8811332365193922, 0.886275, 0.921569, 0.533333, 1.930164663397818, 0.960784, 0.94902, 0.670588, 1.979196090276244, 1.0, 0.984314, 0.901961]
      rho_meanLUT.ColorSpace = 'Lab'
      rho_meanLUT.NanColor = [0.25, 0.0, 0.0]
      rho_meanLUT.ScalarRangeInitialized = 1.0

      # get opacity transfer function/opacity map for 'rho_mean'
      rho_meanPWF = GetOpacityTransferFunction('rho_mean')
      rho_meanPWF.Points = [0.998567552707725, 0.0, 0.5, 0.0, 1.979196090276244, 1.0, 0.5, 0.0]
      rho_meanPWF.ScalarRangeInitialized = 1

      # trace defaults for the display properties.
      input_1Display.Representation = 'Volume'
      input_1Display.ColorArrayName = ['POINTS', 'rho_mean']
      input_1Display.LookupTable = rho_meanLUT
      input_1Display.OSPRayScaleArray = 'rho_mean'
      input_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
      input_1Display.SelectOrientationVectors = 'None'
      input_1Display.ScaleFactor = 0.7000000000000001
      input_1Display.SelectScaleArray = 'None'
      input_1Display.GlyphType = 'Arrow'
      input_1Display.GlyphTableIndexArray = 'None'
      input_1Display.GaussianRadius = 0.035
      input_1Display.SetScaleArray = ['POINTS', 'rho_mean']
      input_1Display.ScaleTransferFunction = 'PiecewiseFunction'
      input_1Display.OpacityArray = ['POINTS', 'rho_mean']
      input_1Display.OpacityTransferFunction = 'PiecewiseFunction'
      input_1Display.DataAxesGrid = 'GridAxesRepresentation'
      input_1Display.SelectionCellLabelFontFile = ''
      input_1Display.SelectionPointLabelFontFile = ''
      input_1Display.PolarAxes = 'PolarAxesRepresentation'
      input_1Display.ScalarOpacityUnitDistance = 1.7320508075688772
      input_1Display.ScalarOpacityFunction = rho_meanPWF
      input_1Display.Slice = 3

      # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
      input_1Display.DataAxesGrid.XTitleFontFile = ''
      input_1Display.DataAxesGrid.YTitleFontFile = ''
      input_1Display.DataAxesGrid.ZTitleFontFile = ''
      input_1Display.DataAxesGrid.XLabelFontFile = ''
      input_1Display.DataAxesGrid.YLabelFontFile = ''
      input_1Display.DataAxesGrid.ZLabelFontFile = ''

      # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
      input_1Display.PolarAxes.PolarAxisTitleFontFile = ''
      input_1Display.PolarAxes.PolarAxisLabelFontFile = ''
      input_1Display.PolarAxes.LastRadialAxisTextFontFile = ''
      input_1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''

      # show data from input
      inputDisplay = Show(input, renderView1)

      # get color transfer function/color map for 'rho_var'
      rho_varLUT = GetColorTransferFunction('rho_var')
      rho_varLUT.RescaleOnVisibilityChange = 1
      rho_varLUT.RGBPoints = [3.375300039465401e-12, 0.001462, 0.000466, 0.013866, 0.0006300062867031984, 0.002267, 0.00127, 0.01857, 0.0012598519360985806, 0.003299, 0.002249, 0.024239, 0.0018898582194264788, 0.004547, 0.003392, 0.030909, 0.002519703868821861, 0.006006, 0.004692, 0.038558, 0.0031497101521497594, 0.007676, 0.006136, 0.046836, 0.003779555801545142, 0.009561, 0.007713, 0.055143, 0.00440956208487304, 0.011663, 0.009417, 0.06346, 0.005039568368200938, 0.013995, 0.011225, 0.071862, 0.0056694140175963205, 0.016561, 0.013136, 0.080282, 0.006299420300924219, 0.019373, 0.015133, 0.088767, 0.006929265950319601, 0.022447, 0.017199, 0.097327, 0.007559272233647499, 0.025793, 0.019331, 0.10593, 0.008189117883042881, 0.029432, 0.021503, 0.114621, 0.00881912416637078, 0.033385, 0.023702, 0.123397, 0.00944913044969868, 0.037668, 0.025921, 0.132232, 0.01007897609909406, 0.042253, 0.028139, 0.141141, 0.01070898238242196, 0.046915, 0.030324, 0.150164, 0.011338828031817341, 0.051644, 0.032474, 0.159254, 0.011968834315145241, 0.056449, 0.034569, 0.168414, 0.012598679964540623, 0.06134, 0.03659, 0.177642, 0.013228686247868519, 0.066331, 0.038504, 0.186962, 0.013858692531196419, 0.071429, 0.040294, 0.196354, 0.0144885381805918, 0.076637, 0.041905, 0.205799, 0.015118544463919697, 0.081962, 0.043328, 0.215289, 0.01574839011331508, 0.087411, 0.044556, 0.224813, 0.01637839639664298, 0.09299, 0.045583, 0.234358, 0.017008242046038364, 0.098702, 0.046402, 0.243904, 0.01763824832936626, 0.104551, 0.047008, 0.25343, 0.018268093978761644, 0.110536, 0.047399, 0.262912, 0.018898100262089542, 0.116656, 0.047574, 0.272321, 0.019528106545417437, 0.122908, 0.047536, 0.281624, 0.02015795219481282, 0.129285, 0.047293, 0.290788, 0.02078795847814072, 0.135778, 0.046856, 0.299776, 0.021417804127536102, 0.142378, 0.046242, 0.308553, 0.022047810410863997, 0.149073, 0.045468, 0.317085, 0.02267765606025938, 0.15585, 0.044559, 0.325338, 0.02330766234358728, 0.162689, 0.043554, 0.333277, 0.02393766862691518, 0.169575, 0.042489, 0.340874, 0.02456751427631056, 0.176493, 0.041402, 0.348111, 0.02519752055963846, 0.183429, 0.040329, 0.354971, 0.025827366209033843, 0.190367, 0.039309, 0.361447, 0.026457372492361738, 0.197297, 0.0384, 0.367535, 0.027087218141757123, 0.204209, 0.037632, 0.373238, 0.02771722442508502, 0.211095, 0.03703, 0.378563, 0.028347230708412916, 0.217949, 0.036615, 0.383522, 0.0289770763578083, 0.224763, 0.036405, 0.388129, 0.0296070826411362, 0.231538, 0.036405, 0.3924, 0.030236928290531585, 0.238273, 0.036621, 0.396353, 0.03086693457385948, 0.244967, 0.037055, 0.400007, 0.03149678022325486, 0.25162, 0.037705, 0.403378, 0.03212678650658276, 0.258234, 0.038571, 0.406485, 0.03275679278991066, 0.26481, 0.039647, 0.409345, 0.03338663843930604, 0.271347, 0.040922, 0.411976, 0.034016644722633944, 0.27785, 0.042353, 0.414392, 0.03464649037202932, 0.284321, 0.043933, 0.416608, 0.03527649665535722, 0.290763, 0.045644, 0.418637, 0.035906342304752606, 0.297178, 0.04747, 0.420491, 0.0365363485880805, 0.303568, 0.049396, 0.422182, 0.037166354871408395, 0.309935, 0.051407, 0.423721, 0.037796200520803784, 0.316282, 0.05349, 0.425116, 0.03842620680413168, 0.32261, 0.055634, 0.426377, 0.039056052453527064, 0.328921, 0.057827, 0.427511, 0.03968605873685496, 0.335217, 0.06006, 0.428524, 0.04031590438625034, 0.3415, 0.062325, 0.429425, 0.04094591066957824, 0.347771, 0.064616, 0.430217, 0.04157591695290614, 0.354032, 0.066925, 0.430906, 0.04220576260230152, 0.360284, 0.069247, 0.431497, 0.04283576888562942, 0.366529, 0.071579, 0.431994, 0.0434656145350248, 0.372768, 0.073915, 0.4324, 0.04409562081835269, 0.379001, 0.076253, 0.432719, 0.04472546646774808, 0.385228, 0.078591, 0.432955, 0.04535547275107599, 0.391453, 0.080927, 0.433109, 0.04598547903440388, 0.397674, 0.083257, 0.433183, 0.04661532468379926, 0.403894, 0.08558, 0.433179, 0.04724533096712716, 0.410113, 0.087896, 0.433098, 0.04787517661652254, 0.416331, 0.090203, 0.432943, 0.04850518289985044, 0.422549, 0.092501, 0.432714, 0.04913502854924582, 0.428768, 0.09479, 0.432412, 0.049765034832573725, 0.434987, 0.097069, 0.432039, 0.0503948804819691, 0.441207, 0.099338, 0.431594, 0.051024886765297005, 0.447428, 0.101597, 0.43108, 0.051654893048624896, 0.453651, 0.103848, 0.430498, 0.052284738698020285, 0.459875, 0.106089, 0.429846, 0.052914744981348176, 0.4661, 0.108322, 0.429125, 0.05354459063074356, 0.472328, 0.110547, 0.428334, 0.05417459691407146, 0.478558, 0.112764, 0.427475, 0.05480444256346684, 0.484789, 0.114974, 0.426548, 0.05543444884679474, 0.491022, 0.117179, 0.425552, 0.05606445513012264, 0.497257, 0.119379, 0.424488, 0.05669430077951802, 0.503493, 0.121575, 0.423356, 0.05732430706284592, 0.50973, 0.123769, 0.422156, 0.0579541527122413, 0.515967, 0.12596, 0.420887, 0.058584158995569194, 0.522206, 0.12815, 0.419549, 0.05921400464496458, 0.528444, 0.130341, 0.418142, 0.05984401092829249, 0.534683, 0.132534, 0.416667, 0.06047401721162038, 0.54092, 0.134729, 0.415123, 0.06110386286101576, 0.547157, 0.136929, 0.413511, 0.06173386914434366, 0.553392, 0.139134, 0.411829, 0.06236371479373904, 0.559624, 0.141346, 0.410078, 0.06299372107706694, 0.565854, 0.143567, 0.408258, 0.06362356672646233, 0.572081, 0.145797, 0.406369, 0.06425357300979022, 0.578304, 0.148039, 0.404411, 0.06488357929311812, 0.584521, 0.150294, 0.402385, 0.0655134249425135, 0.590734, 0.152563, 0.40029, 0.0661434312258414, 0.59694, 0.154848, 0.398125, 0.06677327687523678, 0.603139, 0.157151, 0.395891, 0.06740328315856468, 0.60933, 0.159474, 0.393589, 0.06803312880796006, 0.615513, 0.161817, 0.391219, 0.06866313509128796, 0.621685, 0.164184, 0.388781, 0.06929314137461585, 0.627847, 0.166575, 0.386276, 0.06992298702401124, 0.633998, 0.168992, 0.383704, 0.07055299330733913, 0.640135, 0.171438, 0.381065, 0.07118283895673452, 0.64626, 0.173914, 0.378359, 0.07181284524006241, 0.652369, 0.176421, 0.375586, 0.0724426908894578, 0.658463, 0.178962, 0.372748, 0.0730726971727857, 0.66454, 0.181539, 0.369846, 0.0737027034561136, 0.670599, 0.184153, 0.366879, 0.07433254910550899, 0.676638, 0.186807, 0.363849, 0.07496255538883688, 0.682656, 0.189501, 0.360757, 0.07559240103823227, 0.688653, 0.192239, 0.357603, 0.07622240732156016, 0.694627, 0.195021, 0.354388, 0.07685225297095555, 0.700576, 0.197851, 0.351113, 0.07748225925428344, 0.7065, 0.200728, 0.347777, 0.07811226553761134, 0.712396, 0.203656, 0.344383, 0.07874211118700672, 0.718264, 0.206636, 0.340931, 0.07937211747033462, 0.724103, 0.20967, 0.337424, 0.08000196311973, 0.729909, 0.212759, 0.333861, 0.0806319694030579, 0.735683, 0.215906, 0.330245, 0.08126181505245329, 0.741423, 0.219112, 0.326576, 0.08189182133578118, 0.747127, 0.222378, 0.322856, 0.08252166698517656, 0.752794, 0.225706, 0.319085, 0.08315167326850445, 0.758422, 0.229097, 0.315266, 0.08378167955183236, 0.76401, 0.232554, 0.311399, 0.08441152520122774, 0.769556, 0.236077, 0.307485, 0.08504153148455564, 0.775059, 0.239667, 0.303526, 0.08567137713395101, 0.780517, 0.243327, 0.299523, 0.08630138341727893, 0.785929, 0.247056, 0.295477, 0.0869312290666743, 0.791293, 0.250856, 0.29139, 0.0875612353500022, 0.796607, 0.254728, 0.287264, 0.08819124163333009, 0.801871, 0.258674, 0.283099, 0.08882108728272549, 0.807082, 0.262692, 0.278898, 0.08945109356605338, 0.812239, 0.266786, 0.274661, 0.09008093921544875, 0.817341, 0.270954, 0.27039, 0.09071094549877667, 0.822386, 0.275197, 0.266085, 0.09134079114817205, 0.827372, 0.279517, 0.26175, 0.09197079743149994, 0.832299, 0.283913, 0.257383, 0.09260080371482783, 0.837165, 0.288385, 0.252988, 0.09323064936422322, 0.841969, 0.292933, 0.248564, 0.09386065564755113, 0.846709, 0.297559, 0.244113, 0.0944905012969465, 0.851384, 0.30226, 0.239636, 0.0951205075802744, 0.855992, 0.307038, 0.235133, 0.09575035322966978, 0.860533, 0.311892, 0.230606, 0.09638035951299768, 0.865006, 0.316822, 0.226055, 0.09701036579632558, 0.869409, 0.321827, 0.221482, 0.09764021144572096, 0.873741, 0.326906, 0.216886, 0.09827021772904886, 0.878001, 0.33206, 0.212268, 0.09890006337844423, 0.882188, 0.337287, 0.207628, 0.09953006966177215, 0.886302, 0.342586, 0.202968, 0.10015991531116752, 0.890341, 0.347957, 0.198286, 0.10078992159449542, 0.894305, 0.353399, 0.193584, 0.10141992787782332, 0.898192, 0.358911, 0.18886, 0.10204977352721871, 0.902003, 0.364492, 0.184116, 0.1026797798105466, 0.905735, 0.37014, 0.17935, 0.10330962545994198, 0.90939, 0.375856, 0.174563, 0.1039396317432699, 0.912966, 0.381636, 0.169755, 0.10456947739266527, 0.916462, 0.387481, 0.164924, 0.10519948367599316, 0.919879, 0.393389, 0.16007, 0.10582948995932105, 0.923215, 0.399359, 0.155193, 0.10645933560871644, 0.92647, 0.405389, 0.150292, 0.10708934189204435, 0.929644, 0.411479, 0.145367, 0.10771918754143972, 0.932737, 0.417627, 0.140417, 0.10834919382476763, 0.935747, 0.423831, 0.13544, 0.108979039474163, 0.938675, 0.430091, 0.130438, 0.1096090457574909, 0.941521, 0.436405, 0.125409, 0.1102390520408188, 0.944285, 0.442772, 0.120354, 0.11086889769021419, 0.946965, 0.449191, 0.115272, 0.11149890397354208, 0.949562, 0.45566, 0.110164, 0.11212874962293745, 0.952075, 0.462178, 0.105031, 0.11275875590626536, 0.954506, 0.468744, 0.099874, 0.11338860155566075, 0.956852, 0.475356, 0.094695, 0.11401860783898864, 0.959114, 0.482014, 0.089499, 0.11464845348838404, 0.961293, 0.488716, 0.084289, 0.11527845977171193, 0.963387, 0.495462, 0.079073, 0.11590846605503982, 0.965397, 0.502249, 0.073859, 0.1165383117044352, 0.967322, 0.509078, 0.068659, 0.11716831798776309, 0.969163, 0.515946, 0.063488, 0.11779816363715849, 0.970919, 0.522853, 0.058367, 0.11842816992048638, 0.97259, 0.529798, 0.053324, 0.11905801556988176, 0.974176, 0.53678, 0.048392, 0.11968802185320968, 0.975677, 0.543798, 0.043618, 0.12031802813653757, 0.977092, 0.55085, 0.03905, 0.12094787378593294, 0.978422, 0.557937, 0.034931, 0.12157788006926083, 0.979666, 0.565057, 0.031409, 0.12220772571865622, 0.980824, 0.572209, 0.028508, 0.12283773200198413, 0.981895, 0.579392, 0.02625, 0.1234675776513795, 0.982881, 0.586606, 0.024661, 0.1240975839347074, 0.983779, 0.593849, 0.02377, 0.12472759021803531, 0.984591, 0.601122, 0.023606, 0.12535743586743067, 0.985315, 0.608422, 0.024202, 0.12598744215075858, 0.985952, 0.61575, 0.025592, 0.12661728780015397, 0.986502, 0.623105, 0.027814, 0.12724729408348187, 0.986964, 0.630485, 0.030908, 0.12787713973287723, 0.987337, 0.63789, 0.034916, 0.12850714601620514, 0.987622, 0.64532, 0.039886, 0.12913715229953304, 0.987819, 0.652773, 0.045581, 0.12976699794892843, 0.987926, 0.66025, 0.05175, 0.1303970042322563, 0.987945, 0.667748, 0.058329, 0.1310268498816517, 0.987874, 0.675267, 0.065257, 0.1316568561649796, 0.987714, 0.682807, 0.072489, 0.132286701814375, 0.987464, 0.690366, 0.07999, 0.1329167080977029, 0.987124, 0.697944, 0.087731, 0.13354671438103077, 0.986694, 0.70554, 0.095694, 0.13417656003042616, 0.986175, 0.713153, 0.103863, 0.13480656631375407, 0.985566, 0.720782, 0.112229, 0.13543641196314946, 0.984865, 0.728427, 0.120785, 0.13606641824647733, 0.984075, 0.736087, 0.129527, 0.13669626389587272, 0.983196, 0.743758, 0.138453, 0.13732627017920063, 0.982228, 0.751442, 0.147565, 0.13795627646252853, 0.981173, 0.759135, 0.156863, 0.1385861221119239, 0.980032, 0.766837, 0.166353, 0.1392161283952518, 0.978806, 0.774545, 0.176037, 0.1398459740446472, 0.977497, 0.782258, 0.185923, 0.1404759803279751, 0.976108, 0.789974, 0.196018, 0.14110582597737045, 0.974638, 0.797692, 0.206332, 0.14173583226069836, 0.973088, 0.805409, 0.216877, 0.14236583854402626, 0.971468, 0.813122, 0.227658, 0.14299568419342165, 0.969783, 0.820825, 0.238686, 0.14362569047674953, 0.968041, 0.828515, 0.249972, 0.14425553612614492, 0.966243, 0.836191, 0.261534, 0.14488554240947282, 0.964394, 0.843848, 0.273391, 0.1455153880588682, 0.962517, 0.851476, 0.285546, 0.1461453943421961, 0.960626, 0.859069, 0.29801, 0.14677523999159148, 0.95872, 0.866624, 0.31082, 0.14740524627491938, 0.956834, 0.874129, 0.323974, 0.1480352525582473, 0.954997, 0.881569, 0.337475, 0.14866509820764268, 0.953215, 0.888942, 0.351369, 0.14929510449097055, 0.951546, 0.896226, 0.365627, 0.14992495014036594, 0.950018, 0.903409, 0.380271, 0.15055495642369385, 0.948683, 0.910473, 0.395289, 0.15118480207308924, 0.947594, 0.917399, 0.410665, 0.1518148083564171, 0.946809, 0.924168, 0.426373, 0.15244481463974502, 0.946392, 0.930761, 0.442367, 0.1530746602891404, 0.946403, 0.937159, 0.458592, 0.1537046665724683, 0.946903, 0.943348, 0.47497, 0.15433451222186367, 0.947937, 0.949318, 0.491426, 0.15496451850519158, 0.949545, 0.955063, 0.50786, 0.15559436415458697, 0.95174, 0.960587, 0.524203, 0.15622437043791487, 0.954529, 0.965896, 0.540361, 0.15685437672124275, 0.957896, 0.971003, 0.556275, 0.15748422237063814, 0.961812, 0.975924, 0.571925, 0.15811422865396604, 0.966249, 0.980678, 0.587206, 0.15874407430336143, 0.971162, 0.985282, 0.602154, 0.1593740805866893, 0.976511, 0.989753, 0.61676, 0.1600039262360847, 0.982257, 0.994109, 0.631017, 0.1606339325194126, 0.988362, 0.998364, 0.644924]
      rho_varLUT.NanColor = [0.0, 1.0, 0.0]
      rho_varLUT.ScalarRangeInitialized = 1.0

      # get opacity transfer function/opacity map for 'rho_var'
      rho_varPWF = GetOpacityTransferFunction('rho_var')
      rho_varPWF.Points = [3.375300039465401e-12, 0.0, 0.5, 0.0, 0.1606339325194126, 1.0, 0.5, 0.0]
      rho_varPWF.ScalarRangeInitialized = 1

      # trace defaults for the display properties.
      inputDisplay.Representation = 'Volume'
      inputDisplay.ColorArrayName = ['POINTS', 'rho_var']
      inputDisplay.LookupTable = rho_varLUT
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
      inputDisplay.ScalarOpacityFunction = rho_varPWF
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
      input_1Display.SetScalarBarVisibility(renderView1, True)

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView2'
      # ----------------------------------------------------------------

      # show data from input_1
      input_1Display_1 = Show(input_1, renderView2)

      # trace defaults for the display properties.
      input_1Display_1.Representation = 'Volume'
      input_1Display_1.ColorArrayName = ['POINTS', 'rho_mean']
      input_1Display_1.LookupTable = rho_meanLUT
      input_1Display_1.OSPRayScaleArray = 'rho_mean'
      input_1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
      input_1Display_1.SelectOrientationVectors = 'None'
      input_1Display_1.ScaleFactor = 0.7000000000000001
      input_1Display_1.SelectScaleArray = 'None'
      input_1Display_1.GlyphType = 'Arrow'
      input_1Display_1.GlyphTableIndexArray = 'None'
      input_1Display_1.GaussianRadius = 0.035
      input_1Display_1.SetScaleArray = ['POINTS', 'rho_mean']
      input_1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
      input_1Display_1.OpacityArray = ['POINTS', 'rho_mean']
      input_1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
      input_1Display_1.DataAxesGrid = 'GridAxesRepresentation'
      input_1Display_1.SelectionCellLabelFontFile = ''
      input_1Display_1.SelectionPointLabelFontFile = ''
      input_1Display_1.PolarAxes = 'PolarAxesRepresentation'
      input_1Display_1.ScalarOpacityUnitDistance = 1.7320508075688772
      input_1Display_1.ScalarOpacityFunction = rho_meanPWF
      input_1Display_1.Slice = 3

      # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
      input_1Display_1.DataAxesGrid.XTitleFontFile = ''
      input_1Display_1.DataAxesGrid.YTitleFontFile = ''
      input_1Display_1.DataAxesGrid.ZTitleFontFile = ''
      input_1Display_1.DataAxesGrid.XLabelFontFile = ''
      input_1Display_1.DataAxesGrid.YLabelFontFile = ''
      input_1Display_1.DataAxesGrid.ZLabelFontFile = ''

      # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
      input_1Display_1.PolarAxes.PolarAxisTitleFontFile = ''
      input_1Display_1.PolarAxes.PolarAxisLabelFontFile = ''
      input_1Display_1.PolarAxes.LastRadialAxisTextFontFile = ''
      input_1Display_1.PolarAxes.SecondaryRadialAxesTextFontFile = ''

      # setup the color legend parameters for each legend in this view

      # get color legend/bar for rho_meanLUT in view renderView2
      rho_meanLUTColorBar_1 = GetScalarBar(rho_meanLUT, renderView2)
      rho_meanLUTColorBar_1.Title = 'rho_mean'
      rho_meanLUTColorBar_1.ComponentTitle = ''
      rho_meanLUTColorBar_1.TitleFontFile = ''
      rho_meanLUTColorBar_1.LabelFontFile = ''

      # set color bar visibility
      rho_meanLUTColorBar_1.Visibility = 1

      # show color legend
      input_1Display_1.SetScalarBarVisibility(renderView2, True)

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView3'
      # ----------------------------------------------------------------

      # show data from input_1
      input_1Display_2 = Show(input_1, renderView3)

      # trace defaults for the display properties.
      input_1Display_2.Representation = 'Volume'
      input_1Display_2.ColorArrayName = ['POINTS', 'rho_var']
      input_1Display_2.LookupTable = rho_varLUT
      input_1Display_2.OSPRayScaleArray = 'rho_mean'
      input_1Display_2.OSPRayScaleFunction = 'PiecewiseFunction'
      input_1Display_2.SelectOrientationVectors = 'None'
      input_1Display_2.ScaleFactor = 0.7000000000000001
      input_1Display_2.SelectScaleArray = 'None'
      input_1Display_2.GlyphType = 'Arrow'
      input_1Display_2.GlyphTableIndexArray = 'None'
      input_1Display_2.GaussianRadius = 0.035
      input_1Display_2.SetScaleArray = ['POINTS', 'rho_mean']
      input_1Display_2.ScaleTransferFunction = 'PiecewiseFunction'
      input_1Display_2.OpacityArray = ['POINTS', 'rho_mean']
      input_1Display_2.OpacityTransferFunction = 'PiecewiseFunction'
      input_1Display_2.DataAxesGrid = 'GridAxesRepresentation'
      input_1Display_2.SelectionCellLabelFontFile = ''
      input_1Display_2.SelectionPointLabelFontFile = ''
      input_1Display_2.PolarAxes = 'PolarAxesRepresentation'
      input_1Display_2.ScalarOpacityUnitDistance = 1.7320508075688772
      input_1Display_2.ScalarOpacityFunction = rho_varPWF
      input_1Display_2.Slice = 3

      # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
      input_1Display_2.DataAxesGrid.XTitleFontFile = ''
      input_1Display_2.DataAxesGrid.YTitleFontFile = ''
      input_1Display_2.DataAxesGrid.ZTitleFontFile = ''
      input_1Display_2.DataAxesGrid.XLabelFontFile = ''
      input_1Display_2.DataAxesGrid.YLabelFontFile = ''
      input_1Display_2.DataAxesGrid.ZLabelFontFile = ''

      # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
      input_1Display_2.PolarAxes.PolarAxisTitleFontFile = ''
      input_1Display_2.PolarAxes.PolarAxisLabelFontFile = ''
      input_1Display_2.PolarAxes.LastRadialAxisTextFontFile = ''
      input_1Display_2.PolarAxes.SecondaryRadialAxesTextFontFile = ''

      # setup the color legend parameters for each legend in this view

      # get color legend/bar for rho_varLUT in view renderView3
      rho_varLUTColorBar = GetScalarBar(rho_varLUT, renderView3)
      rho_varLUTColorBar.Title = 'rho_var'
      rho_varLUTColorBar.ComponentTitle = ''
      rho_varLUTColorBar.TitleFontFile = ''
      rho_varLUTColorBar.LabelFontFile = ''

      # set color bar visibility
      rho_varLUTColorBar.Visibility = 1

      # show color legend
      input_1Display_2.SetScalarBarVisibility(renderView3, True)

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
  freqs = {'input': [1, 1, 1, 1, 1]}
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
