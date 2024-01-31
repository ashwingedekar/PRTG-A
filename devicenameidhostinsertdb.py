import mysql.connector
import pandas as pd
import numpy as np  # Import numpy for handling missing values

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
        return True
    except mysql.connector.Error as err:
        print("Database connection failed:", err)
        return False

# Function to insert data from Excel to MySQL
def insert_data_from_excel():
    try:
        # Read the Excel file into a DataFrame
        df = pd.read_excel('C:/prtg/devices_data.xlsx')

        # Handle missing values by replacing 'nan' with None
        df = df.where(pd.notnull(df), None)

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
            devicename = row['Device']
            host = row['Host']
            deviceid = row['ID']

            # SQL query to insert data into the table
            query = "INSERT INTO device (devicename, host, deviceid) VALUES (%s, %s, %s)"
            cursor.execute(query, (devicename, host, deviceid))

        # Commit the changes to the database
        cnx.commit()

        # Close the cursor and connection
        cursor.close()
        cnx.close()

        print("Data inserted successfully.")
    except Exception as e:
        print("Error inserting data:", e)

# Check database connectivity
if check_database_connection():
    # Insert data from Excel to MySQL if database connection is successful
    insert_data_from_excel()
else:
    print("Cannot proceed with data insertion due to database connection failure.")
