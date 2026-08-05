import os

def find_extra_file(folder1, folder2):
    # List all files in both folders (ignoring extensions)
    folder1_files = set(os.path.splitext(f)[0] for f in os.listdir(folder1))
    folder2_files = set(os.path.splitext(f)[0] for f in os.listdir(folder2))
    
    # Find the extra file
    extra_file_in_folder1 = folder1_files - folder2_files
    extra_file_in_folder2 = folder2_files - folder1_files

    # Output the result
    if extra_file_in_folder1:
        print(f"The extra file in folder1 is: {extra_file_in_folder1}")
    elif extra_file_in_folder2:
        print(f"The extra file in folder2 is: {extra_file_in_folder2}")
    else:
        print("Both folders have the same files.")

# Specify the paths to your folders
folder1_path = 'simple/train/Image'
folder2_path = 'simple/train/Instance'

# Run the function
find_extra_file(folder1_path, folder2_path)
