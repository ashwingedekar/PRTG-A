from flask import Flask, render_template, request, jsonify
import requests
import pandas as pd
from io import StringIO
from datetime import datetime
import mysql.connector

app = Flask(__name__)

def get_sensor_ids():
    try:
        # Connect to the MySQL database
        cnx = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",  # Enter your MySQL username
            password="",  # Enter your MySQL password
            database="ashwin"  # Enter your MySQL database name
        )

        # Create a cursor object to execute queries
        cursor = cnx.cursor()

        # Execute the query to retrieve sensor IDs
        cursor.execute("SELECT ID FROM data")  # Modify your_table_name according to your database structure

        # Fetch all sensor IDs
        sensor_ids = cursor.fetchall()

        # Close the cursor and database connection
        cursor.close()
        cnx.close()

        return [str(sensor_id[0]) for sensor_id in sensor_ids]  # Convert to list of strings

    except Exception as e:
        print("Error fetching sensor IDs:", e)
        return []

@app.route('/')
def index():
    sensor_ids = get_sensor_ids()  # Get sensor IDs from the database
    return render_template('index.html', sensor_ids=sensor_ids)

@app.route('/fetch_data', methods=['POST'])
def fetch_data():
    try:
        # Get values from the form
        sensor_id = request.form['sensorId']
        start_date = request.form['startDate']
        end_date = request.form['endDate']
        avg = request.form['avg']
        username = request.form['username']
        passhash = request.form['passhash']
        speed_data_type = request.form.get('speedDataType', 'max')

        # Convert date-time strings to a datetime object
        start_datetime = datetime.strptime(start_date, '%Y-%m-%dT%H:%M')
        end_datetime = datetime.strptime(end_date, '%Y-%m-%dT%H:%M')

        # Format datetime objects back to strings for the API request
        start_date_str = start_datetime.strftime('%Y-%m-%d-%H-%M-%S')
        end_date_str = end_datetime.strftime('%Y-%m-%d-%H-%M-%S')

        # Construct API endpoint with form values
        api_endpoint = f'https://tp-prtg-101-100.comtelindia.com:10443/api/historicdata.csv?id={sensor_id}&avg={avg}&sdate={start_date_str}&edate={end_date_str}&username={username}&passhash={passhash}'

        # Make the API request
        response = requests.get(api_endpoint)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Use pandas to read the CSV data
            df = pd.read_csv(StringIO(response.text))

            if df.empty:
                return jsonify({"success": False, "message": "No data available."})

            if speed_data_type == 'min':
                speed_row = df.loc[df["Traffic Total (Speed)(RAW)"].idxmin()]
                speed_data_key = "min_speed_data"
            else:
                speed_row = df.loc[df["Traffic Total (Speed)(RAW)"].idxmax()]
                speed_data_key = "max_speed_data"

            # Prepare the result as a dictionary
            result_dict = {
                "success": True,
                "message": "Data fetched successfully.",
                speed_data_key: {
                    "Date Time": speed_row["Date Time"],
                    "Traffic Total (Speed)": speed_row["Traffic Total (Speed)"],
                    "Traffic Total (Speed)(RAW)": speed_row["Traffic Total (Speed)(RAW)"],
                    "output_location": f"C:/prtg/output_{speed_data_type}_speed_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
                }
            }

            return jsonify(result_dict)

        else:
            return jsonify({"success": False, "message": f"Error: {response.status_code} - {response.text}"})

    except Exception as e:
        return jsonify({"success": False, "message": f"Error processing CSV data: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
