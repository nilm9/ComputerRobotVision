import numpy as np
import matplotlib.pyplot as plt

# Parameters for the ground truth and noise
a, b, c = -0.43, 19, 150
X = np.arange(1, 40.1, 0.1)

# Assuming that we have better estimates for the noise now
measurement_noise_cov = np.array([[250, 0], [0, 250]])  # Reduced noise levels
process_noise_cov = np.array([[1e-4, 0, 0, 0], [0, 1e-4, 0, 0], [0, 0, 1e-2, 0], [0, 0, 0, 1e-2]])

# Kalman Filter matrices
F = np.array([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]])  # Assuming constant velocity model
H = np.array([[1, 0, 0, 0], [0, 1, 0, 0]])
Q = process_noise_cov  # Updated process noise covariance
R = measurement_noise_cov  # Updated measurement noise covariance

# Assuming we have a better initial state now
initial_state = np.array([0, 0, 1, -5])  # Initial velocity set to reflect the parabola opening downwards
initial_covariance = np.eye(4)

def create_ground_truth(a, b, c, X):
    """
    Create a set of points representing the ground truth of our system.

    Parameters:
    - a, b, c: coefficients for the quadratic equation y = a*(x-b)^2 + c
    - X: array of x values

    Returns:
    - 2D array of ground truth [x, y] positions
    """
    Y = a * (X - b) ** 2 + c
    return np.vstack((X, Y)).T


def simulate_noisy_measurements(true_positions, measurement_noise_cov):
    """
    Add simulated noise to the ground truth positions to create noisy measurements.

    Parameters:
    - true_positions: 2D array of ground truth [x, y] positions
    - measurement_noise_cov: covariance matrix for the noise

    Returns:
    - 2D array of noisy measurements
    """
    noise = np.random.multivariate_normal([0, 0], measurement_noise_cov, size=true_positions.shape[0])
    noisy_measurements = true_positions + noise
    return noisy_measurements


def kalman_filter(measurements, F, H, Q, R, initial_state, initial_covariance):
    """
    Apply the Kalman filter to estimate states from measurements.

    Parameters:
    - measurements: 2D array of measured [x, y] positions
    - F: state transition matrix
    - H: measurement matrix
    - Q: process noise covariance matrix
    - R: measurement noise covariance matrix
    - initial_state: initial state estimate
    - initial_covariance: initial estimate of state covariance

    Returns:
    - Tuple of arrays containing the estimated states and covariances
    """
    # Initialize the state estimates list with the initial state
    estimated_states = [initial_state]
    # Initialize the covariance estimates list with the initial covariance
    estimated_covariances = [initial_covariance]

    for measurement in measurements:
        # Prediction Step:
        # Use the state transition matrix to predict the next state
        predicted_state = F @ estimated_states[-1]
        # Use the state transition matrix to predict the next covariance
        predicted_covariance = F @ estimated_covariances[-1] @ F.T + Q

        # Update Step:
        # Calculate the difference between actual measurement and prediction
        innovation = measurement - H @ predicted_state
        # Calculate the innovation covariance
        innovation_covariance = H @ predicted_covariance @ H.T + R
        # Calculate the Kalman gain
        kalman_gain = predicted_covariance @ H.T @ np.linalg.inv(innovation_covariance)

        # Correct the predicted state using the measurement and Kalman gain
        updated_state = predicted_state + kalman_gain @ innovation
        # Update the state covariance
        updated_covariance = (np.eye(len(kalman_gain)) - kalman_gain @ H) @ predicted_covariance

        # Append the updated state and covariance to the lists
        estimated_states.append(updated_state)
        estimated_covariances.append(updated_covariance)

    # Return the list of estimated states and covariances as numpy arrays
    return np.array(estimated_states), np.array(estimated_covariances)


# Generate the ground truth and measurements
true_positions = create_ground_truth(a, b, c, X)
noisy_measurements = simulate_noisy_measurements(true_positions, measurement_noise_cov)

# Run Kalman Filter
estimated_states, _ = kalman_filter(noisy_measurements, F, H, Q, R, initial_state, initial_covariance)

# Visualization
plt.scatter(X, true_positions[:, 1], label='True Position', s=10)
plt.scatter(X, noisy_measurements[:, 1], label='Measured Position', s=10)
plt.plot(X, estimated_states[1:, 1], label='Estimated Position', color='blue')
plt.legend()
plt.show()
