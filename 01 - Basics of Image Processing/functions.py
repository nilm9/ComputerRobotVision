import cv2
import numpy as np
import matplotlib.pyplot as plt

def read_image(image_path, color=cv2.IMREAD_COLOR):
    """Reads an image from a file path."""
    return cv2.imread(image_path, color)

def convert_to_grayscale(image):
    """Converts an RGB image to grayscale."""
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

def add_gaussian_noise(image, mean=0, var=10):
    """Adds Gaussian noise to an image."""
    sigma = var ** 0.5
    gaussian = np.random.normal(mean, sigma, image.shape)
    noisy_image = np.clip(image + gaussian, 0, 255).astype('uint8')
    return noisy_image

def gaussian_smoothing(image, kernel_size=(5, 5)):
    """Applies Gaussian smoothing to an image."""
    return cv2.GaussianBlur(image, kernel_size, 0)

def save_image(image, file_name):
    """Saves an image to a file."""
    cv2.imwrite(file_name, image)
