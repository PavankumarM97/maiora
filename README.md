# maiora

# Sales Data Processing Script

This Python script extracts, transforms, and loads sales data from two different regions into a PostgreSQL database. It also includes SQL queries to validate the loaded data.

## Requirements
- Python 3.x
- PostgreSQL

## Installation
1. Clone this repository to your local machine.
2. Install the required Python packages using pip:


## Usage
Follow the steps below to run the script:

1. **Extract and Transform Data:**
- Ensure that the CSV files `order_region_a.csv` and `order_region_b.csv` are in the `data` directory.
- Run the `upload_data.py` script to extract, transform, and load the data into the PostgreSQL database:
  ```
  python upload_data.py
  ```

2. **Run Validation Queries:**
- After uploading the data, you can run the `query_data.py` script to validate the data using SQL queries:
  ```
  python query_data.py
  ```

## Configuration
- Edit the PostgreSQL connection parameters in the scripts (`upload_data.py` and `query_data.py`) to match your database configuration.
- Ensure that you have appropriate permissions to create tables and execute queries in the specified database.

## Notes
- Make sure to replace sensitive information such as passwords with environment variables or other secure methods in a production environment.
- Ensure that PostgreSQL server is running and accessible before running the scripts.
