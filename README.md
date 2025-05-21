# ENGG2112_MajorProject
The repository to upload code and update each week for the ENGG2112 Major Project for Group 6

**Raw and cleaned .csv files can be found in the shared google drive folder:**
https://drive.google.com/drive/folders/1opZFx88zn5x6jilQz0_piGYU5P04zR7_?usp=sharing

**cleaned data files should be stored in a folder named "datasets_cleaned" within your local repo directory.**

# Traffic Prediction Using Historical and Weather Data

**ENGG2112 Major Project – Group 6**

This project aims to predict traffic conditions based on historical traffic records and weather data using data-driven and machine learning approaches. This is a group project developed by Group 6.

## 🚦 Project Overview

Urban traffic congestion is a critical problem in modern cities. In this project, we seek to build a predictive model that estimates traffic flow or congestion levels based on historical traffic patterns and weather conditions. Our goal is to analyze how variables such as rain and temperature conditions affect traffic and to use that data to improve prediction accuracy.

## 📁 Repository Structure
├── data pre-procesing/
│ ├── Data Pre-Processing.ipynb # cleaning raw csv files obtained from Transport Open Data
│ └── Weather Data Lookup # use API to get relevant weather data from SILO
├── datasets/ # raw datasets
| ├── .gitkeep # to ensure folder is kept in repository
| ├── road_traffic_counts_hourly_permanent0.csv # not included in repository
| ├── road_traffic_counts_hourly_permanent1.csv # not included in repository
| ├── road_traffic_counts_hourly_permanent2.csv # not included in repository
| ├── road_traffic_counts_hourly_permanent3.csv # not included in repository
│ └── road_traffic_counts_station_reference.csv # not included in repository
├── datastes_cleaned/ # cleaned datasets for model use
| ├── .gitkeep # to ensure folder is kept in repository
│ ├── trafficData.csv # cleaned and collated traffic counts
│ ├── trafficStations.csv # cleaned traffic station reference
│ └── weatherData.csv # weather data retrieved from SILO API
├── documentation/ # documentation on datasets from Transport Open Data
│ ├── classified-roads-schedule.pdf # outlines classifications of roads
│ └── RMS Dataset Documentation - NSW Traffic Volume Counts.pdf # outlines features and datatypes of raw datasets
├── progress reports/
│ ├── ENGGG2112 Weekly Progress Report (Week 9).docx # week 9 progress report
│ ├── ENGGG2112 Weekly Progress Report (Week 10).docx # week 10 progress report
│ └── ENGGG2112 Weekly Progress Report (Week 11).docx # week 11 progress report
├── sub-problem A models/
| ├── GradientBoostingModel.ipynb # XGBoost model
│ ├── LightGBM_model.ipynb # LightGBM model
│ ├── MLP.ipynb # MLP model
│ └── RandomForest.ipynb # Random Forest model
├── sub-problem A models/
│ └── Sub-Problem-B (RF and SVR).ipynb # Random Forest and SVR models
├── .gitignore # files and folders to ignore in version control
└── README.md # project overview

> **Note:** The datasets are too large to store on GitHub. Please use the link below to access them.

## 🔗 Access to Datasets

You can download the datasets from our shared Google Drive folder:

📂 [ENGG2112 Major Project Files - Google Drive](https://drive.google.com/drive/folders/1opZFx88zn5x6jilQz0_piGYU5P04zR7_?usp=sharing)
