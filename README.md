# EC7212-Computer-Vision-and-Image-Processing-Take-Home-Assignment-1

#### Name     : Sundarasekara G.O.
#### Reg.No.  : EG/2020/3943

---

## Overview
This repository contains Python implementations for some image processing operations, related to the Take Home Assignment 1 for EC7212 – Computer Vision and Image Processing module at Faculty of Engineering, University of Ruhuna.

## ✅ Tasks

### 🔹 Task 1: Intensity Level Reduction
The program reduces the number of intensity levels in an image from 256 to 2, in integer powers of 2. The desired number of intensity levels are specified(input) by the user. This is achieved by dividing pixel values into discrete intervals and mapping them to their average level.

### 🔹 Task 2: Spatial Averaging
The program loads an image and then performs a simple spatial 3x3 average of image pixels. The process is repeated for a 10x10 neighborhood and again for a 20x20 neighborhood. This is achieved using OpenCV’s cv2.blur() function to smooth the image.

### 🔹 Task 3: Image Rotation
The program rotates an image by 45 and 90 degrees. This is done by using OpenCV’s affine transform and rotate functions.

### 🔹 Task 4: Block Averaging for Resolution Reduction
For every 3×3 block of the image (without overlapping), this program replaces all the corresponding 9 pixels by their average. This operation simulates reducing the image spatial resolution. Same procedure is repeated for 5×5 blocks and 7×7 blocks.

## 🧰 Libraries Used
- OpenCV – For image reading, writing, and processing
- NumPy – For numerical operations and efficient array manipulation
- os – For file system operations like directory creation
- Python 3.8+

## 🚀 Running the Code

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/EC7212-Take-Home-Assignment-1.git](https://github.com/Githmi123/EC7212-Computer-Vision-and-Image-Processing-Take-Home-Assignment-1.git
   cd EC7212-Take-Home-Assignment-
   
2. Make sure required libraries are installed:
    ```bash
    pip install opencv-python numpy

3. Run any task using:
    ```bash
    python3 tasks/task_1_intensity_reduction.py
