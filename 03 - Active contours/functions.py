import numpy as np
import cv2

def apply_gaussian_blur(image, sigma):
    return cv2.GaussianBlur(image, (0, 0), sigma)

def calculate_gradients(image):
    grad_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
    grad_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
    return grad_x, grad_y

def magnitude_of_gradient(grad_x, grad_y):
    return np.sqrt(grad_x**2 + grad_y**2)

def is_edge_strong(mag, y, x, lvl):
    return mag[y, x] > lvl

def update_point(point, grad, lvl, mag):
    """
    Propose a new point based on the direction of the edge.
    Move the point perpendicular to the edge direction (gradient direction).
    """
    # Calculate the perpendicular direction to the gradient
    perpendicular_direction = np.array([-grad[1], grad[0]])
    perpendicular_direction /= (np.linalg.norm(perpendicular_direction) + 1e-10)

    # Propose moving in both possible perpendicular directions
    move_in = point + perpendicular_direction.astype(np.int32)
    move_out = point - perpendicular_direction.astype(np.int32)

    # Check which direction is towards a stronger edge, if any
    if is_edge_strong(mag, *move_in, lvl):
        return move_in
    elif is_edge_strong(mag, *move_out, lvl):
        return move_out
    return point  # Remain in place if no strong edge is found

def my_active_contour(image, x0, y0, N, sigma, lvl):
    # Preprocessing step: Apply Gaussian blur and calculate gradient magnitude
    image_blurred = apply_gaussian_blur(image, sigma)
    grad_x, grad_y = calculate_gradients(image_blurred)
    mag = magnitude_of_gradient(grad_x, grad_y)

    # Initialize the contour points array
    contour_points = np.stack((y0, x0)).T

    # Iterative loop to move contour points towards edges
    for iteration in range(N):
        # Apply internal and external forces, update contour points
        for i, point in enumerate(contour_points):
            grad = np.array([grad_y[point[0], point[1]], grad_x[point[0], point[1]]])
            new_point = update_point(point, grad, lvl, mag)  # Use update_point function

            # If the new point is different from the current point, update it
            if not np.array_equal(new_point, point):
                contour_points[i] = new_point

    # Extract final contour coordinates
    x_final, y_final = contour_points[:, 1], contour_points[:, 0]
    return x_final.tolist(), y_final.tolist()
