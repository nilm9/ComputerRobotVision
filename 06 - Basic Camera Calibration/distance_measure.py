import cv2
import numpy as np

# Define object points for chessboard (assumed to be the same as during the calibration process)
objp = np.zeros((6*7, 3), np.float32)
objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)

# Global variables to store clicks
click_points = []
world_points = []

def click_event(event, x, y, flags, params):
    # To collect two points for distance calculation
    global click_points, world_points, objp, mtx, dist

    if event == cv2.EVENT_LBUTTONDOWN:
        # Save the 2D click point
        click_points.append((x, y))

        # Calculate the corresponding 3D point
        ret, rvecs, tvecs = cv2.solvePnP(objp, params[0], mtx, dist)
        image_points = np.array([[x, y]], dtype='double')
        world_point, _ = cv2.projectPoints(image_points, rvecs, tvecs, mtx, dist)
        world_points.append(world_point[0][0])

        # Draw the point as a circle
        cv2.circle(params[1], (x, y), 5, (0, 0, 255), -1)

        # If two points have been clicked, calculate the distance
        if len(click_points) == 2:
            distance = np.linalg.norm(world_points[0] - world_points[1])
            print(f"Distance between points in world units: {distance:.2f}")

            # Clear the points for the next measurement
            click_points = []
            world_points = []

        cv2.imshow("Image", params[1])

def measure_distance(image_path, mtx, dist):
    # Load the image
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find the chessboard corners
    ret, corners = cv2.findChessboardCorners(gray, (7, 6), None)

    if not ret:
        print("Chessboard couldn't be found in the image.")
        return None

    # Draw the corners
    cv2.drawChessboardCorners(img, (7, 6), corners, ret)

    # Set callback function for mouse click events
    cv2.imshow('Image', img)
    cv2.setMouseCallback('Image', click_event, [corners, img])

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Loading the camera matrix and distortion coefficients from a file
calib_data = np.load('calibration_data.npz')
mtx = calib_data['mtx']
dist = calib_data['dist']

# Need to make the photos
measure_distance('/path/to/image/with/checkerboard.jpg', mtx, dist)
