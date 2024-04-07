# Kalman Filter Exercises with Python

## Overview

This series of exercises introduces the Kalman Filter for estimating trajectories and tracking objects in image sequences. It is aimed at developing a practical understanding of the Kalman Filter equations in 2D point estimation and applying these to track a robot in an image sequence, even through occlusions.

## Exercise 26: Kalman Filter for 2D Point Estimation

- Implement the Kalman Filter equations to estimate a trajectory in 2D points.
- Generate a set of ground truth points based on a quadratic function and create noisy measurements manually.
- Utilize state transition and measurement model matrices along with system and measurement noise covariance matrices to simulate the Kalman Filter process.
- Visualize and compare the true positions, noisy measurements, and estimated positions.

## Exercise 27: Tracking a Robot with Kalman Filter

- Apply the Kalman Filter to track a robot's position in an image sequence, handling partial occlusions using a pattern matching approach based on cross-correlation.
- Adjust the measurement noise covariance matrix based on the success of the pattern matching to distinguish between successful and failed robot detections.
- Visualize the trajectory of measurements, the estimated positions, and the position uncertainty.
- Experiment with different initialization parameters and system models to optimize the tracking performance.

## Key Concepts

- Understanding the operation and implementation of the Kalman Filter for state estimation in dynamic systems.
- Practicing with real-world data by simulating trajectories and tracking objects in visual data.
- Learning to adjust and experiment with Kalman Filter parameters and models to achieve better estimation accuracy.
