import cv2
import numpy as np
import os
import matplotlib.pyplot as plt


def my_hough(edge_image):
    # Calculate the maximum possible distance (D) for rho,
    # which is the diagonal length of the image
    D = np.ceil(np.sqrt(np.sum(np.array(edge_image.shape) ** 2))).astype(int)

    # Create an array of rho values ranging from -D to D
    h = np.linspace(-D, D, 2 * D + 1)

    # Create an array of theta values ranging from -90 to 89 degrees,
    # then convert degrees to radians since np.cos and np.sin use radians
    alpha = np.deg2rad(np.arange(-90, 90))

    # Initialize the accumulator array to zeros, with dimensions of
    # the length of rho array and length of theta array
    # This will count the number of votes each (rho, theta) pair gets
    accu = np.zeros((2 * D + 1, len(alpha)), dtype=np.int64)

    # Get the indices of the edge points, which are non-zero values in the edge image
    y_idxs, x_idxs = np.nonzero(edge_image)

    # For each edge point, calculate all possible (rho, theta) pairs that could have
    # created this edge point based on the polar form of the line equation:
    # rho = x*cos(theta) + y*sin(theta)
    for i in range(len(x_idxs)):
        x = x_idxs[i]
        y = y_idxs[i]
        for j in range(len(alpha)):
            # Calculate rho for this edge point (x, y) and angle alpha[j]
            rho = x * np.cos(alpha[j]) + y * np.sin(alpha[j])
            # Find the nearest index in the h array for this calculated rho value
            rho_idx = np.argmin(np.abs(h - rho))
            # Increment the accumulator cell for this (rho_idx, alpha[j]) pair
            accu[rho_idx, j] += 1

    # Return the accumulator array and the h (rho) and alpha (theta) arrays
    return accu, h, alpha


def draw_lines(image, h, theta, peaks):
    for peak in peaks:
        rho = h[peak[0]]
        # Ensure theta is accessed as an array
        angle = theta[peak[1]]  # This should be the angle in radians
        a = np.cos(angle)
        b = np.sin(angle)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Ensure correct color space for plt
    plt.title("Detected Lines")
    plt.axis('off')
    plt.show()

def main():
    # Load an edge image
    edge_image = cv2.imread('./HoughTestImages/edge02.png', cv2.IMREAD_GRAYSCALE)
    edge_image = cv2.Canny(edge_image, 50, 150)  # Use Canny edge detection or any pre-processing necessary

    # Perform Hough transform
    accu, h, alpha = my_hough(edge_image)

    # Find peaks in the accumulator
    num_peaks = 10
    indices = np.argpartition(accu.flatten(), -2*num_peaks)[-2*num_peaks:]
    peak_indices = np.vstack(np.unravel_index(indices, accu.shape)).T

    # Visualize the result
    plt.figure(figsize=(10, 5))

    plt.subplot(131)
    plt.imshow(edge_image, cmap='gray')
    plt.title('Edge Image')

    plt.subplot(132)
    plt.imshow(accu, extent=[np.rad2deg(alpha[0]), np.rad2deg(alpha[-1]), h[-1], h[0]], cmap='gray')
    plt.title('Hough Image')

    plt.subplot(133)
    plt.imshow(np.log(1 + accu), extent=[np.rad2deg(alpha[0]), np.rad2deg(alpha[-1]), h[-1], h[0]], cmap='gray', aspect='auto')
    plt.title('Hough Image (logarithmic scale)')

    plt.tight_layout()
    plt.show()

    # Draw detected lines on the original image
    original_image = cv2.cvtColor(edge_image, cv2.COLOR_GRAY2BGR)
    draw_lines(original_image, h, alpha, peak_indices)

if __name__ == "__main__":
    main()
