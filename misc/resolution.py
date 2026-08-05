import cv2
import os

def quadruple_resolution(input_folder, output_folder):
    """
    Quadruples the resolution of all images in a folder and saves them to another folder.
    
    Parameters:
        input_folder (str): Path to the folder containing input images.
        output_folder (str): Path to the folder to save the output images.
    """
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Process each image in the input folder
    for filename in os.listdir(input_folder):
        # Construct full file path
        input_path = os.path.join(input_folder, filename)

        # Check if it's an image file
        if not os.path.isfile(input_path) or not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            continue

        # Load the image
        img = cv2.imread(input_path)
        if img is None:
            print(f"Warning: Could not load image {filename}. Skipping.")
            continue

        # Get original dimensions
        original_height, original_width = img.shape[:2]

        # Calculate new dimensions (quadruple resolution)
        new_width = original_width * 4
        new_height = original_height * 4

        # Resize the image using cubic interpolation
        img_high_res = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_CUBIC)

        # Construct output file path
        output_path = os.path.join(output_folder, filename)

        # Save the high-resolution image
        cv2.imwrite(output_path, img_high_res)
        print(f"Processed and saved: {filename} with resolution {new_width}x{new_height}")

# Example usage
input_folder = "badres"  # Replace with your input folder path
output_folder = "goodres"  # Replace with your output folder path
quadruple_resolution(input_folder, output_folder)
