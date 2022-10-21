import jetson.inference
import jetson.utils

net = jetson.inference.detectNet('ssd-mobilenet-v2', threshold=0.5)
camera = jetson.utils.gstCamera(1920,1080,"csi://0")
display = jetson.utils.glDisplay()

while display.IsOpen():
	img,width,height = camera.CaptureRGBA()
	detections=net.Detect(img,width,height)
	display.RenderOnce(img,width,height)
	display.SetTitle("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
