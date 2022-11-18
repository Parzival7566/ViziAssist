#!/bin/sh

echo "Welcome to ViziAssist - Your Sixth Sense!"
echo "Runnng the Detectnet program"
cd jetson-inference/build/aarch64/bin/
./detectnet.py --network=ssd-inception-v2 csi://0 irl_test_1.mp4
echo "Detectnet execution ended!"

