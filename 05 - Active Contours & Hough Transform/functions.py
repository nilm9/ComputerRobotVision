import numpy as np
import cv2
from skimage import io, color
from skimage.segmentation import active_contour
from skimage.filters import gaussian
from skimage.draw import ellipse


def downscale_image(image, scale_percent=50):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)


def segment_active_contour(image_path):
    image = io.imread(image_path)
    if len(image.shape) == 3:  # Convert to grayscale if the image is RGB
        image = color.rgb2gray(image)

    # Downscale the image for faster processing
    image = downscale_image(image)

    # Assuming the object to be centered and occupying a significant part of the image
    r, c = image.shape[:2]
    r_center, c_center = r // 2, c // 2
    r_radius, c_radius = r // 4, c // 4  # Rough estimates
    rr, cc = ellipse(r_center, c_center, r_radius, c_radius)
    init = np.column_stack([cc, rr])

    # Perform segmentation
    snake = active_contour(gaussian(image, 3),
                           init, alpha=0.015, beta=10, gamma=0.001,
                           convergence=0.1)  # Convergence parameter added

    return image, init, snake


def detect_and_draw_circles(image_path, dp=1, min_dist=20, param1=100, param2=50, min_radius=0, max_radius=0):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Downscale the image for faster processing
    image = downscale_image(image)

    image_color = cv2.imread(image_path)
    # Increase param1 and param2 to reduce false positives
    # Adjust min_dist if the coins are close to each other
    circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, dp, min_dist,
                               param1=param1, param2=param2,
                               minRadius=min_radius, maxRadius=max_radius)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # Draw the outer circle
            cv2.circle(image_color, (i[0], i[1]), i[2], (255, 0, 0), 2)
            # Draw the center of the circle
            cv2.circle(image_color, (i[0], i[1]), 2, (0, 255, 0), 3)
    else:
        # No circles were found
        print(f"No circles detected in {image_path}.")

    return image_color
