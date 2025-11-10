from tensorflow.keras.models import load_model
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import Adamax
from PIL import Image

def preprocess_image(img):
    if img.mode != "RGB":
        img = img.convert("RGB")
    # img = img.resize((300, 300))  # Resize image
    img_array = image.img_to_array(img)  # Convert to array
    img_array = np.expand_dims(img_array, axis=0)  # Expand dims to match batch shape
    img_array /= 255.0  # Normalize pixel values
    
    return img_array



def predict_image_tuber(img_path):
    # img = Image.open(img_path)  # Load image from file path
    # processed_img = preprocess_image(img)
    model = load_model("./models/model_tuberculosis.h5",compile = False) 
    model.compile(optimizer=Adamax(learning_rate=0.0005), loss='categorical_crossentropy', metrics=['accuracy']) 
    processed_img = preprocess_image(img_path)  # Preprocess image
    predictions = model.predict(processed_img)  # Get prediction
     # Convert prediction to class
    if predictions[0][0] > 0.5:
        predicted_label = "Tuberculosis"
    else:
        predicted_label = "Normal"

    print(f"Prediction: {predicted_label}")
    return predicted_label
    
# predict_image_tuber("./Tuberculosis-1.png")