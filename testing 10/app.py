from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# Function to fetch device IDs from the database
def get_device_ids():
    try:
        # Connect to the MySQL database
        cnx = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="ashwin"
        )

        # Create a cursor object to execute queries
        cursor = cnx.cursor()

        # Execute the query to retrieve device IDs
        cursor.execute("SELECT deviceid FROM device")

        # Fetch all device IDs
        device_ids = cursor.fetchall()

        # Close the cursor and database connection
        cursor.close()
        cnx.close()

        return [str(device_id[0]) for device_id in device_ids]

    except Exception as e:
        print("Error fetching device IDs:", e)
        return []

# Function to fetch device details from the database
def get_device_details(device_id):
    try:
        # Connect to the MySQL database
        cnx = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="ashwin"
        )

        # Create a cursor object to execute queries
        cursor = cnx.cursor()

        # Execute the query to retrieve device details
        cursor.execute("SELECT devicename, host FROM device WHERE deviceid = %s", (device_id,))

        # Fetch the device details
        device_details = cursor.fetchone()

        # Close the cursor and database connection
        cursor.close()
        cnx.close()

        return device_details

    except Exception as e:
        print("Error fetching device details:", e)
        return None

# Route for the index page
@app.route('/')
def index():
    device_ids = get_device_ids()  # Get device IDs from the database
    return render_template('index.html', device_ids=device_ids)

# Route for fetching data
@app.route('/fetch_data', methods=['POST'])
def fetch_data():
    try:
        # Get values from the form
        device_id = request.form['deviceid']

        # Get device details from the database
        device_details = get_device_details(device_id)

        if device_details:
            device_name, host_ip = device_details
            return f'''
                <h2>Device ID: {device_id}</h2>
                <p>Device Name: {device_name}</p>
                <p>Host IP: {host_ip}</p>
            '''
        else:
            return '<h2>No device found with the provided ID.</h2>'

    except Exception as e:
        return f'<h2>Error fetching data: {str(e)}</h2>'

if __name__ == '__main__':
    app.run(debug=True)
