import numpy as np
from scipy.signal import convolve2d
from scipy.ndimage import gaussian_filter
from imageio import imread, imwrite
import matplotlib.pyplot as plt


def validate_inputs(image, operator):
    if not (isinstance(image, np.ndarray) and isinstance(operator, np.ndarray)):
        raise ValueError("Inputs must be of type numpy.ndarray")
    if image.ndim != 2 or operator.ndim != 2:
        raise ValueError("Inputs must be two dimensional")
    if any(size % 2 == 0 for size in operator.shape):
        raise ValueError("Operator must have odd dimensions")
    if operator.shape[0] >= image.shape[0] or operator.shape[1] >= image.shape[1]:
        raise ValueError("Operator must be smaller than image")


def my_correlation(image, operator):
    validate_inputs(image, operator)
    # Convert inputs to float
    image = image.astype(np.float64)
    operator = operator.astype(np.float64)

    # Calculate half side lengths of the operator
    h1, h2 = operator.shape[0] // 2, operator.shape[1] // 2

    # Initialize the output with zeros
    fim_corr = np.zeros_like(image)

    # Loop over each position where the operator fits within the image
    for i in range(h1, image.shape[0] - h1):
        for j in range(h2, image.shape[1] - h2):
            # Extract the sub-region of the image that aligns with the operator
            sub_image = image[i - h1:i + h1 + 1, j - h2:j + h2 + 1]
            # Calculate the correlation for the current position by
            # multiplying the operator with the sub-image and summing the results
            fim_corr[i, j] = np.sum(sub_image * operator)

    return fim_corr


def edge_detection(image, operator_x, operator_y, threshold):
    # Normalize image
    image = image / 255.0

    # Calculate gradients
    gx = my_correlation(image, operator_x)
    gy = my_correlation(image, operator_y)

    # Calculate magnitude of gradient
    mog = np.sqrt(gx ** 2 + gy ** 2)

    # Thresholding
    edge_map = mog > threshold
    return edge_map.astype(np.uint8) * 255  # Convert to uint8 format


def plot_results(images, titles, filename):
    plt.figure(figsize=(18, 12))
    for i, (image, title) in enumerate(zip(images, titles), 1):
        plt.subplot(2, 3, i)
        plt.imshow(image, cmap='gray')
        plt.title(title)
        plt.axis('off')
    plt.savefig(filename)
    plt.show()
