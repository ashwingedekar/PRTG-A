import csv
import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('101.100_saturday.xml')
root = tree.getroot()

# Define a list to store sensor data
sensor_data = []

# Iterate through all <sensor> elements
for sensor in root.findall('.//sensor'):
    # Check if <sensortype> is "Syslog Receiver"
    sensortype = sensor.find('sensortype')
    if sensortype is not None and sensortype.text == 'SNMP Traffic':
        # Find sensor ID
        sensor_id_element = sensor.find('id')
        sensor_id = sensor_id_element.text if sensor_id_element is not None else "Unknown ID"
        
        # Find parent <device> element
        device = sensor.find('..')
        if device is not None:
            # Find device name within the <name> tag under the parent <device> tag
            device_name_element = device.find('name')
            device_name = device_name_element.text if device_name_element is not None else "Unknown Device"
        else:
            device_name = "Unknown Device"
        
        # Append sensor ID and device name to the list
        sensor_data.append((sensor_id, device_name))

# Specify the output CSV file path
output_csv_file = '101.100_saturday.csv'

# Write the extracted sensor data to the CSV file
with open(output_csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Sensor ID', 'Device Name'])  # Write header
    for sensor_id, device_name in sensor_data:
        writer.writerow([sensor_id, device_name])

print("Sensor data for Syslog Receiver sensors have been saved to:", output_csv_file)
