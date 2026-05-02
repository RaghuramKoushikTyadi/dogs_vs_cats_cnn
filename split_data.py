import os
import shutil
import random

source_dir = "dataset_raw"
base_dir = "dataset"

classes = ["Cat", "Dog"]

split_ratio = (0.7, 0.15, 0.15)

for split in ["train", "val", "test"]:
    for cls in classes:
        os.makedirs(os.path.join(base_dir, split, cls.lower() + "s"), exist_ok=True)

for cls in classes:
    src_folder = os.path.join(source_dir, cls)
    images = os.listdir(src_folder)
    random.shuffle(images)

    total = len(images)
    train_end = int(total * split_ratio[0])
    val_end = int(total * (split_ratio[0] + split_ratio[1]))

    splits = {
        "train": images[:train_end],
        "val": images[train_end:val_end],
        "test": images[val_end:]
    }

    for split, files in splits.items():
        for file in files:
            src = os.path.join(src_folder, file)
            dst = os.path.join(base_dir, split, cls.lower() + "s", file)
            shutil.copy(src, dst)