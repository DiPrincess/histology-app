import joblib
import numpy as np
from skimage.transform import resize
from skimage.color import rgb2gray

MODEL_PATH = "mlp_model.pkl"

# Загрузка предобученной модели
model = joblib.load(MODEL_PATH)

def preprocess_image(image):
    gray = rgb2gray(image)
    resized = resize(gray, (64, 64), anti_aliasing=True)
    return resized.flatten()

def classify_image(image):
    vector = preprocess_image(image)
    prediction = model.predict([vector])[0]
    return prediction
