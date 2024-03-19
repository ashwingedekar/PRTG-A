import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('prtg-101.100.xml')
root = tree.getroot()

# Find the device element
device_element = root.find(".//device")

# Extract device name and ID
if device_element is not None:
    device_name_element = device_element.find("name")
    device_id_element = device_element.find("id")
    device_name = device_name_element.text if device_name_element is not None else ""
    device_id = device_id_element.text if device_id_element is not None else ""
else:
    device_name = ""
    device_id = ""

# Find all sensor elements
sensor_elements = root.findall(".//sensor")

# Extract sensor names and IDs
sensor_data = []
for sensor in sensor_elements:
    sensor_name_element = sensor.find("name")
    sensor_id_element = sensor.find("id")
    if sensor_name_element is not None and sensor_id_element is not None:
        sensor_name = sensor_name_element.text if sensor_name_element.text is not None else ""
        sensor_id = sensor_id_element.text if sensor_id_element.text is not None else ""
        sensor_data.append((sensor_name, sensor_id))

# Build XML string for device
device_xml = f"<device><id>{device_id}</id><name>{device_name}</name></device>"

# Build XML string for sensors
sensors_xml = "".join([f"<sensor><id>{sensor_id}</id><name>{sensor_name}</name></sensor>" for sensor_name, sensor_id in sensor_data])

# Print the XML data
print("Device XML:", device_xml)
print("Sensors XML:", sensors_xml)
