import sys
from image_processor import classify_image
from utils import load_image

def main(image_path):
    image = load_image(image_path)
    label = classify_image(image)
    print(f"Predicted tissue type: {label}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_image>")
    else:
        main(sys.argv[1])
