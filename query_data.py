import psycopg2

# Connect to PostgreSQL database using psycopg2
conn = psycopg2.connect(
    dbname="maiora",
    user="postgres",
    password="Pavan@97",
    host="localhost",
    port="5432"
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
