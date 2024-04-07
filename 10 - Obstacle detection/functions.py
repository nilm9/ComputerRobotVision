import os

# functions.py
import cv2
import numpy as np
import scipy.io
from scipy.linalg import svd

def load_image_sequence(directory):
    # Get the number of .png files in the directory
    return [f for f in os.listdir(directory) if f.endswith('.png')]

def load_correspondences(file_path):
    # Load the MATLAB .mat file containing correspondences
    return scipy.io.loadmat(file_path)

def detect_and_match_features(orb, bf, descriptors_prev, current_img, roi):
    # Detect and match features between two images in a given ROI using OpenCV
    # orb and bf are the ORB detector and BFMatcher objects created outside this function
    keypoints_curr, descriptors_curr = orb.detectAndCompute(current_img, mask=roi)
    matches = bf.match(descriptors_prev, descriptors_curr)
    return matches, keypoints_curr, descriptors_curr

def compute_matrices(X, Y, XPrime, YPrime, L):
    Mcor = np.zeros((2*L, 8))
    Mnex = np.zeros((2*L, 1))
    for j in range(L):
        Mcor[2*j] = [X[j], Y[j], 1, 0, 0, 0, -X[j]*XPrime[j], -Y[j]*XPrime[j]]
        Mcor[2*j+1] = [0, 0, 0, X[j], Y[j], 1, -X[j]*YPrime[j], -Y[j]*YPrime[j]]
        Mnex[2*j:2*j+2] = [XPrime[j], YPrime[j]]
    return Mcor, Mnex

def check_obstacles(sigma1, sigma2, theta):
    # Check if the number of singular values above a threshold is equal or not
    return sum(sigma1 > theta) == sum(sigma2 > theta)

def save_obstacles(file_path, obstacles):
    # Save the obstacles matrix to a .mat file
    scipy.io.savemat(file_path, {'obstacles': obstacles})
