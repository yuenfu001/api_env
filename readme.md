# Business List Generator

### This Python script utilizes the Google Places API to generate a list of businesses based on specified locations and keywords. The script retrieves information about businesses within a given radius of each location and filters the results based on predefined keywords.

## Prerequisites

- Before using the script, make sure you have the following:

- Python installed on your machine

- requests, pandas, and python-decouple Python packages. You can install them using:

    - bash

    - pip install requests pandas python-decouple (I used poetry venv but you can use pip)

    - Google Places API key. You can obtain one by following the Google Cloud Platform documentation.

Configuration

    Clone the repository:

    bash

git clone https://github.com/yuenfu001/api_env.git

Create a .env file in the project root and add your Google Places API key:

makefile

    GOOGLE_API_KEY=your_api_key_here

Usage

    Open the main.py file and modify the locations and keywords variables to suit your specific requirements.

    Run the script on cmd or powershell or bash:

    python api.py or py api.py

    The script will generate a CSV file named business_list.csv containing information about the businesses that match the specified keywords.

Script Details

    The script iterates over the provided locations, makes requests to the Google Places API, and retrieves relevant information about businesses.
    The results are filtered based on the specified keywords, and the final list is stored in a CSV file.

Feel free to customize the script according to your needs, such as adjusting the radius, changing the keywords, or adding more locations.