# ViziAssist - Your Sixth Sense
## Problem 
A survey on vision impediments in the population of India found that nearly **40 million people** are visually impaired. People with vision defects are unable to confidently set out on the road without the presence of smart guidance softwares to assist them while driving. This problem is further accentuated by the fact that most cars on the road today are not smart cars and fundamentally lack such aforementioned technologies. Thus there exists a gap in the market for a product that assists people with vision impediments in driving , irrespective of the type of car they own.
## Solution
ViziAssist, a smart attachment device that uses cameras to detect objects/hurdles in the path of the automobile. This project is different than the existing technologies for a few reasons; it contains an on-board GPU that does extremely fast, real-time processing and the GPU will be trained through machine learning techniques for efficient obstacle detection. This will prove to be a valuable asset in the automation of the automobile sector and can help people with a minor extent of vision defects to drive safely on the road.


Below, is the **NVIDIA Jetson Nano**; the GPU used for training, testing and validating the data.
![Jetson Nano](https://developer.nvidia.com/sites/default/files/akamai/embedded/images/jetsonNano/JetsonNano-DevKit_Front-Top_Right_trimmed.jpg)
## How it Works
For this project, imprtant data, lbraries and overall steup of the Jetson Nano can be obtained from the jetson-inference repository(https://github.com/dusty-nv/jetson-inference), created by NVIDIA. 
The project is essentially an Object Detection, Computer Vision Problem. So, for this purpose, the **MobileNet-SSD-v2** model, pretrained on 91 classes of the **MS-COCO** Dataset, will be used.

![Mobilenet-ssd-v2](https://pytorch.org/assets/images/ssd_diagram.png)

All of files and directories that we used in the project have been uploaded to this Repository
Primarily, the detections happen through the **detection.py** script.

Also added a script that can check the temperature of the CPU and GPU at all time.
## Alpha Testing
Below is a brief look at the algorithm doing real-time object detection based on data obtained from the roads of Chandigarh City (obtained from : https://sites.google.com/view/ird-dataset/home)

![Gif](https://github.com/Parzival7566/ViziAssist/blob/main/data/ezgif.com-gif-maker%20(2).gif)

The algorithm has also been tested on the same dataset using the **cityscapes image segmentation dataset**

![Gif](https://github.com/Parzival7566/ViziAssist/blob/main/data/ezgif.com-gif-maker%20(1).gif)

And using the **monodepth cityscapes dataset**

![Gif](https://github.com/Parzival7566/ViziAssist/blob/main/data/ezgif.com-gif-maker.gif)

## Current Status

Currently, the product is still in the developmental stage. In the near future, the product will be made more compact and aesthetic, so as to seamlessly blend with the interiors of any automobile.

**Update** : The device is currently able to correctly present outut through LEDs

![Current_Stage](https://github.com/Parzival7566/ViziAssist/blob/main/data/IMG_20221115_224935.jpg)
