from skimage.io import imread
import numpy as np

def load_image(image_path):
    try:
        image = imread(image_path)
        return image
    except Exception as e:
        print(f"Error loading image: {e}")
        return np.zeros((64, 64))
