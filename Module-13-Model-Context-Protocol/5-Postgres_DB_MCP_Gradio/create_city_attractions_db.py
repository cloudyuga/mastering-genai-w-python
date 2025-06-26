import psycopg2

# Define PostgreSQL connection parameters
conn = psycopg2.connect(
    dbname="testdb",
    user="postgres",          # change if you have a different user
    password="postgres",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS attractions (
        id SERIAL PRIMARY KEY,
        city TEXT NOT NULL,
        attraction TEXT NOT NULL
    )
""")

# Attractions data
attractions_data = {
    "paris": [
        "Eiffel Tower",
        "Louvre Museum",
        "Notre-Dame Cathedral",
        "Seine River Cruise",
        "Montmartre"
    ],
    "tokyo": [
        "Shibuya Crossing",
        "Tokyo Tower",
        "Meiji Shrine",
        "Asakusa Temple",
        "Akihabara District"
    ],
    "rome": [
        "Colosseum",
        "Trevi Fountain",
        "Pantheon",
        "Roman Forum",
        "Vatican Museums"
    ],
    "new york": [
        "Statue of Liberty",
        "Central Park",
        "Times Square",
        "Empire State Building",
        "Broadway Shows"
    ],
    "london": [
        "Tower of London",
        "London Eye",
        "Buckingham Palace",
        "British Museum",
        "Big Ben"
    ]
}

# Insert data
for city, attractions in attractions_data.items():
    for attraction in attractions:
        cursor.execute(
            "INSERT INTO attractions (city, attraction) VALUES (%s, %s)",
            (city.lower(), attraction)
        )

# Commit and close
conn.commit()
cursor.close()
conn.close()

print("✅ Data inserted into PostgreSQL testdb successfully.")
