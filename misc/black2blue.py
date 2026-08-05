import os
import numpy as np
from PIL import Image

def convert_nonwhite_to_blue(folder_path, output_folder=None, threshold=50):
    """
    Converts every non-white pixel in images to blue (0, 0, 255) based on a threshold.
    
    Args:
        folder_path (str): Path to the folder containing images.
        output_folder (str): Path to the folder where modified images will be saved.
                             If None, it saves in the same folder.
        threshold (int): Threshold value to determine if a pixel is close to white.
                         Default is 50.
    """
    # Calculate the white threshold values
    white_threshold = 255 - threshold

    if output_folder:
        os.makedirs(output_folder, exist_ok=True)
    else:
        output_folder = folder_path

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path).convert("RGB")  # Ensure RGB mode

            # Convert image to numpy array for pixel manipulation
            img_data = np.array(img)

            # Define non-white pixels (all RGB values below the threshold)
            non_white_pixels = (img_data[:, :, 0] < white_threshold) | \
                               (img_data[:, :, 1] < white_threshold) | \
                               (img_data[:, :, 2] < white_threshold)

            # Change non-white pixels to blue
            img_data[non_white_pixels] = [0, 0, 255]

            # Save the modified image
            modified_img = Image.fromarray(img_data)
            output_path = os.path.join(output_folder, filename)
            modified_img.save(output_path)
            print(f"Modified non-white pixels to blue in {filename}")

# Example usage
folder_path = "simple/train/not_goodlabel"
output_folder = "simple/train/goodlabel"  # Or None to overwrite in the same folder
convert_nonwhite_to_blue(folder_path, output_folder)
