import csv
import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('output101.xml')
root = tree.getroot()

# Define a list to store sensor ids
sensor_ids = []

# Iterate through all <sensor> elements
for sensor in root.iter('sensor'):
    # Check if the <sensortype> is "SNMP Traffic"
    sensortype = sensor.find('sensortype')
    if sensortype is not None and sensortype.text == 'SNMP Traffic':
        # If yes, append the sensor id to the list
        sensor_id = sensor.find('id')
        if sensor_id is not None:
            sensor_ids.append(sensor_id.text)

# Specify the output CSV file path
output_csv_file = 'sensor_ids100.csv'

# Write the extracted sensor IDs to the CSV file
with open(output_csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Sensor ID'])  # Write header
    for sensor_id in sensor_ids:
        writer.writerow([sensor_id])

print("Sensor IDs for SNMP Traffic sensors have been saved to:", output_csv_file)
