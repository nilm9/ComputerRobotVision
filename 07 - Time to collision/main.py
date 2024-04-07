import os

from functions import estimate_height_in_image, calculate_toc, load_timestamps

def process_sequence(sequence_dir):
    timestamps = load_timestamps(sequence_dir)
    heights = []

    for idx, time in enumerate(timestamps):
        image_path = os.path.join(sequence_dir, f"image_{idx+1}.png")
        height = estimate_height_in_image(image_path)
        if height is not None:
            heights.append(height)
        else:
            print(f"Height estimation failed for image {idx+1}")

    if len(heights) > 1:
        toc = calculate_toc(heights, timestamps)
        return toc
    else:
        print("Not enough data to estimate the time of collision.")
        return None

if __name__ == "__main__":
    sequence_dir = './sequences/4/'
    toc_seconds = process_sequence(sequence_dir)
    if toc_seconds:
        print(f"Estimated Time of Collision: {abs(toc_seconds)} seconds")
    else:
        print("Time of Collision could not be estimated.")
