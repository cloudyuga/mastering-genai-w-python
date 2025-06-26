# add the following code to create a PostgreSQL database named 'testdb' in create_city_attractions_db.py

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Step 1: Connect to default 'postgres' database to create 'testdb'
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)  # Required for CREATE DATABASE

cursor = conn.cursor()

# Create 'testdb' if it doesn't exist
try:
    cursor.execute("CREATE DATABASE testdb;")
    print("✅ Database 'testdb' created successfully.")
except psycopg2.errors.DuplicateDatabase:
    print("ℹ️ Database 'testdb' already exists.")

cursor.close()
conn.close()
