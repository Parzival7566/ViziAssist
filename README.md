# ViziAssist - Your Sixth Sense
## Problem 
A survey on vision impediments in the population of India found that nearly **40 million people** are visually impaired. People with vision defects are unable to confidently set out on the road without the presence of smart guidance softwares to assist them while driving. This problem is further accentuated by the fact that most cars on the road today are not smart cars and fundamentally lack such aforementioned technologies. Thus there exists a gap in the market for a product that assists people with vision impediments in driving , irrespective of the type of car they own.
## Solution
ViziAssist, a smart attachment device that uses cameras to detect objects/hurdles in the path of the automobile. This project is different than the existing technologies for a few reasons; it contains an on-board GPU that does extremely fast, real-time processing and the GPU will be trained through machine learning techniques for efficient obstacle detection. This will prove to be a valuable asset in the automation of the automobile sector and can help people with a minor extent of vision defects to drive safely on the road.


Below, is the **NVIDIA Jetson Nano**; the GPU that we will be using for training, testing and validating our data.
![Jetson Nano](https://developer.nvidia.com/sites/default/files/akamai/embedded/images/jetsonNano/JetsonNano-DevKit_Front-Top_Right_trimmed.jpg)
## How it Works
For this project, we have made use of the jetson-inference repository, created by NVIDIA.
Our project is essentially an Object Detection, Computer Vision Problem. So, for this purpose, we have made use of the **MobileNet-SSD-v2**, pretrained on 91 classes of the **MS-COCO** Dataset.

![Mobilenet-ssd-v2](https://pytorch.org/assets/images/ssd_diagram.png)

We have uploaded all of our files and directories that we used in our project to this Repository
Primarily, our detections happen through the **detection.py** script in the build/aarch/bin directory

