from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
from lungcancer import predict_image_lung
#from tuberculosis import predict_image_tuber
from braincancer import predict_image_brain
from Breast_cancer import predict_image_breast
#from response import get_chatbot_response
import os
#from utils.chat_history import chat_history

app = Flask(__name__)
CORS(app)  # Allow all origins (for development)
UPLOAD_FOLDER = "./uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=["POST","GET"])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"message": "No file part"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400
    image = Image.open(file) 
    # You can save the file if needed
    file.save(f"./{file.filename}")

    return jsonify({"message": "Image received successfully"}), 200



@app.route('/checklungcancer', methods=["POST","GET"])
def upload_image_lung():
    if 'image' not in request.files:
        return jsonify({"message": "No file part"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400
    # image = Image.open(file) 
    image = Image.open(file)  # Open image
    image = image.resize((224, 224))
    # You can save the file if needed
    # file.save(f"./{file.filename}")
    save_path = os.path.join(UPLOAD_FOLDER, file.filename)
    absolute_path = os.path.abspath(save_path)
    image.save(save_path)
    print(image)
    prediction = predict_image_lung(absolute_path)
    # prediction="hello"
    return jsonify({"message": f"{prediction}"}), 200



'''
@app.route('/checktubercancer', methods=["POST","GET"])
def upload_image_tuber():
    if 'image' not in request.files:
        return jsonify({"message": "No file part"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400
    # image = Image.open(file) 
    image = Image.open(file)  # Open image
    image = image.resize((300, 300))
    # You can save the file if needed
    # file.save(f"./{file.filename}")
    save_path = os.path.join(UPLOAD_FOLDER, file.filename)
    image.save(save_path)
    # prediction="hello"
    prediction = predict_image_tuber(image)
    return jsonify({"message": f"{prediction}"}), 200
'''

@app.route('./test',method=["POST","GET"])
def testing():
    api = os.environ.get("testing")
    return jsonify({"message":f"{api}"})

@app.route('/checkbraincancer', methods=["POST","GET"])
def upload_image_brain():
    if 'image' not in request.files:
        return jsonify({"message": "No file part"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400
    # image = Image.open(file) 
    image = Image.open(file.stream)  # Open image
    image = image.resize((64, 64))
    # You can save the file if needed
    prediction = predict_image_brain(image)
    # prediction="hello"
    return jsonify({"message": f"{prediction}"}), 200



@app.route('/checkbreastcancer', methods=["POST","GET"])
def upload_image_breast():
    if 'image' not in request.files:
        return jsonify({"message": "No file part"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400
    # image = Image.open(file) 
    image = Image.open(file.stream)  # Open image
    image = image.resize((300, 300))
    # You can save the file if needed
    save_path = os.path.join(UPLOAD_FOLDER, file.filename)
    image.save(save_path)
    
    prediction = predict_image_breast(image)
    # prediction="hello"
    return jsonify({"message": f"{prediction}"}), 200

'''
@app.route('/chatbot', methods=["POST","GET"])
def chatbot():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({"error": "Missing 'message' in request body"}), 400

    user_message = data['message']
    if not isinstance(user_message, str) or not user_message.strip():
        return jsonify({"error": "'message' must be a non-empty string"}), 400
    bot_reply = get_chatbot_response(user_message,chat_history)
    # Dummy chatbot logic — echo back the message with some prefix
   # bot_reply = f"You said: {user_message}. This is a demo response."

    # TODO: Replace the above with your AI/chatbot logic

    return jsonify({"reply": bot_reply})

'''

@app.route("/check-age", methods=["POST","GET"])
def check_age():
    #data = request.get_json()
    #age = data.get("age", 0)
    age =12 
    if age >= 18:
        return jsonify({"message": "✅ You are eligible to vote!"})
    else:
        return jsonify({"message": "❌ You are not eligible to vote!"})
if __name__ == '__main__':
    # Use 5000 for local development if PORT is not set
    port = int(os.environ.get('PORT', 5000))
    print(f"Running locally on port {port}")
    app.run(debug=True, host='0.0.0.0', port=port)
