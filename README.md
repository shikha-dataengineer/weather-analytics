# weather-analytics

📌 Overview

This project demonstrates a serverless, scalable ETL pipeline that fetches real-time weather data from the OpenWeatherMap API(https://openweathermap.org/api), processed in Google Colab, and stored the structured data into Google Cloud Storage (GCS) in parquet or csv format.

## 🚀 Project Workflow

1. Fetch live weather data from OpenWeatherMap API (e.g., Amsterdam).
2. Process and structure the data using Python & Pandas in Google Colab.
3. Save the result locally in Colab.
4. Upload the output file (CSV or Parquet) to a GCS bucket.

 ## 🛠️ Technologies Used

- **Google Colab** – Used to write and execute the Python ETL script.
- **OpenWeatherMap API** – Source for real-time weather data.
- **Pandas** – For simple data processing and transformation.
- **Google Cloud Storage (GCS)** – Storage location for final CSV/Parquet files.
- **Google Cloud Python Client** – To interact with GCS directly from Colab.

## GCS Path

-- gs://weather-analysis-data-bucket/weather/amsterdam_weather.csv
