# main.py
import cv2
from functions import calculate_optical_flow, visualize_optical_flow, load_image, prepare_image_for_flow
import numpy as np
import os

# Parameters
N = 50  # Size of local area
scale_factor = 1  # For visualizing the vectors

# Path to the directory containing image sequences
sequence_dir = './sequencesOpticalFlow/3'

# Load all the images from the directory
images = [load_image(os.path.join(sequence_dir, f)) for f in sorted(os.listdir(sequence_dir)) if f.endswith('.png')]

# Prepare the images (convert to grayscale, scale to range [0, 1])
prepared_images = [prepare_image_for_flow(I) for I in images]

# Process the sequences and visualize optical flow
for i in range(len(prepared_images) - 1):
    flow = calculate_optical_flow(prepared_images[i+1], prepared_images[i], N)
    x, y = np.meshgrid(np.arange(0, flow.shape[1]) * N, np.arange(0, flow.shape[0]) * N)
    vx, vy = flow[..., 0], flow[..., 1]
    visualize_optical_flow(images[i+1], x, y, vx * scale_factor, vy * scale_factor, f'flow_{i}.png')

print("Optical flow processing is complete.")
