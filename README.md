# ETL Project – Electric Vehicle Population Data (WA State)

This project performs Extract, Transform, and Load (ETL) operations on a dataset containing electric and alternative fuel vehicle registrations in Washington State.

## Detailed Documentation

For a complete explanation of the ETL pipeline, data model, and design decisions, refer to the [Project Wiki](https://github.com/VermaA2/-ETL-_120285/wiki/ETL-Project:-Electric-Vehicle-Population-Data-(Washington-State)).


## Dataset
**Source**: [WA Open Data Portal](https://data.wa.gov/)  
**File Name**: `Electric_Vehicle_Population_Data.csv`

## Features Explored
- Model Year
- Electric Range
- Base MSRP

## Output Tables
- `dim_vehicle_make.csv` — Unique vehicle makes (dimension table)
- `dim_vehicle_model.csv` — Unique vehicle models (dimension table)
- `dim_vehicle_location.csv` — Location details: City, State, Postal Code (dimension table)
- `fact_vehicle_registration.csv` — Vehicle registration facts including VIN, model year, MSRP, electric range, and encoded vehicle type (fact table)

## How to Run
1. Place the dataset CSV file (`Electric_Vehicle_Population_Data.csv`) in the root of the project folder.  
2. Run the script using Python 3:


python etl_120285.py
## Data Model (Star Schema)
The transformed dataset is structured using a Star Schema optimized for analytics:

Fact Table: fact_vehicle_registration.csv
Contains detailed transactional data such as VIN, Model Year, MSRP, Electric Range, and encoded Electric Vehicle Type.

## Dimension Tables:

dim_vehicle_make.csv — List of unique vehicle makes to provide descriptive context.

dim_vehicle_model.csv — List of unique vehicle models for detailed classification.

dim_vehicle_location.csv — Location data including city, state, and postal code to support geographic analysis.

## Star Schema Diagram
<p align="center">
  <img src="https://github.com/VermaA2/-ETL-_120285/blob/main/star_schema.png" alt="Star Schema Diagram" width="600">
</p>

## Summary Statistics
As part of the ETL exploration, summary statistics for key features are generated and saved in summary_statistics.csv. This file includes count, mean, standard deviation, min, max, and quartiles for:

Electric Range
Base MSRP
Model Year

These statistics help understand data distribution and highlight quality issues such as zero values or outliers.

## Summary Statistics (CSV)
summary_statistics.csv — Summary statistics for electric range, base MSRP, and model year.
