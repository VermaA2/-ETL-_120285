## ETL Project: Electric Vehicle Population Data (Washington State)

### Overview  
This ETL project processes electric and alternative fuel vehicle registration data for Washington State, transforming raw data into a clean, analytics-ready star schema model.

---

### Table of Contents  
- [Project Background](#project-background)  
- [Data Source](#data-source)  
- [ETL Pipeline Details](#etl-pipeline-details)  
  - [Extract](#extract)  
  - [Explore](#explore)  
  - [Clean](#clean)  
  - [Transform](#transform)  
  - [Load](#load)  
- [Data Model](#data-model)  
- [Running the ETL](#running-the-etl)  
- [Output Files](#output-files)  
- [Summary Statistics Export](#summary-statistics-export)  
- [How It Meets Requirements](#how-it-meets-requirements)  
- [Future Improvements](#future-improvements)  

---

### Project Background  
The goal is to enable stakeholders and data consumers to efficiently analyze electric vehicle registrations across Washington State by structuring the dataset into a star schema format. This enables fast, intuitive queries and reporting.

---

### Data Source  
- **Dataset:** Electric Vehicle Population Data  
- **Provider:** Washington State Open Data Portal  
- **File:** `Electric_Vehicle_Population_Data.csv`

---

### ETL Pipeline Details  

#### Extract  
- Loads the CSV file into a Pandas DataFrame for processing.  
- Initial columns and data types are inspected to understand dataset structure.

#### Explore  
- Summary statistics on key numeric features such as Electric Range, Base MSRP, and Model Year are generated to understand data distribution and identify anomalies.

#### Clean  
- Rows with missing values in key numeric fields (`Electric Range`, `Base MSRP`) are removed to ensure data quality.  
- Missing values in categorical field `Electric Vehicle Type` are filled with 'Unknown' to maintain completeness.

#### Transform  
- The `Electric Vehicle Type` categorical field is encoded into a numeric code for optimized storage and easier querying.  
- Dimension tables for `Make`, `Model`, and `Location` (City, State, Postal Code) are created by extracting distinct values.  
- A fact table is prepared with core transactional data including VIN, model year, MSRP, electric range, and encoded vehicle type.

#### Load  
- Each table is exported as a CSV file to the project root folder, ready for loading into a data warehouse or BI tool.

---

### Data Model  
The dataset is modeled using a **Star Schema**:

- **Fact Table:** `fact_vehicle_registration.csv`  
  Contains key transactional data with detailed vehicle registration info.

- **Dimension Tables:**  
  - `dim_vehicle_make.csv` (Vehicle Makes)  
  - `dim_vehicle_model.csv` (Vehicle Models)  
  - `dim_vehicle_location.csv` (Geographical Location)

This model supports scalable and performant analytical queries.

---

### Running the ETL  
1. Place `Electric_Vehicle_Population_Data.csv` in the project root.  
2. Run the script with Python 3 and pandas installed:

python etl_120285.py
