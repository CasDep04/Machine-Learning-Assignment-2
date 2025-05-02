import os
import pandas as pd

# Path to meta_train.csv
meta_file = "meta_train.csv"
train_images_dir = "train_images"

# Read the metadata CSV
try:
    df = pd.read_csv(meta_file)
    print(f"Successfully loaded {meta_file} with {len(df)} entries")
except Exception as e:
    print(f"Error loading {meta_file}: {e}")
    exit(1)

# Count statistics
total_files = len(df)
missing_files = 0
wrong_directory_files = 0

# Check each file
for index, row in df.iterrows():
    filename = row['image_id']
    label = row['label']
    
    # Expected path based on label
    expected_path = os.path.join(train_images_dir, label, filename)
    
    # Check if file exists
    if not os.path.exists(expected_path):
        missing_files += 1
        print(f"Missing file: {expected_path}")
        
        # Check if it exists in a different directory
        found = False
        for folder in os.listdir(train_images_dir):
            if folder == label:
                continue
            wrong_path = os.path.join(train_images_dir, folder, filename)
            if os.path.exists(wrong_path):
                wrong_directory_files += 1
                print(f"  Found in wrong directory: {wrong_path}")
                found = True
                break
        
        if not found:
            print(f"  File not found anywhere in {train_images_dir}")

# Print summary
print("\nSummary:")
print(f"Total files listed in metadata: {total_files}")
print(f"Missing files: {missing_files}")
print(f"Files in wrong directory: {wrong_directory_files}")
print(f"Correctly placed files: {total_files - missing_files}")

if missing_files == 0:
    print("\nAll files from metadata exist in the correct directories!")
else:
    print(f"\n{missing_files} files from metadata are misplaced or missing.")