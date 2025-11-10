from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import Adam
from PIL import Image

IMG_SIZE = 64  # Image input size used in training

def preprocess_image(img):
    # Ensure the image is in RGB
    if img.mode != "RGB":
        img = img.convert("RGB")
    
    # Resize the image to match model input size
    img = img.resize((IMG_SIZE, IMG_SIZE))
    
    # Convert to numpy array
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize to [0, 1]
    
    return img_array

def predict_image_brain(input_image):
    # Load the trained model
    model = load_model("./models/model_brain_cancer.h5")
    model.compile(optimizer=Adam(learning_rate=0.000006), loss='binary_crossentropy', metrics=['accuracy'])

    # Load image if input is a path
    if isinstance(input_image, str):
        img = Image.open(input_image)
    else:
        img = input_image  # Already a PIL.Image.Image

    # Preprocess image
    processed_img = preprocess_image(img)

    # Predict
    predictions = model.predict(processed_img)
    confidence = predictions[0][0]
    predicted_label = "No Tumor" if confidence > 0.5 else "Tumor Detected"

    print(f"Prediction: {predicted_label} (Confidence: {confidence:.4f})")
    return predicted_label
