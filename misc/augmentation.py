import os
import numpy as np
from PIL import Image
import random

# Paths to your image and label folders
images_path = 'simple/train/Image/'
labels_path = 'simple/train/Instance/'
augmented_images_path = 'simple/train/augmented_images'
augmented_labels_path = 'simple/train/augmented_labels'

# Create directories for augmented data if they don't exist
os.makedirs(augmented_images_path, exist_ok=True)
os.makedirs(augmented_labels_path, exist_ok=True)

# Define augmentation functions
def random_flip(image, label):
    if random.random() > 0.5:
        image = image.transpose(Image.FLIP_LEFT_RIGHT)
        label = label.transpose(Image.FLIP_LEFT_RIGHT)
    if random.random() > 0.5:
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
        label = label.transpose(Image.FLIP_TOP_BOTTOM)
    return image, label

def random_rotate(image, label):
    angle = random.choice([0, 90, 180, 270])
    image = image.rotate(angle)
    label = label.rotate(angle)
    return image, label

# Get image and label files with different extensions
image_files = os.listdir(images_path)
label_files = os.listdir(labels_path)

# Perform augmentations separately
for image_file in image_files:
    image_name, image_ext = os.path.splitext(image_file)  # Get name without extension
    
    # Find the corresponding label file with any extension
    label_file = next((f for f in label_files if os.path.splitext(f)[0] == image_name), None)
    if label_file is None:
        print(f"No matching label for {image_file}")
        continue

    # Load original image and label
    original_image = Image.open(os.path.join(images_path, image_file)).convert("RGB")
    original_label = Image.open(os.path.join(labels_path, label_file)).convert("L")  # Label as grayscale

    # Apply and save each augmentation individually

    # 1. Random Flip
    image, label = random_flip(original_image.copy(), original_label.copy())
    image.save(os.path.join(augmented_images_path, f"{image_name}_flip{image_ext}"))
    label.save(os.path.join(augmented_labels_path, f"{image_name}_flip{image_ext}"))

    # 2. Random Rotate
    image, label = random_rotate(original_image.copy(), original_label.copy())
    image.save(os.path.join(augmented_images_path, f"{image_name}_rotate{image_ext}"))
    label.save(os.path.join(augmented_labels_path, f"{image_name}_rotate{image_ext}"))
