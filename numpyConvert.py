import os
import numpy as np
from PIL import Image

train_images_dir = "train_images"
train_hash_dir = "train_hash"

os.makedirs(train_hash_dir, exist_ok=True)

def image_to_numpy_array(image_path):
    """Convert image to a numpy array."""
    with Image.open(image_path) as img:
        img = img.convert("RGB") 
        img_array = np.array(img)
        # print("this is the shape of the image array", np.array(img))
        return img_array

for folder in os.listdir(train_images_dir):
    folder_path = os.path.join(train_images_dir, folder)
    if not os.path.isdir(folder_path):
        continue
    hash_folder_path = os.path.join(train_hash_dir, folder)
    os.makedirs(hash_folder_path, exist_ok=True)
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if not filename.lower().endswith('.jpg'):
            continue
        try:
            img_array = image_to_numpy_array(file_path)
            hash_filename = os.path.splitext(filename)[0] + ".npy"
            hash_file_path = os.path.join(hash_folder_path, hash_filename)
            # Save as numpy array
            np.save(hash_file_path, img_array)
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            continue
print("completed")