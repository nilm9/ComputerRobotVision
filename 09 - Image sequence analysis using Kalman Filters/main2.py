import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


# Define a function to load images
def load_image(path):
    return cv2.imread(path, cv2.IMREAD_GRAYSCALE)


# Define a function for pattern matching that returns the center location and max correlation
def pattern_matching(image, pattern, threshold):
    result = cv2.matchTemplate(image, pattern, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # Check if the pattern matching is above the threshold
    if max_val < threshold:
        return None  # Pattern matching failed
    # Calculate the center location of the matched pattern
    center_loc = (max_loc[0] + pattern.shape[1] // 2, max_loc[1] + pattern.shape[0] // 2)
    return center_loc, max_val  # Return center location and max correlation


# Define a function to initialize the Kalman Filter
def init_kalman_filter(F, H, Q, R, initial_state, initial_covariance):
    kf = cv2.KalmanFilter(4, 2)
    kf.transitionMatrix = F
    kf.measurementMatrix = H
    kf.processNoiseCov = Q
    kf.measurementNoiseCov = R
    kf.statePre = initial_state
    kf.errorCovPre = initial_covariance
    return kf


# Define a function to update the Kalman Filter with each new measurement
def update_kalman_filter(kf, measurement):
    predicted_state = kf.predict()
    if measurement is not None:
        # Reshape measurement to match the measurement matrix H
        kf.correct(np.array([[measurement[0]], [measurement[1]]], dtype=np.float32))
    return kf.statePost.copy()


# Load the pattern image and image sequence
pattern = load_image('pattern.png')  # Update with the actual path
image_folder = './robWall'  # Update with the actual path

# Kalman Filter initialization
F = np.array([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32)  # State transition matrix
H = np.array([[1, 0, 0, 0], [0, 1, 0, 0]], np.float32)  # Measurement matrix
Q = 1e-5 * np.eye(4, dtype=np.float32)  # Process noise covariance
R = 10 * np.eye(2, dtype=np.float32)  # Measurement noise covariance
initial_state = np.array([0, 0, 0, 0], np.float32)  # Initial state estimate
initial_covariance = 1 * np.eye(4, dtype=np.float32)  # Initial state covariance

kf = init_kalman_filter(F, H, Q, R, initial_state, initial_covariance)

# Process image sequence and update Kalman Filter
estimated_positions = []  # List to hold estimated positions
measurement_positions = []  # List to hold actual measurements
correlation_values = []  # List to hold correlation values
threshold = 0.5  # Threshold for successful pattern matching

for filename in sorted(os.listdir(image_folder)):
    if filename.endswith('.png'):
        image_path = os.path.join(image_folder, filename)
        image = load_image(image_path)
        measurement = pattern_matching(image, pattern, threshold)

        # Handle pattern matching results
        if measurement is not None:
            # If pattern match is successful, use smaller measurement noise
            kf.measurementNoiseCov = np.array([[1, 0], [0, 1]], np.float32)
            measurement_positions.append(measurement[0])
            correlation_values.append(measurement[1])
        else:
            # If pattern match fails, use larger measurement noise to reflect uncertainty
            kf.measurementNoiseCov = np.array([[10000, 0], [0, 10000]], np.float32)

        # Update Kalman Filter with the new measurement
        estimated_state = update_kalman_filter(kf, measurement[0] if measurement is not None else None)
        estimated_positions.append(estimated_state[:2])

# Convert lists to NumPy arrays for plotting
estimated_positions = np.array(estimated_positions)
measurement_positions = np.array(measurement_positions)

# Plot the estimated trajectory
plt.figure(figsize=(10, 5))
if measurement_positions.size > 0:
    plt.plot(measurement_positions[:, 0], measurement_positions[:, 1], 'r--', label='Trajectory of measurements')
plt.plot(estimated_positions[:, 0], estimated_positions[:, 1], 'b.-', label='Estimated trajectory')
if measurement_positions.size > 0:
    plt.plot(measurement_positions[-1, 0], measurement_positions[-1, 1], 'ro', label='Current measurement')
plt.plot(estimated_positions[-1, 0], estimated_positions[-1, 1], 'bx', label='Current state estimation')
if correlation_values:
    plt.text(estimated_positions[-1, 0], estimated_positions[-1, 1], f'Max. correlation: {max(correlation_values):.5f}',
             fontsize=8)
plt.legend()
plt.savefig('kalmanII.png')
plt.show()
