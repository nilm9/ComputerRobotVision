import os
import cv2
import matplotlib.pyplot as plt
from functions import segment_active_contour, detect_and_draw_circles

def process_active_contours(folder_path):
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith('.png'):
            image_path = os.path.join(folder_path, filename)
            image_ac, init_ac, snake_ac = segment_active_contour(image_path)

            # Plot initial and final contours
            plt.figure(figsize=(10, 5))
            plt.imshow(image_ac, cmap='gray')
            plt.plot(init_ac[:, 0], init_ac[:, 1], '--r', lw=3)  # Initial contour
            plt.plot(snake_ac[:, 0], snake_ac[:, 1], '-g', lw=3)  # Final contour
            plt.title(f'Active Contour Result - {filename}')
            plt.axis('off')
            plt.show()
            plt.close()  # Close the figure to free up memory

def process_hough_circles(folder_path):
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith('.png'):
            image_path = os.path.join(folder_path, filename)
            result_image_hc = detect_and_draw_circles(image_path)

            # Convert to RGB and display
            result_image_hc_rgb = cv2.cvtColor(result_image_hc, cv2.COLOR_BGR2RGB)
            plt.imshow(result_image_hc_rgb)
            plt.title(f'Detected Circles - {filename}')
            plt.axis('off')
            plt.show()
            plt.close()  # Close the figure to free up memory

def main():
    # Path to the image folders (update to your specific paths)
    active_contour_folder = './ActiveContourTestImages'
    hough_circle_folder = './coinsandpips'

    # Process images for active contour
    process_active_contours(active_contour_folder)

    # Process images for Hough circle detection
    process_hough_circles(hough_circle_folder)

if __name__ == "__main__":
    main()
