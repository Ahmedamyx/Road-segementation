import os
from PIL import Image
import numpy as np
import random

# Define paths for the input and output folders
input_image_folder = "Image"
input_label_folder = "Instance"
output_image_folder = "cropped_images"
output_label_folder = "cropped_labels"

# Create output directories if they do not exist
os.makedirs(output_image_folder, exist_ok=True)
os.makedirs(output_label_folder, exist_ok=True)

# Function to crop and save images
def crop_and_save(image_path, label_path, output_image_path, output_label_path, crop_size_ratio=0.6):
    # Open the image and label
    image = Image.open(image_path)
    label = Image.open(label_path)
    
    # Convert to numpy arrays
    image_np = np.array(image)
    label_np = np.array(label)

    # Determine the crop size as 60% of the smaller dimension
    crop_size = int(crop_size_ratio * min(image_np.shape[:2]))

    # Randomly select the top-left corner for the crop
    max_x = image_np.shape[1] - crop_size
    max_y = image_np.shape[0] - crop_size
    top_left_x = random.randint(0, max_x)
    top_left_y = random.randint(0, max_y)

    # Crop both the image and the label
    cropped_image = image_np[top_left_y:top_left_y + crop_size, top_left_x:top_left_x + crop_size]
    cropped_label = label_np[top_left_y:top_left_y + crop_size, top_left_x:top_left_x + crop_size]

    # Convert back to PIL images and save
    cropped_image_pil = Image.fromarray(cropped_image)
    cropped_label_pil = Image.fromarray(cropped_label)

    cropped_image_pil.save(output_image_path)
    cropped_label_pil.save(output_label_path)

# Iterate over files in the input image folder
for image_file in os.listdir(input_image_folder):
    # Define full path for the current image and find corresponding label
    image_path = os.path.join(input_image_folder, image_file)
    label_file = os.path.splitext(image_file)[0] + '.png'  # Assuming label extension is .png
    label_path = os.path.join(input_label_folder, label_file)
    
    if os.path.exists(label_path):  # Check if the label file exists
        # Generate new filenames with "_cropped" suffix
        base_name = os.path.splitext(image_file)[0]
        cropped_image_name = f"{base_name}_cropped.jpg"  # Change extension if needed
        cropped_label_name = f"{base_name}_cropped.png"

        # Define output paths for cropped image and label
        output_image_path = os.path.join(output_image_folder, cropped_image_name)
        output_label_path = os.path.join(output_label_folder, cropped_label_name)
        
        # Perform cropping and save the results
        crop_and_save(image_path, label_path, output_image_path, output_label_path)

print("Batch cropping complete and files saved with '_cropped' suffix in cropped_images and cropped_labels folders.")
