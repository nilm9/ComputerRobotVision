# Exercise 03: Active Contours and Curve Visualization

## Overview

This exercise set introduces active contours, a method for detecting and visualizing object boundaries in images. Participants will learn to implement the shrinkage method for active contour modeling, visualize curves on images, and handle user input to create initial curves for contour detection.

## Exercises Breakdown

### 9. Visualizing Curves - "The House of St. Nicholas"

- **Objective**: Learn to draw curves on images, a foundational skill for visualizing active contour results.
- **Tasks**:
  - Load a grayscale image and draw a predefined octagon on it.
  - Draw the "Haus vom Nikolaus", a closed curve of eight straight lines, on the grayscale image with different colors for vertices and lines.

### 10. Curve Input

- **Objective**: Gain experience in defining initial curves through user interaction, crucial for initializing active contours.
- **Tasks**:
  - Use a graphical tool to let users draw a curve on an image.
  - Extract and round the coordinates of the curve's vertices to integers.
  - Visualize the user-defined curve on the image.

### 11. Active Contours - The Shrinking Method

- **Objective**: Implement the shrinking method for active contour modeling without relying on built-in functions.
- **Tasks**:
  - Create a function to perform simple contour extraction through the shrinking method.
  - Apply Gaussian blur to the image and calculate the gradient magnitude using the Sobel operator.
  - Define an energy component and implement the shrinking method, moving points towards their neighbors based on the energy threshold.

### 12. Applying and Testing MyActiveContour

- **Objective**: Apply the implemented active contour function to various test images and assess its effectiveness.
- **Tasks**:
  - Let users create an initial curve on test images.
  - Use the `MyActiveContour` function to calculate and visualize the final contour.
  - Experiment with different parameters (number of iterations, sigma for Gaussian blur, energy level threshold) to optimize contour detection.

## Key Takeaways


### Internal Energy (E_int)
Maintains the structure of the snake by:
- Ensuring continuity to prevent gaps.
- Promoting curvature for a smoother shape.

### External Energy (E_ext)
Drives the snake towards image features like edges and lines by utilizing image gradients.

### Constraint Energy (E_con)
Incorporates additional knowledge such as user inputs, influencing the snake's behavior with forces like balloon energy to navigate towards object boundaries.

### Operation Process
- The snake iteratively deforms, balancing between internal structure and external feature attraction, while considering user-defined constraints.
- The contour evolves until it reaches a state of minimal energy, closely fitting the object's boundaries.

### Optimization with SGD
- Aims for global minimum energy using Stochastic Gradient Descent by randomly sampling energies to adjust the snake, helping it escape local minima.
- Iterations proceed until convergence, indicated by the snake stabilizing around the object boundary.
- SGD is beneficial for complex energy landscapes with potential multiple minima.