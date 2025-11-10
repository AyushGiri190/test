from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import Adam
from PIL import Image

IMG_SIZE = 128  # Image input size used in training

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

def predict_image_breast(input_image):
    # Load the trained breast cancer model
    model = load_model("./models/vgg16.h5", compile=False)
    model.compile(optimizer=Adam(learning_rate=0.000006), loss='categorical_crossentropy', metrics=['accuracy'])

    # Load image if input is a path
    if isinstance(input_image, str):
        img = Image.open(input_image)
    else:
        img = input_image  # Already a PIL.Image.Image

    # Preprocess image
    processed_img = preprocess_image(img)

    # Predict
    predictions = model.predict(processed_img)
    predicted_index = np.argmax(predictions[0])
    labels = ["Normal", "Cancer", "Cancer"]
    predicted_label = labels[predicted_index]
    confidence = predictions[0][predicted_index]

    print(f"Prediction: {predicted_label} (Confidence: {confidence:.4f})")
    return predicted_label
