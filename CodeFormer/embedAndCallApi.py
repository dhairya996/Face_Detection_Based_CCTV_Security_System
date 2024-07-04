import os
import base64
from deepface import DeepFace
import requests
import json
import ast

api_url="https://miniproj-frontend.onrender.com"

def get_image_and_embeddings(image_path):
    # Get the filename from the image path
    img_filename = os.path.basename(image_path)

    # Remove the extension from the filename
    img_name, _ = os.path.splitext(img_filename)

    # Get embeddings
    embeddings = DeepFace.represent(image_path, model_name="Facenet", enforce_detection=False)

    embeddings_only = embeddings[0]['embedding']

    # Convert image to base64
    with open(image_path, "rb") as img_file:
        base64_image = base64.b64encode(img_file.read()).decode('utf-8')


            # Prepare the JSON object
    json_data = {
        "file": base64_image,
        "embeddings": embeddings_only
    }

    try:
        # Send POST request to the API
        response = requests.post(api_url, json=json_data)

        # Check the response status
        if response.status_code == 200:
            print("POST request successful.")
            print("Response:")
            print(response.json())
        else:
            print("POST request failed with status code:", response.message)
    except Exception as e:
        print("An error occurred:", str(e))

  







































