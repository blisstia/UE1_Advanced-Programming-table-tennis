import torch
from PIL import Image
import os
from os import listdir
from os.path import isfile, join
image_folder = "/Users/tia/Desktop/UE1_projet/dataset/test/demo_images"

print(f"Setup complete. Using torch {torch.__version__} ({torch.cuda.get_device_properties(0).name if torch.cuda.is_available() else 'CPU'})")

image_files = [f for f in listdir(image_folder) if isfile(join(image_folder, f))]

cur_dir = os.path.dirname(os.path.realpath(__file__))
path_to_yolo5 = cur_dir
path_to_weights = 'yolov5s.pt'
# Model
model = torch.hub.load(path_to_yolo5,
                               'custom',
                               path=path_to_weights,
                               source='local')
model.classes = [32]
imgs = []
for image in image_files:
# Images
    img = Image.open(f"{image_folder}/{image}")
    imgs.append(img)  # batched list of images

# Inference
print("working...")
result = model(imgs)

result.save()
