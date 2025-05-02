import os
from PIL import Image

train_images_dir = "train_images"
not_jpg_count = 0
corrupted_count = 0

for folder in os.listdir(train_images_dir):
    folder_path = os.path.join(train_images_dir, folder)
    if not os.path.isdir(folder_path):
        continue
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        # Check if file is a jpg
        if not filename.lower().endswith('.jpg'):
            not_jpg_count += 1
            continue
        # Try to open the image to check for corruption
        try:
            with Image.open(file_path) as img:
                img.load()
                
        except Exception:
            corrupted_count += 1

print(f"Files not .jpg: {not_jpg_count}")
print(f"Corrupted .jpg files: {corrupted_count}")