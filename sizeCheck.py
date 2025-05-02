import os
from PIL import Image

train_images_dir = "train_images"
size_counts = {}
total_images = 0

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
                size = img.size
                total_images += 1
                size_counts[size] = size_counts.get(size, 0) + 1
        except Exception:
            continue

print(f"Total .jpg images checked: {total_images}")
print(f"Number of unique image sizes: {len(size_counts)}")
print("Image size counts (width, height):")
for size, count in size_counts.items():
    print(f"{size}: {count}")