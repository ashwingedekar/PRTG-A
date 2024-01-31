# app.py

from flask import Flask, render_template, request, jsonify
import requests
import pandas as pd
from io import StringIO
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_data', methods=['POST'])
def fetch_data():
    try:
        # Get values from the form
        sensor_id = request.form['sensorId']
        start_date = request.form['startDate']
        end_date = request.form['endDate']

        # Convert date-time strings to a datetime object
        start_datetime = datetime.strptime(start_date, '%Y-%m-%dT%H:%M')
        end_datetime = datetime.strptime(end_date, '%Y-%m-%dT%H:%M')

        # Format datetime objects back to strings for the API request
        start_date_str = start_datetime.strftime('%Y-%m-%d-%H-%M-%S')
        end_date_str = end_datetime.strftime('%Y-%m-%d-%H-%M-%S')

        # Construct API endpoint with form values
        api_endpoint = f'https://tp-prtg-101-100.comtelindia.com:10443/api/historicdata.csv?id={sensor_id}&avg=0&sdate={start_date_str}&edate={end_date_str}&username=Ashwin.Gedekar&passhash=3422185132'

        # Make the API request
        response = requests.get(api_endpoint)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Use pandas to read the CSV data
            df = pd.read_csv(StringIO(response.text))

            # Find the row with the maximum "Traffic Total (Speed)(RAW)"
            max_speed_row = df.loc[df["Traffic Total (Speed)(RAW)"].idxmax()]

            # Prepare the result as a dictionary
            result_dict = {
                "success": True,
                "message": "Data fetched successfully.",
                "max_speed_data": {
                    "Date Time": max_speed_row["Date Time"],
                    "Traffic Total (Speed)": max_speed_row["Traffic Total (Speed)"],
                    "Traffic Total (Speed)(RAW)": max_speed_row["Traffic Total (Speed)(RAW)"]
                }
            }
        else:
            result_dict = {
                "success": False,
                "message": f"Error: {response.status_code} - {response.text}"
            }

    except Exception as e:
        result_dict = {
            "success": False,
            "message": f"Error processing CSV data: {str(e)}"
        }

    return jsonify(result_dict)

if __name__ == '__main__':
    app.run(debug=True)