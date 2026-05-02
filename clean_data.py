import os
from PIL import Image

def clean_folder(folder):
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        try:
            img = Image.open(path).convert("RGB")
            img.save(path)
        except:
            os.remove(path)

base_dir = "dataset"

for split in ["train", "val", "test"]:
    for cls in ["cats", "dogs"]:
        clean_folder(os.path.join(base_dir, split, cls))