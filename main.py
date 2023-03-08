# Import the required modules
from PIL import Image
import os
import glob

# Set the source and destination folders
source_folder = "original_images" # Change this to your source folder name
destination_folder = "converted_images" # Change this to your destination folder name

# Create the destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Loop through the source folder and convert each image
for image_file in glob.glob(os.path.join(source_folder, "*.*")):
    # Get the file name and extension
    file_name, file_ext = os.path.splitext(image_file)
    # Check if the file is a png or jpg image
    if file_ext.lower() in [".png", ".jpg"]:
        # Open the image with Pillow
        image = Image.open(image_file)
        # Set the new file name and path
        new_file_name = os.path.basename(file_name) + ".webp"
        new_file_path = os.path.join(destination_folder, new_file_name)
        # Save the image as webp with lossless compression
        image.save(new_file_path, format="WebP", lossless=True)
        # Print a message
        print(f"Converted {image_file} to {new_file_path}")