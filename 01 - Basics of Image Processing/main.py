from functions import read_image, convert_to_grayscale, add_gaussian_noise, gaussian_smoothing, save_image
import os


def main():
    # Define the path to the directory containing the noisy images
    noisy_images_path = './NoiselessImages'
    noisy_images_save_path = './NoiselessImages'  # If you want to save in the same directory

    # Iterate over all files in the noisy images directory
    for file_name in os.listdir(noisy_images_path):
        # Construct the full file path
        file_path = os.path.join(noisy_images_path, file_name)

        # Check if the file is an image (you can add more extensions if needed)
        if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.webp')):
            # Read and process the image
            image = read_image(file_path)
            grayscale_image = convert_to_grayscale(image)
            noisy_image = add_gaussian_noise(grayscale_image)
            smoothed_image = gaussian_smoothing(noisy_image)

            # Save the processed images with new names in the same directory
            base_name = os.path.splitext(file_name)[0]
            save_image(grayscale_image, os.path.join(noisy_images_save_path, base_name + '_grayscale.png'))
            save_image(noisy_image, os.path.join(noisy_images_save_path, base_name + '_noisy.png'))
            save_image(smoothed_image, os.path.join(noisy_images_save_path, base_name + '_smoothed.png'))


if __name__ == "__main__":
    main()
