# Camera Calibration and Measurement Exercises

## Overview

This series of exercises is designed to teach camera calibration techniques and their application to measure real-world objects in images using Python. The exercises walk through the process of calibrating a camera, using that calibration to measure distances in an image, and classifying objects like coins based on their size.

## Camera Calibration

### Objective
To determine the intrinsic parameters and distortion coefficients of a camera to correct images and accurately measure objects.

### Procedure
1. Capture 10-20 images of a checkerboard pattern from various angles.
2. Use a camera calibration library like OpenCV in Python to calculate intrinsic parameters.
3. Evaluate the calibration quality and eliminate any outlier images.
4. Export the camera parameters for use in subsequent tasks.

## Ruler Function

### Objective
Turn a camera into a virtual ruler to measure objects in millimeters using the intrinsic parameters from the calibration step.

### Procedure
1. Take an image that includes the checkerboard pattern and objects to be measured.
2. Calculate the extrinsic camera parameters for this particular image using the calibration results.
3. Use Python to process the image, rectify it, and then interactively measure distances between points in world units.

## Coin Classifier

### Objective
Classify coins based on their diameter by applying a circle Hough transform on the rectified image from the camera.

### Procedure
1. Detect coins in the rectified image using the circle Hough transform available in libraries like OpenCV.
2. Determine two points on the coin's border to measure the diameter.
3. Convert the image coordinates of these points to world units and calculate the distance.
4. Classify coins into categories (e.g., 1 Eurocent, 10 Eurocents, 50 Eurocents) based on their measured diameters.
5. Count the number of coins in each category and visualize the results.

## References
- OpenCV Documentation: [Camera Calibration and 3D Reconstruction](https://docs.opencv.org/master/dc/dbb/tutorial_py_calibration.html)
- Circle Detection in OpenCV: [Hough Circle Transform](https://docs.opencv.org/master/da/d53/tutorial_py_houghcircles.html)

## Figures
Figures illustrate the calibration images, the virtual ruler application, and examples of coin classification results.

---
Note: This documentation assumes familiarity with Python programming and basic image processing concepts.
