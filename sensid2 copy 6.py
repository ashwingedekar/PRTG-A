import xml.etree.ElementTree as ET

# Path to the XML file
xml_file = 'prtg-101.100.xml'

# Parse the XML file
tree = ET.parse(xml_file)
root = tree.getroot()

# Extract device names, sensor IDs, and sensor types for all devices and sensors
for device in root.findall('.//device'):
    device_name_element = device.find('name')
    if device_name_element is not None:
        device_name = device_name_element.text
    else:
        device_name = "N/A"
    
    for sensor in device.findall('.//sensor'):
        sensor_id_element = sensor.find('id')
        sensor_type_element = sensor.find('sensortype')
        if sensor_id_element is not None and sensor_type_element is not None:
            sensor_id = sensor_id_element.text
            sensor_type = sensor_type_element.text
            print("Device Name:", device_name)
            print("Sensor ID:", sensor_id)
            print("Sensor Type:", sensor_type)
            print("----------------------")
        else:
            print("Error: Sensor ID or Sensor Type missing")
