#!/usr/bin/env python3

from jetson_inference import imageNet
from jetson_utils import loadImage

import argparse


# parse the command line
parser = argparse.ArgumentParser()

parser.add_argument("filename", type=str, help="filename of the image to process")
parser.add_argument("--network", type=str, default="googlenet", help="model to use, can be:  googlenet, resnet-18, ect.")

args = parser.parse_args()

# load an image (into shared CPU/GPU memory)
img = loadImage(args.filename)

# load the recognition network
net = imageNet(args.network)

# classify the image
class_idx, confidence = net.Classify(img)

# find the object description
class_desc = net.GetClassDesc(class_idx)

# print out the result
print("image is recognized as '{:s}' (class #{:d}) with {:f}% confidence".format(class_desc, class_idx, confidence * 100))

