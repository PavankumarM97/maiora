import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import urllib.parse

# Load environment variables from .env file
load_dotenv()

# Database credentials
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

# URL-encode the password
password = urllib.parse.quote(DB_PASSWORD)

# Load the data from the provided CSV files
file_a = '/home/pavan/Downloads/order_region_a.csv'
file_b = '/home/pavan/Downloads/order_region_b.csv'

# Read the data into pandas DataFrames
df_a = pd.read_csv(file_a)
df_b = pd.read_csv(file_b)

# Add a 'region' column to each DataFrame
df_a['region'] = 'A'
df_b['region'] = 'B'

# Combine the data from both regions into a single DataFrame
combined_df = pd.concat([df_a, df_b], ignore_index=True)

# Calculate the 'total_sales' column
combined_df['total_sales'] = combined_df['QuantityOrdered'] * combined_df['ItemPrice']

# Remove duplicate entries based on 'OrderId'
combined_df = combined_df.drop_duplicates(subset='OrderId')

# Connect to PostgreSQL database
engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{password}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Load the transformed data into the sales_data table
combined_df.to_sql('sales_data', engine, if_exists='replace', index=False, method='multi')

print("Data upload complete.")
