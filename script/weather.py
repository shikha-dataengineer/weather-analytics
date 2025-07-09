import requests
import pandas as pd

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

from google.colab import auth
auth.authenticate_user()

from google.cloud import storage
import pandas as pd

# Replace with your bucket name
BUCKET_NAME = 'weather-analysis-data-bucket'
FILENAME = 'amsterdam_weather.csv'

# Save sample DataFrame to CSV
df = pd.DataFrame({'city': ['Amsterdam'], 'temp': [20.5]})
df.to_csv(FILENAME, index=False)

client = storage.Client()
bucket = client.get_bucket(BUCKET_NAME)
blob = bucket.blob(f'weather/{FILENAME}')  # Optional: set folder path
blob.upload_from_filename(FILENAME)

print(f"File uploaded to: gs://{BUCKET_NAME}/weather/{FILENAME}")
