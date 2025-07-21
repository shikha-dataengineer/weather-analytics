import os
import requests
import pandas as pd
from google.cloud import storage

# Setup GCP credentials for Google Cloud Storage
gcp_key = os.environ.get("GCP_SERVICE_ACCOUNT_KEY")

if gcp_key:
    with open("gcp_key.json", "w") as f:
        f.write(gcp_key)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp_key.json"
else:
    print("ERROR: GCP_SERVICE_ACCOUNT_KEY not found in environment variables.")
    exit(1)

# Weather API details
API_KEY = "445a0f5faf7f919d9a94b4a30e00ed10"
CITY = "Amsterdam"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# Fetch the weather data
response = requests.get(URL)
data = response.json()

# Flatten JSON and convert to DataFrame
df = pd.json_normalize(data)

# Save as CSV
df.to_csv("amsterdam_weather.csv", index=False)

# Save as Parquet (requires pyarrow or fastparquet)
df.to_parquet("amsterdam_weather.parquet", index=False)

print("Files saved: amsterdam_weather.csv & amsterdam_weather.parquet")

# Upload CSV file to Google Cloud Storage
BUCKET_NAME = 'weather-analysis-data-bucket'
FILENAME = 'amsterdam_weather.csv'

client = storage.Client()
bucket = client.get_bucket(BUCKET_NAME)
blob = bucket.blob(f'weather/{FILENAME}') 
blob.upload_from_filename(FILENAME)

print(f"File uploaded to: gs://{BUCKET_NAME}/weather/{FILENAME}")
