import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('prtg-101.100.xml')
root = tree.getroot()

# Function to remove characters from text content recursively
def remove_characters(element, char_to_remove):
    if element.text:
        element.text = element.text.replace(char_to_remove, "")
    for child in element:
        remove_characters(child, char_to_remove)

# Call the function to remove characters
remove_characters(root, '�C')

# Save the modified XML back to file
tree.write('modified_example.xml')
