# Time-to-Collision Estimation Exercises

## Overview

This series of exercises, provided by the Intelligent Systems Group at Universität Duisburg-Essen, focuses on estimating the time-to-collision (TTC) using image sequences. The goal is to implement techniques for calculating the point in time when a moving object (e.g., a robot) will collide with a solid object, using visual information captured at various moments.

## Exercises

### 1. Preparing the Dataset

- **Objective:** Gather and prepare image sequences for analysis.
- **Tasks:**
  - Download the 'sequences.zip' file containing multiple image sequences of a robot moving towards a solid object.
  - Unzip the file to extract the image sequences, each consisting of a different number of images captured at non-equidistant points in time.
  - A vector (`WS_time.mat` or its equivalent) is provided with each sequence, indicating the timestamps (in milliseconds) of when each image was taken.

### 2. Time of Collision Estimation

- **Objective:** Implement a function to estimate the time of collision (TOC) using the provided image sequences.
- **Tasks:**
  - Create a function that takes a directory containing an image sequence and its corresponding timestamps as input.
  - Analyze the images to extract the height of the object the robot is moving towards.
  - Based on the height measurements from two images and their corresponding timestamps, estimate the TTC.
  - Convert the TTC estimations from the different images into an estimation for the TOC, which is the actual point in time (in milliseconds) when the collision is predicted to occur.
  - Return the estimated TOC in seconds.

### 3. Function Adaptation for All Sequences

- **Objective:** Ensure the TOC estimation function works for all provided sequences.
- **Tasks:**
  - Test and adapt the function to handle all five provided sequences, taking into account their variable image counts and time intervals.
  - Use the estimations of TTC from the different images within a sequence to determine a comprehensive estimation for the TOC.
  - The first sequence should yield an estimated TOC of approximately 24 seconds.

### 4. Visualization and Parameter Adjustment

- **Hints:**
  - For choosing suitable parameters, particularly for image analysis techniques such as edge detection or height extraction, visualizing the extracted features on the images can be very helpful.
  - Techniques such as edge detection, Hough transforms, and height extraction from the images are suggested to be utilized for analyzing the object's size change over time.


# Key Takeaways


- **Time-to-Collision (TTC)**: TTC is crucial for autonomous navigation, predicting the time until an object or camera will collide with another object based solely on visual information from image sequences.

- **3D Motion to 2D Displacement**: 3D motion of objects or camera movement results in 2D displacement in the image plane, offering insights into the dynamics of the scene.

- **Moving Camera and Object Detection**: Identifying moving objects against a moving camera background is a complex challenge that involves distinguishing between 3D motion-induced changes and object-specific movements in an image sequence.

- **Focus-of-Expansion (FoE)**: In image sequences, FoE refers to the point in the image towards which all motion vectors diverge, typically used in TTC estimation and navigation tasks.

- **Correspondence Problem**: A central issue in image sequence analysis is identifying which features in successive frames correspond to the same point in the 3D space, vital for motion tracking and 3D reconstruction.
