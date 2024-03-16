import csv
import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('prtg-101.100.xml')
root = tree.getroot()

# Define a list to store sensor data
sensor_data = []

# Iterate through all <sensor> elements
for sensor in root.findall('.//sensor'):
    # Find the sensor ID
    sensor_id_element = sensor.find('id')
    sensor_id = sensor_id_element.text if sensor_id_element is not None else "Unknown ID"
    
    # Find the name inside the <device><name> tag
    device_name_element = sensor.find('.//device/name')
    device_name = device_name_element.text if device_name_element is not None else "Unknown Device"
    
    # Append the sensor ID and device name to the list
    sensor_data.append((sensor_id, device_name))

# Specify the output CSV file path
output_csv_file = 'sensor_data-5.csv'

# Write the extracted sensor data to the CSV file
with open(output_csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Sensor ID', 'Device Name'])  # Write header
    for sensor_id, device_name in sensor_data:
        writer.writerow([sensor_id, device_name])

print("Sensor data for Syslog Receiver sensors have been saved to:", output_csv_file)
