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
                'Longitude': result['geometry']['location']['lng'],
                'Rating': result.get('rating', None),
                'PriceLevel': result.get('price_level', None)
            }
            places.append(place_info)

        # Check if there is another page of results
        next_page_token = response.json().get('next_page_token')
        if not next_page_token:
            break

        # Wait for a short time before making the next request
        time.sleep(1)

        # Include the next_page_token in the next request
        params['pagetoken'] = next_page_token

    return places

if __name__ == "__main__":
    api_key = config("key")
    locations = [
        "9.095747029786386, 7.48804969180376"

        ]
    # Maitama: 9.095747029786386, 7.48804969180376
    # Jabi: 9.053617,7.432077

    # , "9.055, 7.46", "9.0833, 7.4833", "9.0667, 7.4833", "9.0833, 7.4667", "9.0667, 7.48", "9.05, 7.4333",
    radius = 50000  # in meters
    keywords = ["hotel","Lounge", "restaurant","club","suites","resort","amala","joint" ]  # Change this to your specific keyword

    all_places = []

    for location in locations:
            places = get_places(api_key, location, radius, keywords)
            all_places.extend(places)

    df = pd.DataFrame(all_places)
    df.to_csv('flex.csv', index=False)