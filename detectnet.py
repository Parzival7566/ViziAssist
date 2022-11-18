#!/usr/bin/env python3
import sys
import argparse
import Jetson.GPIO as GPIO

from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput, logUsage

# parse the command line
parser = argparse.ArgumentParser(description="Locate objects in a live camera stream using an object detection DNN.", 
                                 formatter_class=argparse.RawTextHelpFormatter, 
                                 epilog=detectNet.Usage() + videoSource.Usage() + videoOutput.Usage() + logUsage())

parser.add_argument("input_URI", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output_URI", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="ssd-mobilenet-v2", help="pre-trained model to load (see below for options)")
parser.add_argument("--overlay", type=str, default="box,labels,conf", help="detection overlay flags (e.g. --overlay=box,labels,conf)\nvalid combinations are:  'box', 'labels', 'conf', 'none'")
parser.add_argument("--threshold", type=float, default=0.5, help="minimum detection threshold to use") 

is_headless = ["--headless"] if sys.argv[0].find('console.py') != -1 else [""]

GPIO.setmode(GPIO.BOARD)

# Pin Definition
led_pin_1 = 11
led_pin_2 = 16
led_pin_3 = 29
led_pin_4 = 31
led_pin_5 = 32
#33,37 are also high ampereage

# Set up the GPIO channel 
GPIO.setup(led_pin_1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led_pin_2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led_pin_3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led_pin_4, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(led_pin_5, GPIO.OUT, initial=GPIO.LOW) 
 

try:
	args = parser.parse_known_args()[0]
except:
	print("")
	parser.print_help()
	sys.exit(0)

# create video sources and outputs
input = videoSource(args.input_URI, argv=sys.argv)
output = videoOutput(args.output_URI, argv=sys.argv+is_headless)
	
# load the object detection network
net = detectNet(args.network, sys.argv, args.threshold)

# note: to hard-code the paths to load a model, the following API can be used:
#
# net = detectNet(model="model/ssd-mobilenet.onnx", labels="model/labels.txt", 
#                 input_blob="input_0", output_cvg="scores", output_bbox="boxes", 
#                 threshold=args.threshold)

# process frames until the user exits
while True:
	# capture the next image
	img = input.Capture()

	# detect objects in the image (with overlay)
	detections = net.Detect(img, overlay=args.overlay)

	# print the detections
	print("detected {:d} objects in image".format(len(detections)))
	for detection in detections:
		print(detection)
		class_name = net.GetClassDesc(detection.ClassID)
		GPIO.output(led_pin_1, GPIO.LOW)
		GPIO.output(led_pin_2, GPIO.LOW)
		GPIO.output(led_pin_3, GPIO.LOW)
		GPIO.output(led_pin_4, GPIO.LOW)
		GPIO.output(led_pin_5, GPIO.LOW)
		if class_name == "car":
			GPIO.output(led_pin_1, GPIO.HIGH)
			continue
		if class_name == "person":
			GPIO.output(led_pin_2, GPIO.HIGH)
			continue
		if class_name == "motorcycle":
			GPIO.output(led_pin_3, GPIO.HIGH)
			continue
		if class_name == "truck":
			GPIO.output(led_pin_4, GPIO.HIGH)
			continue
		if class_name == "bus":
			GPIO.output(led_pin_5, GPIO.HIGH)
			continue
		else:
			GPIO.output(led_pin_1, GPIO.LOW)
			GPIO.output(led_pin_2, GPIO.LOW)
			GPIO.output(led_pin_3, GPIO.LOW)
			GPIO.output(led_pin_4, GPIO.LOW)
			GPIO.output(led_pin_5, GPIO.LOW)


	# render the image
	output.Render(img)

	# update the title bar
	output.SetStatus("{:s} | Network {:.0f} FPS".format(args.network, net.GetNetworkFPS()))

	# print out performance info
	net.PrintProfilerTimes()

	# exit on input/output EOS
	if not input.IsStreaming() or not output.IsStreaming():
		break

GPIO.cleanup()
