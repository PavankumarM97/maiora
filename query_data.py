import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Database credentials
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

# Connect to PostgreSQL database using psycopg2
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)
cursor = conn.cursor()

# a. Count the total number of records
cursor.execute('SELECT COUNT(*) FROM sales_data')
total_records = cursor.fetchone()[0]
print("Total number of records:", total_records)

# b. Find the total sales amount by region
cursor.execute('SELECT region, SUM(total_sales) FROM sales_data GROUP BY region')
total_sales_by_region = cursor.fetchall()
print("Total sales amount by region:", total_sales_by_region)

# c. Find the average sales amount per transaction
cursor.execute('SELECT AVG(total_sales) FROM sales_data')
avg_sales_per_transaction = cursor.fetchone()[0]
print("Average sales amount per transaction:", avg_sales_per_transaction)

# d. Ensure there are no duplicate id values
cursor.execute('SELECT "OrderId", COUNT(*) FROM sales_data GROUP BY "OrderId" HAVING COUNT(*) > 1')
duplicate_order_ids = cursor.fetchall()
if len(duplicate_order_ids) > 0:
    print("Duplicate OrderIds:", duplicate_order_ids)
else:
    print("No duplicate id is present")

# Close the cursor and connection
cursor.close()
conn.close()
