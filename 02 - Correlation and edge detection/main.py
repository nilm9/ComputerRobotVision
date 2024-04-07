import cv2
import numpy as np
import os
from functions import edge_detection, plot_results


def process_image(image_path, operator_x, operator_y, thresholds, output_folder):
    # Load grayscale image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Perform edge detection with different thresholds
    edge_maps = [edge_detection(image, operator_x, operator_y, threshold) for threshold in thresholds]

    # Generate titles for plot
    threshold_titles = [f'Edge Map (Threshold = {threshold})' for threshold in thresholds]
    titles = ['Original Image'] + threshold_titles

    # Generate output file name
    base_name = os.path.basename(image_path)
    file_name, _ = os.path.splitext(base_name)
    output_path = os.path.join(output_folder, f'{file_name}_edge_detection.png')

    # Plot and save results
    images = [image] + edge_maps
    plot_results(images, titles, output_path)


def main():
    image_directory = './edgetestimages'  # Directory containing images
    output_folder = './results'  # Directory to save results
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Define operators for edge detection
    operator_x = np.array([[-1, 0, 1]])  # Horizontal edge operator
    operator_y = np.array([[-1], [0], [1]])  # Vertical edge operator
    thresholds = [0.20, 0.5, 0.75]

    # Process each image in the directory
    for file_name in os.listdir(image_directory):
        # Construct the full file path
        file_path = os.path.join(image_directory, file_name)

        # Check if the file is an image (e.g., .png, .jpg, .jpeg)
        if file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            print(f'Processing {file_name}...')
            process_image(file_path, operator_x, operator_y, thresholds, output_folder)


if __name__ == '__main__':
    main()
