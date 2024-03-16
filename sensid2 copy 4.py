import csv
import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('prtg-101.100.xml')
root = tree.getroot()

# Define a dictionary to store device names
device_names = {}

# Iterate through all <device> elements
for device in root.findall('.//device'):
    device_id_element = device.find('id')
    if device_id_element is not None:
        device_id = device_id_element.text
        # Find device name within the <name> tag under the <device> tag
        device_name_element = device.find('name')
        device_name = device_name_element.text if device_name_element is not None else "Unknown Device"
        # Store device name in the dictionary with device ID as key
        device_names[device_id] = device_name

# Print out the device names for debugging
print("Device Names:", device_names)

# Define a list to store sensor data
sensor_data = []

# Iterate through all <sensor> elements
for sensor in root.findall('.//sensor'):
    # Check if <sensortype> is "Syslog Receiver"
    sensortype = sensor.find('sensortype')
    if sensortype is not None and sensortype.text == 'Syslog Receiver':
        # Find sensor ID
        sensor_id_element = sensor.find('id')
        sensor_id = sensor_id_element.text if sensor_id_element is not None else "Unknown ID"
        
        # Find parent <device> element and its ID
        parent_device = sensor.find('..')
        if parent_device is not None:
            device_id_element = parent_device.find('id')
            device_id = device_id_element.text if device_id_element is not None else "Unknown Device ID"
        else:
            device_id = "Unknown Device ID"
        
        # Retrieve device name from the dictionary
        device_name = device_names.get(device_id, "Unknown Device")
        
        # Append sensor ID and device name to the list
        sensor_data.append((sensor_id, device_name))

# Specify the output CSV file path
output_csv_file = 'sensor_data-12.csv'

# Write the extracted sensor data to the CSV file
with open(output_csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Sensor ID', 'Device Name'])  # Write header
    for sensor_id, device_name in sensor_data:
        writer.writerow([sensor_id, device_name])

print("Sensor data for Syslog Receiver sensors have been saved to:", output_csv_file)
