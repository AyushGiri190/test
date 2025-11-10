import requests
import json

# Replace this with the actual URL of your deployed Render service
BASE_URL = "https://test-yzgp.onrender.com"


# Replace this with your local URL or your Render URL once deployed
URL = "https://test-yzgp.onrender.com/checkbraincancer"   # For local testing
# URL = "https://your-render-app.onrender.com/checkbraincancer"  # For Render deployment

# Path to a test image file on your computer
IMAGE_PATH = "checknotumour.jpg"

# Open the image in binary mode and send as multipart/form-data
with open(IMAGE_PATH, "rb") as image_file:
    files = {"image": image_file}
    response = requests.post(URL, files=files)

# Display response from your Flask app
print("Status Code:", response.status_code)
try:
    print("Response JSON:", response.json())
except Exception:
    print("Raw Response:", response.text)
