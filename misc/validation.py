import os
import random
import shutil

def take_matched_files(input_folder1, input_folder2, output_folder1, output_folder2, percentage=0.15):
    # Create output folders if they do not exist
    os.makedirs(output_folder1, exist_ok=True)
    os.makedirs(output_folder2, exist_ok=True)
    
    # List all files in both folders
    files1 = [f for f in os.listdir(input_folder1) if os.path.isfile(os.path.join(input_folder1, f))]
    files2 = [f for f in os.listdir(input_folder2) if os.path.isfile(os.path.join(input_folder2, f))]
    
    # Create dictionaries to map base names to full file names
    files1_dict = {os.path.splitext(f)[0]: f for f in files1}
    files2_dict = {os.path.splitext(f)[0]: f for f in files2}
    
    # Find common base names
    common_base_names = list(set(files1_dict.keys()) & set(files2_dict.keys()))
    
    # Determine the number of files to select
    num_files_to_select = max(1, int(len(common_base_names) * percentage))
    
    # Randomly select files
    selected_base_names = random.sample(common_base_names, num_files_to_select)
    
    for base_name in selected_base_names:
        file1 = files1_dict[base_name]
        file2 = files2_dict[base_name]
        
        # Move the matched files to their respective output folders
        shutil.move(os.path.join(input_folder1, file1), os.path.join(output_folder1, file1))
        shutil.move(os.path.join(input_folder2, file2), os.path.join(output_folder2, file2))

    print(f"Moved {len(selected_base_names)} files to the output folders.")

# Example usage
input_folder1 = "Simple/Train/Image"
input_folder2 = "Simple/Train/Instance"
output_folder1 = "verify_image"
output_folder2 = "verify_label"

take_matched_files(input_folder1, input_folder2, output_folder1, output_folder2)
