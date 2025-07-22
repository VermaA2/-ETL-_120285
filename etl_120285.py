"""
ETL Pipeline for Washington State Electric Vehicle Dataset

This script extracts, explores, cleans, transforms, and loads the dataset into
dimension and fact tables for analytics using a star schema.
"""

import pandas as pd

# Step 1: Extract - Load dataset from CSV
df = pd.read_csv("Electric_Vehicle_Population_Data.csv")

# Step 2: Explore - Print dataset columns and summary statistics for key features
summary_stats = df[['Electric Range', 'Base MSRP', 'Model Year']].describe()
print("Summary Statistics:")
print(summary_stats)

# Export summary statistics to CSV for documentation
summary_stats.to_csv('summary_statistics.csv')
print("Summary statistics exported to summary_statistics.csv")

# Step 3: Clean - Drop rows with missing key numeric metrics to ensure data quality
df = df.dropna(subset=['Electric Range', 'Base MSRP'])

# Fill missing values in 'Electric Vehicle Type' with 'Unknown' to maintain consistency
df['Electric Vehicle Type'] = df['Electric Vehicle Type'].fillna('Unknown')

# Step 4: Transform - Encode 'Electric Vehicle Type' as numeric codes for storage optimization
df['EV_Type_Code'] = df['Electric Vehicle Type'].astype('category').cat.codes

# Use correct VIN column name based on dataset
vin_col = 'VIN (1-10)'

# Create dimension tables with unique entries for each dimension
dim_make = df[['Make']].drop_duplicates().reset_index(drop=True).copy()
dim_model = df[['Model']].drop_duplicates().reset_index(drop=True).copy()
dim_location = df[['City', 'State', 'Postal Code']].drop_duplicates().reset_index(drop=True).copy()

# Create fact table containing vehicle registration details and encoded vehicle type
fact_vehicle = df[[vin_col, 'Model Year', 'Base MSRP', 'Electric Range', 'EV_Type_Code']].copy()

# Export dimension and fact tables to CSV files with meaningful names
dim_make.to_csv('dim_vehicle_make.csv', index=False)           # Vehicle makes (brands)
dim_model.to_csv('dim_vehicle_model.csv', index=False)         # Vehicle models
dim_location.to_csv('dim_vehicle_location.csv', index=False)   # Geographic location info
fact_vehicle.to_csv('fact_vehicle_registration.csv', index=False)  # Fact table for analysis

print("ETL process completed and CSV files generated.")
