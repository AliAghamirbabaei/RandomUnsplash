import json
import requests

def getImageURL():
    response = requests.get(
        "https://api.unsplash.com/photos/random/?client_id=YOUR_CLIENT_ID")
    json_response = json.loads(response.text)
    image_urls = json_response['urls']
    url = image_urls['full']
    return url

print(getImageURL())
