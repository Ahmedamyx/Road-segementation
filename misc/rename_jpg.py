import os
from PIL import Image

def convert_jpg_to_png(folder_path, output_folder):
    """
    Converts all .jpg files in a folder to .png format.
    
    Args:
        folder_path (str): Path to the folder containing .jpg files.
        output_folder (str): Path to the folder where .png files will be saved. 
                             If None, it saves in the same folder.
    """
    if output_folder:
        os.makedirs(output_folder, exist_ok=True)
    else:
        output_folder = folder_path

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".jpg"):
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path)

            # Save as .png in the output folder
            png_filename = os.path.splitext(filename)[0] + ".png"
            png_path = os.path.join(output_folder, png_filename)
            img.save(png_path, "PNG")
            print(f"Converted {filename} to {png_filename}")

# Example usage
folder_path = "simple/train/goodlabel"
output_folder = "simple/train/Instance"  # Or None to save in the same folder
convert_jpg_to_png(folder_path, output_folder)
