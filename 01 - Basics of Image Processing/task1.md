# Task 1 Summary: Basics of Image Processing

## Overview

This task set aims to introduce fundamental concepts of image processing. The exercises are designed to familiarize you with operations such as reading, displaying, and writing images, color to grayscale conversion, noise simulation, and image smoothing and denoising.

## Exercises

### Exercise 4: Handling Images

#### Loading and Displaying Images
- The task begins with loading both grayscale and RGB images from files. 
- Display these images to understand how image data is visualized.

#### Color Channels
- Investigate the color channels of an RGB image by isolating and displaying each channel (Red, Green, Blue) separately.

#### Grayscale Conversion
- Explore different methods for converting RGB images to grayscale, including averaging and other statistical methods.
- Display the converted images for comparison.

#### Saving Images
- Save the converted grayscale images in a preferred format.

### Exercise 5: Smoothing and Noise

#### Image Smoothing
- Apply smoothing techniques to images to reduce noise or blur details, using both manually created filters and predefined ones.
- Compare the effects of different smoothing techniques on the same image.

#### Noise Simulation
- Introduce various types of noise to images (e.g., Gaussian white noise, salt & pepper noise) to simulate real-world image degradation.
- Display the noisy images alongside the original for visual comparison.

#### Denoising
- Apply denoising techniques to recover the original image from its noisy version as much as possible.
- Evaluate the effectiveness of different denoising methods by comparing the before and after images.

### Exercise 6: Advanced Denoising Challenge

- Apply your learned denoising techniques to a set of provided noisy images.
- Aim to achieve the best possible restoration, as quantified by image quality metrics such as the Peak Signal-to-Noise Ratio (PSNR).
- Save your denoised images and document the improvement in image quality.

## Objectives

- Understand the basics of image file handling, including the differences between grayscale and RGB images.
- Learn how to manipulate image data directly through operations like channel separation and noise addition.
- Explore the effects of various image processing techniques, including smoothing and denoising, on image quality.
- Develop practical skills in improving image quality through denoising, with an emphasis on objective evaluation of results.

# Key Takeaways 

- **Image Representation**: Images are typically stored as multi-dimensional arrays, with grayscale images being 2D arrays, and color images being 3D arrays, where the third dimension represents color channels.

- **Color Space Conversion**: Understanding how to convert between color spaces, such as from RGB to grayscale, is essential in image processing to reduce complexity and focus on intensity information.

- **Noise and Its Impact**:
  - **Gaussian White Noise**: This type of noise has a probability density function equal to that of the Gaussian distribution, often used to model the effect of random processes that occur in nature. The noise level is consistent across the image, which can simulate electronic noise in sensors.
  - **Salt & Pepper Noise**: This is a form of noise typically caused by sharp and sudden disturbances in the image signal. It presents as sparsely occurring white and black pixels, hence the name. This type of noise can simulate dead pixels or faulty data transmission.

- **Smoothing Techniques**: Applying smoothing or filtering techniques, such as Gaussian smoothing, can reduce noise and is a common preprocessing step in image analysis and computer vision algorithms.

