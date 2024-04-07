import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
from functions import my_active_contour


def draw_contour(image, x, y, title="Active Contour", save_path=None):

    plt.figure()
    plt.imshow(image, cmap='gray')
    plt.plot(x + [x[0]], y + [y[0]], 'g-', linewidth=2)  # Close the contour by connecting to the start
    plt.title(title)
    plt.axis('off')
    if save_path:
        plt.savefig(save_path)
    plt.show()
    plt.close()


def process_directory(directory_path, N, sigma, lvl):

    for filename in os.listdir(directory_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(directory_path, filename)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            # Get image dimensions
            h, w = image.shape[:2]

            # Define an initial contour that frames the entire image
            x0 = [0, w - 1, w - 1, 0, 0]  # X coordinates
            y0 = [0, 0, h - 1, h - 1, 0]  # Y coordinates




            x_final, y_final = my_active_contour(image, x0, y0, N, sigma, lvl)

            image_colored = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
            draw_contour(image_colored, x_final, y_final, save_path=f"contoured_{filename}")


def main():
    directory_path = './TestImages'
    N = 10000000  # Number of iterations
    sigma = 2.0  # Gaussian blur parameter
    lvl = 10  # Edge level threshold

    process_directory(directory_path, N, sigma, lvl)


if __name__ == "__main__":
    main()
