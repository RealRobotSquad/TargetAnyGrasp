import cv2
import numpy as np
from matplotlib import pyplot as plt

import os
import json

# Load the uploaded RGB and depth images
# os.getcwd()
data_dir= os.getcwd()
record_timestamps_path = os.path.join(data_dir, "out", "record_timestamps.txt")
# read timestamps
with open(record_timestamps_path, "r") as file:
    timestamps = file.read().splitlines()

# get latest timestamp
if timestamps:
    latest_timestamp = timestamps[-1]
else:
    print("No timestamps found in the file.")

OUT_PATH = os.path.join(data_dir, "out", latest_timestamp)

color_image_path = os.path.join(OUT_PATH, "color.png")
depth_image_path = os.path.join(OUT_PATH, "depth.png")

color_image = cv2.imread(color_image_path)
depth_image = cv2.imread(depth_image_path, cv2.IMREAD_UNCHANGED)

# load the mask
mask_image_path = os.path.join(OUT_PATH, "grounded_light_hqsam", "mask.jpg")
mask = cv2.imread(mask_image_path, cv2.IMREAD_GRAYSCALE)

_, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)

# 格式为 (x_min, y_min, x_max, y_max)
# with open(os.path.join(OUT_PATH, 'bounding_box.json'), 'r') as f:
#     data = json.load(f)
# scale = np.rint(np.array(data['bounding_boxes'][0])).astype(int)

# selected_region = (scale[0], scale[1], scale[2], scale[3])

# mask = np.zeros(color_image.shape[:2], dtype=np.uint8)

# x_min, y_min, x_max, y_max = selected_region
# mask[y_min:y_max, x_min:x_max] = 255

masked_rgb = cv2.bitwise_and(color_image, color_image, mask=mask)

masked_depth = np.where(mask == 255, depth_image, 0)

# Save the processed images
masked_rgb_save_path = os.path.join(OUT_PATH, "light_hqsam_mask_color.png")
masked_depth_save_path = os.path.join(OUT_PATH, "light_hqsam_mask_depth.png")

# Save masked RGB image
cv2.imwrite(masked_rgb_save_path, masked_rgb)

# Save masked depth image as 16-bit PNG (to preserve depth information)
cv2.imwrite(masked_depth_save_path, masked_depth)