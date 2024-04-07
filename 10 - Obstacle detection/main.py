# main.py
import cv2
import numpy as np
import os
from functions import (load_image_sequence, load_correspondences,
                       detect_and_match_features, compute_matrices,
                       check_obstacles, save_obstacles)
from scipy.linalg import svd

# Select sequence
img_seq_dir = "./1"
img_seq = load_image_sequence(img_seq_dir)

# Create ORB detector and BFMatcher objects
orb = cv2.ORB_create()
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Initialize an empty list to hold descriptors from the previous image for each tile
previous_descriptors = [None] * 8
descriptors_curr = None
# Initialize obstacles matrix
obstacles = np.zeros((len(img_seq), 8))

for k, filename in enumerate(img_seq):
    # Load image and convert to grayscale
    img_path = os.path.join(img_seq_dir, filename)
    I = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2GRAY)

    # Display the image
    cv2.imshow('Image', I)
    cv2.waitKey(1)

    for t in range(8):
        # Define the ROI/tile coordinates
        roiP = (128 * (t - 1) + 1, 128 * 5, 128, 128 * 2)
        roi = np.zeros(I.shape[:2], dtype=np.uint8)
        roi[roiP[1]:roiP[1] + roiP[3], roiP[0]:roiP[0] + roiP[2]] = 255

        # Draw rectangle around the ROI
        cv2.rectangle(I, (roiP[0], roiP[1]), (roiP[0] + roiP[2], roiP[1] + roiP[3]), (255, 0, 0), 2)

        if k > 0:  # No previous image for the first frame
            # Detect and match features
            if previous_descriptors[t] is not None:
                matches, keypoints_curr, descriptors_curr = detect_and_match_features(
                    orb, bf, previous_descriptors[t], I, roi)

                # Extract coordinates of corresponding points
                X = np.float32([keypoints_curr[m.trainIdx].pt[0] for m in matches])
                Y = np.float32([keypoints_curr[m.trainIdx].pt[1] for m in matches])
                XPrime = np.float32([previous_descriptors[t][m.queryIdx].pt[0] for m in matches])
                YPrime = np.float32([previous_descriptors[t][m.queryIdx].pt[1] for m in matches])

                # Plot points in current image which have a match with salient point from previous image
                for (x, y) in zip(XPrime, YPrime):
                    cv2.circle(I, (int(x), int(y)), 5, (0, 255, 255), -1)  # Yellow dot

                L = len(matches)
                if L >= 8:
                    Mcor, Mnex = compute_matrices(X, Y, XPrime, YPrime, L)

                    sigma1 = svd(Mcor, compute_uv=False)
                    sigma2 = svd(np.hstack([Mcor, Mnex]), compute_uv=False)

                    theta = 8
                    if check_obstacles(sigma1, sigma2, theta):
                        obst_color = (0, 255, 0)  # Green for no obstacles
                    else:
                        obst_color = (0, 0, 255)  # Red for obstacles
                        obstacles[k, t] = 1

                    for (x, y) in zip(XPrime, YPrime):
                        cv2.circle(I, (int(x), int(y)), 5, obst_color, -1)  # Dot with obstacle detection color

            # Update the previous descriptors with the current ones for the next iteration
            previous_descriptors[t] = descriptors_curr

    # Display the image with obstacles
    cv2.imshow('Image with Obstacles', I)
    cv2.waitKey(1)

# Save the obstacles matrix
save_obstacles('obstacles.mat', obstacles)
cv2.destroyAllWindows()
