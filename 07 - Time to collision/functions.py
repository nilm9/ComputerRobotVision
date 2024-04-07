import cv2
import numpy as np
import os
import json

from scipy.io import loadmat


def load_timestamps(sequence_dir):
    # The path to the .mat file with the timestamps
    mat_path = os.path.join(sequence_dir, 'WS_time.mat')

    # Load the .mat file
    mat = loadmat(mat_path)

    # Extract the timestamps from the 'time' key of the .mat file
    timestamps = mat['time'].squeeze()  # Remove single-dimensional entries from the array

    return timestamps


def estimate_height_in_image(image_path):
    # Load the image in grayscale mode
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Image at path {image_path} not found.")

    # Threshold the image to get the object as a white shape on a black background
    _, binary_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return None

    # Find the largest contour based on area
    largest_contour = max(contours, key=cv2.contourArea)

    # Calculate the bounding box of this contour
    _, _, _, height = cv2.boundingRect(largest_contour)
    return height


def calculate_toc(heights, times):
    # We'll use linear regression to fit the heights to times
    # and then use the model to predict the time when height approaches zero
    heights = np.array(heights, dtype=np.float64)
    times = np.array(times, dtype=np.float64)

    # Fit a line (a*x + b) to the data
    A = np.vstack([times, np.ones(len(times))]).T
    a, b = np.linalg.lstsq(A, heights, rcond=None)[0]

    # Calculate the estimated time of collision
    estimated_toc = -b / a
    return estimated_toc


