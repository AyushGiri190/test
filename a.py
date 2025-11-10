import requests
import json

# Replace this with the actual URL of your deployed Render service
BASE_URL = "https://test-yzgp.onrender.com"

def get_api_response(endpoint="/"):
    """
    Sends a GET request to the specified API endpoint and returns the JSON response.
    """
    url = f"{BASE_URL}{endpoint}"
    print(f"-> Calling API endpoint: {url}")

    try:
        # Send the GET request
        response = requests.get(url, timeout=10)

        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()

        # Parse the JSON response body
        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while connecting to the API: {e}")
        return None

def main():
    # 1. Test the root endpoint
    root_data = get_api_response("/")
    if root_data:
        print("\n--- Response from Root (/) ---")
        print(json.dumps(root_data, indent=4))
        print(f"\nAPI Message Status: {root_data.get('status')}")

    # 2. Test the parameterized endpoint
    name_to_greet = 12
    hello_data = get_api_response("/check-age")
    if hello_data:
        print(f"\n--- Response from /hello/{name_to_greet} ---")
        print(json.dumps(hello_data, indent=4))
        print(f"Greeting Received: {hello_data.get('message')}")

if __name__ == "__main__":
    # NOTE: Remember to install the 'requests' library first: pip install requests
    main()