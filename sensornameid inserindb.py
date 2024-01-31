import mysql.connector
import pandas as pd

# Function to check database connectivity
def check_database_connection():
    try:
        # Connect to the MySQL database
        cnx = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="ashwin"
        )
        print("Database connection successful.")
        cnx.close()
    except Exception as e:
        print("Database connection failed:", e)

# Function to insert data from Excel to MySQL
def insert_data_from_excel():
    try:
        # Read the Excel file into a DataFrame
        df = pd.read_excel('C:/prtg/sensornameiddata.xlsx')

        # Connect to the MySQL database
        cnx = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="ashwin"
        )

        # Create a cursor object to execute SQL queries
        cursor = cnx.cursor()

        # Iterate over the DataFrame and insert each row into the database
        for index, row in df.iterrows():
            sensorname = row['Name']
            sensorid = row['ID']
            query = "INSERT INTO prtg (sensorname, sensorid) VALUES (%s, %s)"
            cursor.execute(query, (sensorname, sensorid))

        # Commit the changes to the database
        cnx.commit()

        # Close the cursor and connection
        cursor.close()
        cnx.close()

        print("Data inserted successfully.")
    except Exception as e:
        print("Error inserting data:", e)

# Check database connectivity
check_database_connection()

# Insert data from Excel to MySQL
insert_data_from_excel()
