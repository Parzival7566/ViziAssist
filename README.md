# ViziAssist - Your Sixth Sense
## Problem 
A survey on vision impediments in the population of India found that nearly **40 million people** are visually impaired. People with vision defects are unable to confidently set out on the road without the presence of smart guidance softwares to assist them while driving. This problem is further accentuated by the fact that most cars on the road today are not smart cars and fundamentally lack such aforementioned technologies. Thus there exists a gap in the market for a product that assists people with vision impediments in driving , irrespective of the type of car they own.
## Solution
ViziAssist, a smart attachment device that uses cameras to detect objects/hurdles in the path of the automobile. This project is different than the existing technologies for a few reasons; it contains an on-board GPU that does extremely fast, real-time processing and the GPU will be trained through machine learning techniques for efficient obstacle detection. This will prove to be a valuable asset in the automation of the automobile sector and can help people with a minor extent of vision defects to drive safely on the road.


Below, is the **NVIDIA Jetson Nano**; the GPU used for training, testing and validating the data.
<img src="https://github.com/Parzival7566/ViziAssist/blob/main/data/Jetson_Nano.jpg" align="center" width="500" height="375">
## How it Works
For this project, imprtant data, lbraries and overall steup of the Jetson Nano can be obtained from the [jetson-inference repository](https://github.com/dusty-nv/jetson-inference), created by NVIDIA. 
The project is essentially an Object Detection, Computer Vision Problem. So, for this purpose, the **MobileNet-SSD-v2** model, pretrained on 91 classes of the **MS-COCO** Dataset, will be used.

<img src="https://pytorch.org/assets/images/ssd_diagram.png" align="center" width="600" height="300">

All of files and directories that we used in the project have been uploaded to this Repository
Primarily, the detections happen through the **detection.py** script.

Also added a script that can check the temperature of the CPU and GPU at all time.
## Alpha Testing
Below is a brief look at the algorithm doing real-time object detection based on data obtained from the roads of [Chandigarh City](https://sites.google.com/view/ird-dataset/home)

![Gif](https://github.com/Parzival7566/ViziAssist/blob/main/data/ezgif.com-gif-maker%20(2).gif)

The algorithm has also been tested on the same dataset using the **cityscapes image segmentation dataset**

![Gif](https://github.com/Parzival7566/ViziAssist/blob/main/data/ezgif.com-gif-maker%20(1).gif)

And using the **monodepth cityscapes dataset**

![Gif](https://github.com/Parzival7566/ViziAssist/blob/main/data/ezgif.com-gif-maker.gif)

## Current Status

The device has been successfully deployed in an automobile as seen below :

<img src="https://github.com/Parzival7566/ViziAssist/blob/main/data/ViziAssist_Deployment.jpg" align="center" width="500" height="300">

**Update** : The device is currently able to correctly present output through LEDs. The real time result of the algorithm can be seen below : 

![Current_Stage_gif](https://github.com/Parzival7566/ViziAssist/blob/main/data/ViziAssist_pdt.gif)

The device is now in a compact form, with 3D-printed casing : 

<img src="https://github.com/Parzival7566/ViziAssist/blob/main/data/ViziAssist_Final.jpg" align="center" width="300" height="400">

## Implementation Process

**Step 1** : Start by setting up the OS for the Jetson Nano. The process for doing the same can be seen at [Jetson SDK](https://developer.nvidia.com/embedded/jetpack-sdk-462)

**Step 2** : After setting up the device, clone the offcial NVIDIA jetson repository 
```
git clone https://github.com/dusty-nv/jetson-inference
```
**Step 3** : Follow the steps specified in the repository for performing [Object Detection](https://github.com/Parzival7566/jetson-inference-for-viziassist-/blob/master/docs/detectnet-console-2.md)

**Step 4** : In order to perform our object detection, we will be using the MobileNet SSD Inception v2, as mentioned earlier. So, while the process to implement remains the same, we shall be making small changes to the [detectnet.py](https://github.com/Parzival7566/ViziAssist/blob/main/detectnet.py), that is located in the [Jetson Inference](https://github.com/Parzival7566/jetson-inference-for-viziassist-/blob/master/python/examples/my-detection.py)

**Step 5** : To make our device provide real-time output, we attach LEDs to the GPIO pins **11,16,29,31,32** using the appropriate wiring. To use these we will need to run
```
sudo pip3 install Jetson.GPIO
```
**Step 6** : We now attach the raspberry pi camera to the slot and run the detection using 
```
./detectnet.py --network=ssd-mobilenet-v2 --threshold=0.50 csi://0
```
