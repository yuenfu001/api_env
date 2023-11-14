import requests
import pandas as pd
import time
from decouple import config

def get_places(api_key, location, radius, keywords=None):
    endpoint = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    places = []

    params = {
        'key': api_key,
        'location': location,
        'radius': radius,
        
    }
    if keywords:
        params['keyword'] = '|'.join(keywords)

    while True:
        response = requests.get(endpoint, params=params)
        results = response.json().get('results', [])

        for result in results:
            place_info = {
                'Name': result.get('name', ''),
                'Address': result.get('vicinity', ''),
                'Latitude': result['geometry']['location']['lat'],
                'Longitude': result['geometry']['location']['lng']
            }
            places.append(place_info)

        # Check if there is another page of results
        next_page_token = response.json().get('next_page_token')
        if not next_page_token:
            break

        # Wait for a short time before making the next request
        time.sleep(2)

        # Include the next_page_token in the next request
        params['pagetoken'] = next_page_token

    return places

api_key = config("key")
locations = [
    "9.05, 7.47", "9.055, 7.46", "9.0833, 7.4833", "9.0667, 7.4833", "9.0833, 7.4667", "9.0667, 7.45", "9.05, 7.4333",

    ]
radius = 10000  # in meters
keywords = ['limited','LTD','Limited','ltd','business']  # Change this to your specific keyword

all_places = []

for location in locations:
        places = get_places(api_key, location, radius, keywords)
        all_places.extend(places)

df = pd.DataFrame(all_places)
df.to_csv('business.csv', index=False)