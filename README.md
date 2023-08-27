# Introduction
The programs were developed and tested on a Raspberry Pi 3 module, focusing on two main concepts. The initial phase involved shape recognition, analyzing video frames to detect objects. This knowledge was then applied to the line-following robot concept, using computer vision analysis to control the robot's movements.

# Line following

![image](https://github.com/Arfan0612/OpenCV-With-Robot-Car/assets/94776851/a941cc34-4ea1-41fb-a8b6-f237edf8eb7e)

It pre-processing processs follows the florchart below:
![image](https://github.com/Arfan0612/OpenCV-With-Robot-Car/assets/94776851/aff4b62e-5a28-4ad5-9cb0-8a3d37e23728)

An example of an image undergoing the pre-processing is shown below:

![image](https://github.com/Arfan0612/OpenCV-With-Robot-Car/assets/94776851/15246c96-957a-4df1-838d-0e46eda2f6d3)

## Opening operation
This operation performs erosion on the binary image, then followed by dilation. This is to further remove the background noise.

![image](https://github.com/Arfan0612/OpenCV-With-Robot-Car/assets/94776851/76597e58-4fc0-4748-85ce-e0c9d0767841)

# Shape recognition
![image](https://github.com/Arfan0612/OpenCV-With-Robot-Car/assets/94776851/ca188ac2-b412-4f2d-a3b4-022ed6f14b1b)

Its pre-processing process follows the flowchart below:
![image](https://github.com/Arfan0612/OpenCV-With-Robot-Car/assets/94776851/6462b8ed-82d8-486c-bc3d-e4f8c4f78cff)


