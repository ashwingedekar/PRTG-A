from flask import Flask, render_template, request, jsonify
import requests
import mysql.connector

app = Flask(__name__)

# Function to fetch sensor IDs from the database
def get_sensor_ids():
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

        # Execute the query to retrieve sensor IDs
        cursor.execute("SELECT ID FROM data")

        # Fetch all sensor IDs
        sensor_ids = cursor.fetchall()

        # Close the cursor and database connection
        cursor.close()
        cnx.close()

        return [str(sensor_id[0]) for sensor_id in sensor_ids]

    except Exception as e:
        print("Error fetching sensor IDs:", e)
        return []

# Route for the index page
@app.route('/')
def index():
    sensor_ids = get_sensor_ids()  # Get sensor IDs from the database
    return render_template('index.html', sensor_ids=sensor_ids)

# Route for fetching data
@app.route('/fetch_data', methods=['POST'])
def fetch_data():
    try:
        # Get values from the form
        columnname = request.form['columnname']
        username = request.form['username']
        passhash = request.form['passhash']
        sensor_id = request.form['sensorId']

        # Construct API endpoint with form values
        api_endpoint = f"https://tp-prtg-101-100.comtelindia.com:10443/api/getobjectstatus.htm?id={sensor_id}&name={columnname}&username={username}&passhash={passhash}"

        # Make the API request
        response = requests.get(api_endpoint)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Return the response text directly
            return jsonify({"success": True, "data": response.text})

        else:
            return jsonify({"success": False, "message": f"Error: {response.status_code} - {response.text}"})

    except Exception as e:
        return jsonify({"success": False, "message": f"Error processing XML data: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
