import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')

api_endpoint = 'https://api.openai.com/v1/images/generations'

prompt_description = 'a photo of a happy corgi puppy sitting and facing forward, studio light, longshot'

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
}

data = {
    'prompt': prompt_description,
    'n': 1,
    'size': '1024x1024'
}

response = requests.post(api_endpoint, headers=headers, json=data)

if response.status_code == 200:
    image_url = response.json()['data'][0]['url']
    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        with open('output.jpg', 'wb') as file:
            file.write(image_response.content)
            print('Image saved as output.jpg')
    else:
        print('Failed to fetch the image from the URL')
else:
    print('Failed to make a request to the API')

