import os
from PIL import Image

train_images_dir = "train_images"
target_size = (480, 640)
to_flip_size = (640, 480)
flipped_count = 0

for folder in os.listdir(train_images_dir):
    folder_path = os.path.join(train_images_dir, folder)
    if not os.path.isdir(folder_path):
        continue
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if not filename.lower().endswith('.jpg'):
            continue
        try:
            with Image.open(file_path) as img:
                if img.size == to_flip_size:
                    # Rotate 90 degrees to get (480, 640)
                    img_rotated = img.rotate(90, expand=True)
                    img_rotated.save(file_path)
                    flipped_count += 1
        except Exception:
            continue

print(f"Flipped {flipped_count} images from {to_flip_size} to {target_size}.")