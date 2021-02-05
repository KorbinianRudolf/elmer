# trace generated using paraview version 5.9.0-RC3

#### import the simple module from the paraview
from paraview.simple import *
import os
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

d = 'E:\\Users\\korbi\\Desktop\\Hiwi_Stelle\\projects\\Stanislav Simulations\\varying inflow_speed'
folders = [os.path.join(d,o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]




for f in folders:
	
	newpath = '{}\\animation'.format(f)
	if not os.path.exists(newpath):
		os.makedirs(newpath)
	
	# create a new 'XML Unstructured Grid Reader'
	case_t0 = XMLUnstructuredGridReader(registrationName='case_t0*', FileName=['{}\\case_t0001.vtu'.format(f), '{}\\case_t0002.vtu'.format(f), '{}\\case_t0003.vtu'.format(f), '{}\\case_t0004.vtu'.format(f), '{}\\case_t0005.vtu'.format(f), '{}\\case_t0006.vtu'.format(f), '{}\\case_t0007.vtu'.format(f), '{}\\case_t0008.vtu'.format(f), '{}\\case_t0009.vtu'.format(f), '{}\\case_t0010.vtu'.format(f), '{}\\case_t0011.vtu'.format(f), '{}\\case_t0012.vtu'.format(f), '{}\\case_t0013.vtu'.format(f), '{}\\case_t0014.vtu'.format(f), '{}\\case_t0015.vtu'.format(f), '{}\\case_t0016.vtu'.format(f), '{}\\case_t0017.vtu'.format(f), '{}\\case_t0018.vtu'.format(f), '{}\\case_t0019.vtu'.format(f), '{}\\case_t0020.vtu'.format(f), '{}\\case_t0021.vtu'.format(f), '{}\\case_t0022.vtu'.format(f), '{}\\case_t0023.vtu'.format(f), '{}\\case_t0024.vtu'.format(f), '{}\\case_t0025.vtu'.format(f), '{}\\case_t0026.vtu'.format(f), '{}\\case_t0027.vtu'.format(f), '{}\\case_t0028.vtu'.format(f), '{}\\case_t0029.vtu'.format(f), '{}\\case_t0030.vtu'.format(f), '{}\\case_t0031.vtu'.format(f), '{}\\case_t0032.vtu'.format(f), '{}\\case_t0033.vtu'.format(f), '{}\\case_t0034.vtu'.format(f), '{}\\case_t0035.vtu'.format(f), '{}\\case_t0036.vtu'.format(f), '{}\\case_t0037.vtu'.format(f), '{}\\case_t0038.vtu'.format(f), '{}\\case_t0039.vtu'.format(f), '{}\\case_t0040.vtu'.format(f), '{}\\case_t0041.vtu'.format(f), '{}\\case_t0042.vtu'.format(f), '{}\\case_t0043.vtu'.format(f), '{}\\case_t0044.vtu'.format(f), '{}\\case_t0045.vtu'.format(f), '{}\\case_t0046.vtu'.format(f), '{}\\case_t0047.vtu'.format(f), '{}\\case_t0048.vtu'.format(f), '{}\\case_t0049.vtu'.format(f), '{}\\case_t0050.vtu'.format(f), '{}\\case_t0051.vtu'.format(f), '{}\\case_t0052.vtu'.format(f), '{}\\case_t0053.vtu'.format(f), '{}\\case_t0054.vtu'.format(f), '{}\\case_t0055.vtu'.format(f), '{}\\case_t0056.vtu'.format(f), '{}\\case_t0057.vtu'.format(f), '{}\\case_t0058.vtu'.format(f), '{}\\case_t0059.vtu'.format(f), '{}\\case_t0060.vtu'.format(f), '{}\\case_t0061.vtu'.format(f), '{}\\case_t0062.vtu'.format(f), '{}\\case_t0063.vtu'.format(f), '{}\\case_t0064.vtu'.format(f), '{}\\case_t0065.vtu'.format(f), '{}\\case_t0066.vtu'.format(f), '{}\\case_t0067.vtu'.format(f), '{}\\case_t0068.vtu'.format(f), '{}\\case_t0069.vtu'.format(f), '{}\\case_t0070.vtu'.format(f), '{}\\case_t0071.vtu'.format(f), '{}\\case_t0072.vtu'.format(f), '{}\\case_t0073.vtu'.format(f), '{}\\case_t0074.vtu'.format(f), '{}\\case_t0075.vtu'.format(f), '{}\\case_t0076.vtu'.format(f), '{}\\case_t0077.vtu'.format(f), '{}\\case_t0078.vtu'.format(f), '{}\\case_t0079.vtu'.format(f), '{}\\case_t0080.vtu'.format(f), '{}\\case_t0081.vtu'.format(f), '{}\\case_t0082.vtu'.format(f), '{}\\case_t0083.vtu'.format(f), '{}\\case_t0084.vtu'.format(f), '{}\\case_t0085.vtu'.format(f), '{}\\case_t0086.vtu'.format(f), '{}\\case_t0087.vtu'.format(f), '{}\\case_t0088.vtu'.format(f), '{}\\case_t0089.vtu'.format(f), '{}\\case_t0090.vtu'.format(f), '{}\\case_t0091.vtu'.format(f), '{}\\case_t0092.vtu'.format(f), '{}\\case_t0093.vtu'.format(f), '{}\\case_t0094.vtu'.format(f), '{}\\case_t0095.vtu'.format(f), '{}\\case_t0096.vtu'.format(f), '{}\\case_t0097.vtu'.format(f), '{}\\case_t0098.vtu'.format(f), '{}\\case_t0099.vtu'.format(f), '{}\\case_t0100.vtu'.format(f), '{}\\case_t0101.vtu'.format(f), '{}\\case_t0102.vtu'.format(f), '{}\\case_t0103.vtu'.format(f), '{}\\case_t0104.vtu'.format(f), '{}\\case_t0105.vtu'.format(f), '{}\\case_t0106.vtu'.format(f), '{}\\case_t0107.vtu'.format(f), '{}\\case_t0108.vtu'.format(f), '{}\\case_t0109.vtu'.format(f), '{}\\case_t0110.vtu'.format(f), '{}\\case_t0111.vtu'.format(f), '{}\\case_t0112.vtu'.format(f), '{}\\case_t0113.vtu'.format(f), '{}\\case_t0114.vtu'.format(f), '{}\\case_t0115.vtu'.format(f), '{}\\case_t0116.vtu'.format(f), '{}\\case_t0117.vtu'.format(f), '{}\\case_t0118.vtu'.format(f), '{}\\case_t0119.vtu'.format(f), '{}\\case_t0120.vtu'.format(f), '{}\\case_t0121.vtu'.format(f), '{}\\case_t0122.vtu'.format(f), '{}\\case_t0123.vtu'.format(f), '{}\\case_t0124.vtu'.format(f), '{}\\case_t0125.vtu'.format(f), '{}\\case_t0126.vtu'.format(f), '{}\\case_t0127.vtu'.format(f), '{}\\case_t0128.vtu'.format(f), '{}\\case_t0129.vtu'.format(f), '{}\\case_t0130.vtu'.format(f), '{}\\case_t0131.vtu'.format(f), '{}\\case_t0132.vtu'.format(f), '{}\\case_t0133.vtu'.format(f), '{}\\case_t0134.vtu'.format(f), '{}\\case_t0135.vtu'.format(f), '{}\\case_t0136.vtu'.format(f), '{}\\case_t0137.vtu'.format(f), '{}\\case_t0138.vtu'.format(f), '{}\\case_t0139.vtu'.format(f), '{}\\case_t0140.vtu'.format(f), '{}\\case_t0141.vtu'.format(f), '{}\\case_t0142.vtu'.format(f), '{}\\case_t0143.vtu'.format(f), '{}\\case_t0144.vtu'.format(f), '{}\\case_t0145.vtu'.format(f), '{}\\case_t0146.vtu'.format(f), '{}\\case_t0147.vtu'.format(f), '{}\\case_t0148.vtu'.format(f), '{}\\case_t0149.vtu'.format(f), '{}\\case_t0150.vtu'.format(f), '{}\\case_t0151.vtu'.format(f), '{}\\case_t0152.vtu'.format(f), '{}\\case_t0153.vtu'.format(f), '{}\\case_t0154.vtu'.format(f), '{}\\case_t0155.vtu'.format(f), '{}\\case_t0156.vtu'.format(f), '{}\\case_t0157.vtu'.format(f), '{}\\case_t0158.vtu'.format(f), '{}\\case_t0159.vtu'.format(f), '{}\\case_t0160.vtu'.format(f), '{}\\case_t0161.vtu'.format(f), '{}\\case_t0162.vtu'.format(f), '{}\\case_t0163.vtu'.format(f), '{}\\case_t0164.vtu'.format(f), '{}\\case_t0165.vtu'.format(f), '{}\\case_t0166.vtu'.format(f), '{}\\case_t0167.vtu'.format(f), '{}\\case_t0168.vtu'.format(f), '{}\\case_t0169.vtu'.format(f), '{}\\case_t0170.vtu'.format(f), '{}\\case_t0171.vtu'.format(f), '{}\\case_t0172.vtu'.format(f), '{}\\case_t0173.vtu'.format(f), '{}\\case_t0174.vtu'.format(f), '{}\\case_t0175.vtu'.format(f), '{}\\case_t0176.vtu'.format(f), '{}\\case_t0177.vtu'.format(f), '{}\\case_t0178.vtu'.format(f), '{}\\case_t0179.vtu'.format(f), '{}\\case_t0180.vtu'.format(f), '{}\\case_t0181.vtu'.format(f), '{}\\case_t0182.vtu'.format(f), '{}\\case_t0183.vtu'.format(f), '{}\\case_t0184.vtu'.format(f), '{}\\case_t0185.vtu'.format(f), '{}\\case_t0186.vtu'.format(f), '{}\\case_t0187.vtu'.format(f), '{}\\case_t0188.vtu'.format(f), '{}\\case_t0189.vtu'.format(f), '{}\\case_t0190.vtu'.format(f), '{}\\case_t0191.vtu'.format(f), '{}\\case_t0192.vtu'.format(f), '{}\\case_t0193.vtu'.format(f), '{}\\case_t0194.vtu'.format(f), '{}\\case_t0195.vtu'.format(f), '{}\\case_t0196.vtu'.format(f), '{}\\case_t0197.vtu'.format(f), '{}\\case_t0198.vtu'.format(f), '{}\\case_t0199.vtu'.format(f), '{}\\case_t0200.vtu'.format(f), '{}\\case_t0201.vtu'.format(f), '{}\\case_t0202.vtu'.format(f), '{}\\case_t0203.vtu'.format(f), '{}\\case_t0204.vtu'.format(f), '{}\\case_t0205.vtu'.format(f), '{}\\case_t0206.vtu'.format(f), '{}\\case_t0207.vtu'.format(f), '{}\\case_t0208.vtu'.format(f), '{}\\case_t0209.vtu'.format(f), '{}\\case_t0210.vtu'.format(f), '{}\\case_t0211.vtu'.format(f), '{}\\case_t0212.vtu'.format(f), '{}\\case_t0213.vtu'.format(f), '{}\\case_t0214.vtu'.format(f), '{}\\case_t0215.vtu'.format(f), '{}\\case_t0216.vtu'.format(f), '{}\\case_t0217.vtu'.format(f), '{}\\case_t0218.vtu'.format(f), '{}\\case_t0219.vtu'.format(f), '{}\\case_t0220.vtu'.format(f), '{}\\case_t0221.vtu'.format(f), '{}\\case_t0222.vtu'.format(f), '{}\\case_t0223.vtu'.format(f), '{}\\case_t0224.vtu'.format(f), '{}\\case_t0225.vtu'.format(f), '{}\\case_t0226.vtu'.format(f), '{}\\case_t0227.vtu'.format(f), '{}\\case_t0228.vtu'.format(f), '{}\\case_t0229.vtu'.format(f), '{}\\case_t0230.vtu'.format(f), '{}\\case_t0231.vtu'.format(f), '{}\\case_t0232.vtu'.format(f), '{}\\case_t0233.vtu'.format(f), '{}\\case_t0234.vtu'.format(f), '{}\\case_t0235.vtu'.format(f), '{}\\case_t0236.vtu'.format(f), '{}\\case_t0237.vtu'.format(f), '{}\\case_t0238.vtu'.format(f), '{}\\case_t0239.vtu'.format(f), '{}\\case_t0240.vtu'.format(f), '{}\\case_t0241.vtu'.format(f), '{}\\case_t0242.vtu'.format(f), '{}\\case_t0243.vtu'.format(f), '{}\\case_t0244.vtu'.format(f), '{}\\case_t0245.vtu'.format(f), '{}\\case_t0246.vtu'.format(f), '{}\\case_t0247.vtu'.format(f), '{}\\case_t0248.vtu'.format(f), '{}\\case_t0249.vtu'.format(f), '{}\\case_t0250.vtu'.format(f), '{}\\case_t0251.vtu'.format(f), '{}\\case_t0252.vtu'.format(f), '{}\\case_t0253.vtu'.format(f), '{}\\case_t0254.vtu'.format(f), '{}\\case_t0255.vtu'.format(f), '{}\\case_t0256.vtu'.format(f), '{}\\case_t0257.vtu'.format(f), '{}\\case_t0258.vtu'.format(f), '{}\\case_t0259.vtu'.format(f), '{}\\case_t0260.vtu'.format(f), '{}\\case_t0261.vtu'.format(f), '{}\\case_t0262.vtu'.format(f), '{}\\case_t0263.vtu'.format(f), '{}\\case_t0264.vtu'.format(f), '{}\\case_t0265.vtu'.format(f), '{}\\case_t0266.vtu'.format(f), '{}\\case_t0267.vtu'.format(f), '{}\\case_t0268.vtu'.format(f), '{}\\case_t0269.vtu'.format(f), '{}\\case_t0270.vtu'.format(f), '{}\\case_t0271.vtu'.format(f), '{}\\case_t0272.vtu'.format(f), '{}\\case_t0273.vtu'.format(f), '{}\\case_t0274.vtu'.format(f), '{}\\case_t0275.vtu'.format(f), '{}\\case_t0276.vtu'.format(f), '{}\\case_t0277.vtu'.format(f), '{}\\case_t0278.vtu'.format(f), '{}\\case_t0279.vtu'.format(f), '{}\\case_t0280.vtu'.format(f), '{}\\case_t0281.vtu'.format(f), '{}\\case_t0282.vtu'.format(f), '{}\\case_t0283.vtu'.format(f), '{}\\case_t0284.vtu'.format(f), '{}\\case_t0285.vtu'.format(f), '{}\\case_t0286.vtu'.format(f), '{}\\case_t0287.vtu'.format(f), '{}\\case_t0288.vtu'.format(f), '{}\\case_t0289.vtu'.format(f), '{}\\case_t0290.vtu'.format(f), '{}\\case_t0291.vtu'.format(f), '{}\\case_t0292.vtu'.format(f), '{}\\case_t0293.vtu'.format(f), '{}\\case_t0294.vtu'.format(f), '{}\\case_t0295.vtu'.format(f), '{}\\case_t0296.vtu'.format(f), '{}\\case_t0297.vtu'.format(f), '{}\\case_t0298.vtu'.format(f), '{}\\case_t0299.vtu'.format(f), '{}\\case_t0300.vtu'.format(f), '{}\\case_t0301.vtu'.format(f), '{}\\case_t0302.vtu'.format(f), '{}\\case_t0303.vtu'.format(f), '{}\\case_t0304.vtu'.format(f), '{}\\case_t0305.vtu'.format(f), '{}\\case_t0306.vtu'.format(f), '{}\\case_t0307.vtu'.format(f), '{}\\case_t0308.vtu'.format(f), '{}\\case_t0309.vtu'.format(f), '{}\\case_t0310.vtu'.format(f), '{}\\case_t0311.vtu'.format(f), '{}\\case_t0312.vtu'.format(f), '{}\\case_t0313.vtu'.format(f), '{}\\case_t0314.vtu'.format(f), '{}\\case_t0315.vtu'.format(f), '{}\\case_t0316.vtu'.format(f), '{}\\case_t0317.vtu'.format(f), '{}\\case_t0318.vtu'.format(f), '{}\\case_t0319.vtu'.format(f), '{}\\case_t0320.vtu'.format(f), '{}\\case_t0321.vtu'.format(f), '{}\\case_t0322.vtu'.format(f), '{}\\case_t0323.vtu'.format(f), '{}\\case_t0324.vtu'.format(f), '{}\\case_t0325.vtu'.format(f), '{}\\case_t0326.vtu'.format(f), '{}\\case_t0327.vtu'.format(f), '{}\\case_t0328.vtu'.format(f), '{}\\case_t0329.vtu'.format(f), '{}\\case_t0330.vtu'.format(f), '{}\\case_t0331.vtu'.format(f), '{}\\case_t0332.vtu'.format(f), '{}\\case_t0333.vtu'.format(f), '{}\\case_t0334.vtu'.format(f), '{}\\case_t0335.vtu'.format(f)])
	case_t0.CellArrayStatus = ['GeometryIds']
	case_t0.PointArrayStatus = ['pressure', 'velocity']

	# get animation scene
	animationScene1 = GetAnimationScene()

	# update animation scene based on data timesteps
	animationScene1.UpdateAnimationUsingDataTimeSteps()

	# Properties modified on case_t0
	case_t0.TimeArray = 'None'

	# get active view
	renderView1 = GetActiveViewOrCreate('RenderView')

	# show data in view
	case_t0Display = Show(case_t0, renderView1, 'UnstructuredGridRepresentation')

	# trace defaults for the display properties.
	case_t0Display.Representation = 'Surface'
	case_t0Display.ColorArrayName = [None, '']
	case_t0Display.SelectTCoordArray = 'None'
	case_t0Display.SelectNormalArray = 'None'
	case_t0Display.SelectTangentArray = 'None'
	case_t0Display.OSPRayScaleArray = 'pressure'
	case_t0Display.OSPRayScaleFunction = 'PiecewiseFunction'
	case_t0Display.SelectOrientationVectors = 'None'
	case_t0Display.ScaleFactor = 1.06
	case_t0Display.SelectScaleArray = 'None'
	case_t0Display.GlyphType = 'Arrow'
	case_t0Display.GlyphTableIndexArray = 'None'
	case_t0Display.GaussianRadius = 0.053
	case_t0Display.SetScaleArray = ['POINTS', 'pressure']
	case_t0Display.ScaleTransferFunction = 'PiecewiseFunction'
	case_t0Display.OpacityArray = ['POINTS', 'pressure']
	case_t0Display.OpacityTransferFunction = 'PiecewiseFunction'
	case_t0Display.DataAxesGrid = 'GridAxesRepresentation'
	case_t0Display.PolarAxes = 'PolarAxesRepresentation'
	case_t0Display.ScalarOpacityUnitDistance = 0.5683734564645577
	case_t0Display.OpacityArrayName = ['POINTS', 'pressure']

	# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
	case_t0Display.ScaleTransferFunction.Points = [4.3925555865654745e-05, 0.0, 0.5, 0.0, 89.73824620136891, 1.0, 0.5, 0.0]

	# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
	case_t0Display.OpacityTransferFunction.Points = [4.3925555865654745e-05, 0.0, 0.5, 0.0, 89.73824620136891, 1.0, 0.5, 0.0]

	# reset view to fit data
	renderView1.ResetCamera()

	#changing interaction mode based on data extents
	renderView1.InteractionMode = '2D'
	renderView1.CameraPosition = [5.3, 1.35, 10000.0]
	renderView1.CameraFocalPoint = [5.3, 1.35, 0.0]

	# get the material library
	materialLibrary1 = GetMaterialLibrary()

	# update the view to ensure updated data information
	renderView1.Update()

	# set scalar coloring
	ColorBy(case_t0Display, ('POINTS', 'velocity', 'Magnitude'))

	# rescale color and/or opacity maps used to include current data range
	case_t0Display.RescaleTransferFunctionToDataRange(True, False)

	# show color bar/color legend
	case_t0Display.SetScalarBarVisibility(renderView1, False)

	# get color transfer function/color map for 'velocity'
	velocityLUT = GetColorTransferFunction('velocity')

	# get opacity transfer function/opacity map for 'velocity'
	velocityPWF = GetOpacityTransferFunction('velocity')

	# set scalar coloring
	ColorBy(case_t0Display, ('POINTS', 'velocity', 'X'))

	# rescale color and/or opacity maps used to exactly fit the current data range
	case_t0Display.RescaleTransferFunctionToDataRange(False, False)

	# Update a scalar bar component title.
	UpdateScalarBarsComponentTitle(velocityLUT, case_t0Display)

	# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
	velocityLUT.ApplyPreset('Grayscale', True)

	# Hide orientation axes
	renderView1.OrientationAxesVisibility = 0

	# get layout
	layout1 = GetLayout()

	# layout/tab size in pixels
	layout1.SetSize(1114, 552)

	# current camera placement for renderView1
	renderView1.InteractionMode = '2D'
	renderView1.CameraPosition = [5.3, 1.35, 10000.0]
	renderView1.CameraFocalPoint = [5.3, 1.35, 0.0]
	renderView1.CameraParallelScale = 5.469232121605372

	# save animation
	SaveAnimation('{}\\animation\\cVX.png'.format(f), renderView1, ImageResolution=[1114, 552],
		TransparentBackground=1,
		FrameWindow=[0, 334])

		# set scalar coloring
	ColorBy(case_t0Display, ('POINTS', 'velocity', 'Y'))

	# rescale color and/or opacity maps used to exactly fit the current data range
	case_t0Display.RescaleTransferFunctionToDataRange(False, False)
	
		# save animation
	SaveAnimation('{}\\animation\\cVY.png'.format(f), renderView1, ImageResolution=[1114, 552],
		TransparentBackground=1,
		FrameWindow=[0, 334])

	#================================================================
	# addendum: following script captures some of the application
	# state to faithfully reproduce the visualization during playback
	#================================================================

	#--------------------------------
	# saving layout sizes for layouts

	# layout/tab size in pixels
	layout1.SetSize(1114, 552)

	#-----------------------------------
	# saving camera placements for views

	# current camera placement for renderView1
	renderView1.InteractionMode = '2D'
	renderView1.CameraPosition = [5.3, 1.35, 10000.0]
	renderView1.CameraFocalPoint = [5.3, 1.35, 0.0]
	renderView1.CameraParallelScale = 5.469232121605372

	#--------------------------------------------
	# uncomment the following to render all views
	# RenderAllViews()
	# alternatively, if you want to write images, you can use SaveScreenshot(...).