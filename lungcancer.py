from tensorflow.keras.models import load_model
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import Adamax



'''Add Code to preprocess the image ready to be predicted  '''
def preprocess_image(img):
    img = image.load_img(img, target_size=(224, 224))  # Load and resize image
    img_array = image.img_to_array(img)  # Convert to array
    img_array = np.expand_dims(img_array, axis=0)  # Expand dims to match batch shape
    #img_array = img_array / 255.0  # Normalize if required
    return img_array



def predict_image_lung(img_path):
    #img_path = "/content/lung_colon_image_set/lung_image_sets/lung_scc/lungscc1.jpeg"
    model = load_model("./models/model_lung_cancer.h5",compile = False) 
    model.compile(optimizer=Adamax(learning_rate=0.0005), loss='categorical_crossentropy', metrics=['accuracy'])
    processed_img = preprocess_image(img_path)
    predictions = model.predict(processed_img)
    predicted_class = np.argmax(predictions, axis=1)[0]  # Get class index
    print(predicted_class)
    # Assuming you used ImageDataGenerator, retrieve class labels
    class_indices ={0:"Lung Cancer Type-ACA",1:"Normal",2:"Lung Cancer Type-SCC"}  # Dictionary mapping class names to indices
    predicted_label = class_indices[predicted_class]  # Get class name
    print(f"Predicted Class: {predicted_label}")
    return predicted_label

# predict_image_lung("./lungACA.jpeg")
