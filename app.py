import os
from flask import Flask, jsonify, request

# The Flask application instance
app = Flask(__name__)

# --- Simple API Endpoint ---

@app.route('/', methods=['GET'])
def home():
    """
    A simple home route to confirm the API is running.
    """
    return jsonify({
        "status": "success",
        "message": "Welcome to the Simple Flask API deployed on Render!",
        "guide": "Try navigating to /hello/<your_name>",
        "environment_port": os.environ.get('PORT', 'Not set (Default is 10000 on Render)')
    })

@app.route('/hello/<name>', methods=['GET'])
def greet_user(name):
    """
    An example route that takes a name parameter from the URL.
    """
    return jsonify({
        "status": "success",
        "greeting": f"Hello, {name}! Your API is running perfectly.",
        "note": "This demonstrates successful routing and parameter handling."
    })

# --- Main Entry Point ---

# Render automatically sets the PORT environment variable (usually to 10000).
# Gunicorn (specified in requirements.txt) will automatically detect and use this port
# when running the command: gunicorn app:app

# We only run the app directly if we are in a local development environment.
if __name__ == '__main__':
    # Use 5000 for local development if PORT is not set
    port = int(os.environ.get('PORT', 5000))
    print(f"Running locally on port {port}")
    app.run(debug=True, host='0.0.0.0', port=port)