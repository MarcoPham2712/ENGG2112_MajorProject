# ENGG2112 Major Project – Group 6

> **Note:** The datasets are too large to store on GitHub. Please use the link below to access them.

🔗 [ENGG2112 Major Project Files - Google Drive](https://drive.google.com/drive/folders/1opZFx88zn5x6jilQz0_piGYU5P04zR7_?usp=sharing)

## 👥 Team Responsibilities

### Sub-Problem A Tasks

| **Mahadi** | **Marco**    | **Hong**          | **Daniel**                |
|------------|--------------|-------------------|---------------------------|
|            | LightGBM     | Random Forest     | Traffic data cleaning     |
|            | XGBoost      | MLP               |                           |

### Sub-Problem B Tasks

| **Mahadi**        | **Marco**   | **Hong** | **Daniel**              |
|-------------------|-------------|----------|-------------------------|
| Random Forest     | XGBoost     | MLP      | Weather data collection |
| Linear Regression |             |          |                         |

## 📁 Repository Structure
```
├── data pre-procesing/
│   ├── Data Pre-Processing.ipynb                                   # cleaning raw csv files obtained from Transport Open Data
│   └── Weather Data Lookup                                         # use API to get relevant weather data from SILO
├── datasets/ 
|   ├── .gitkeep                                                    # to ensure folder is kept in repository
|   ├── road_traffic_counts_hourly_permanent0.csv                   # not included in repository
|   ├── road_traffic_counts_hourly_permanent1.csv                   # not included in repository
|   ├── road_traffic_counts_hourly_permanent2.csv                   # not included in repository
|   ├── road_traffic_counts_hourly_permanent3.csv                   # not included in repository
│   └── road_traffic_counts_station_reference.csv                   # not included in repository
├── datasets_cleaned/
|   ├── .gitkeep                                                    # to ensure folder is kept in repository
│   ├── trafficData.csv                                             # not included in repository
│   ├── trafficStations.csv                                         # not included in repository
│   └── weatherData.csv                                             # not included in repository
├── documentation/
│   ├── classified-roads-schedule.pdf                               # outlines classifications of roads
│   └── RMS Dataset Documentation - NSW Traffic Volume Counts.pdf   # outlines features and datatypes of raw datasets
├── progress reports/
│   ├── ENGGG2112 Weekly Progress Report (Week 9).docx              # week 9 progress report
│   ├── ENGGG2112 Weekly Progress Report (Week 10).docx             # week 10 progress report
│   └── ENGGG2112 Weekly Progress Report (Week 11).docx             # week 11 progress report
├── sub-problem A models/
|   ├── GradientBoostingModel.ipynb                                 # XGBoost model
│   ├── LightGBM_model.ipynb                                        # LightGBM model
│   ├── MLP.ipynb                                                   # MLP model
│   └── RandomForest.ipynb                                          # Random Forest model
├── sub-problem A models/
│   └── Sub-Problem-B (RF and SVR).ipynb                            # Random Forest and SVR models
├── .gitignore                                                      # files and folders to ignore in version control
└── README.md                                                       # project overview
```
