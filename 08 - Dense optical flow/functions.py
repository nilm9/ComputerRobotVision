import sys

import cv2
import numpy as np
import matplotlib.pyplot as plt


def calculate_optical_flow(Ic, Il, N):
    # Initialize flow vectors
    # Determine how many blocks of size N will fit in the image
    rows = Ic.shape[0] // N  # Number of vertical blocks
    cols = Ic.shape[1] // N  # Number of horizontal blocks
    # Initialize an array to hold the optical flow vectors for each block
    flow_vectors = np.zeros((rows, cols, 2), dtype=np.float32)

    # Calculate gradients using Sobel operators for the current image Ic
    # Ix is the gradient in the x direction (horizontal edges)
    Ix = cv2.Sobel(Ic, cv2.CV_64F, 1, 0, ksize=5)
    # Iy is the gradient in the y direction (vertical edges)
    Iy = cv2.Sobel(Ic, cv2.CV_64F, 0, 1, ksize=5)
    # It is the temporal gradient, which is the difference between
    # the current image and the previous image (Il)
    It = Il - Ic

    # Loop through each block to calculate optical flow vectors
    for i in range(0, rows * N, N):
        for j in range(0, cols * N, N):
            # Define the local region for each block by flattening the matrices
            # to create vectors of gradients for x, y, and t
            Ix_local = Ix[i:i+N, j:j+N].flatten()
            Iy_local = Iy[i:i+N, j:j+N].flatten()
            It_local = It[i:i+N, j:j+N].flatten()

            # Construct matrices A and b for the system of equations A * nu = b
            # A contains the spatial gradients and b contains the negative temporal gradients
            A = np.vstack((Ix_local, Iy_local)).T
            b = -It_local

            # Solve for the flow vectors nu (which contains vx and vy) if A is not singular
            # Check if A is invertible (condition number is not too large)
            if np.linalg.cond(A) < 1/sys.float_info.epsilon:
                # nu is calculated using the pseudoinverse of A and matrix multiplication with b
                nu = np.linalg.pinv(A).dot(b)
                # Assign the computed flow vector to the correct block in the flow_vectors array
                flow_vectors[i//N, j//N, :] = nu

    # Return the entire array of flow vectors
    return flow_vectors
def visualize_optical_flow(I, x, y, vx, vy, filename):
    # Display the image
    plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))
    plt.quiver(x, y, vx, vy, color='r')

    # Save the figure
    plt.savefig("./results/3" + filename)
    plt.close()

def load_image(image_path):
    return cv2.imread(image_path)

def prepare_image_for_flow(I):
    I_gray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
    return I_gray.astype(np.float32) / 255.0

