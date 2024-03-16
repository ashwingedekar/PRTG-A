import csv
import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('prtg-101.100.xml')
root = tree.getroot()

# Define a list to store sensor data
sensor_data = []

# Iterate through all <sensor> elements
for sensor in root.iter('sensor'):
    # Check if the <sensortype> is "SNMP Traffic"
    sensortype = sensor.find('sensortype')
    if sensortype is not None and sensortype.text == 'SNMP Traffic':
        # Find the sensor ID
        sensor_id = sensor.find('id')
        if sensor_id is not None:
            # Find the name tag
            name_tag = sensor.find('name')
            if name_tag is not None:
                # Append the sensor ID and name to the list
                sensor_data.append((sensor_id.text, name_tag.text))

# Specify the output CSV file path
output_csv_file = 'sensor_data.csv'

# Write the extracted sensor data to the CSV file
with open(output_csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Sensor ID', 'Name'])  # Write header
    for sensor_id, name in sensor_data:
        writer.writerow([sensor_id, name])

print("Sensor data for SNMP Traffic sensors have been saved to:", output_csv_file)
