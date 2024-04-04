import xml.etree.ElementTree as ET
import re

# Function to remove specified characters from text
def remove_characters(text):
    # Remove "(�C)" and "�C" characters
    cleaned_text = re.sub(r'\(�C\)|�C', '', text)
    return cleaned_text

# Attempt to read the XML file with different encodings
encodings_to_try = ['utf-8', 'latin-1']  # Add more encodings if needed

for encoding in encodings_to_try:
    try:
        with open('101.100_NOW.xml', 'r', encoding=encoding) as file:
            xml_content = file.read()
        break  # Stop trying encodings if successful
    except UnicodeDecodeError:
        continue  # Try the next encoding

# Remove specified characters from the XML content
cleaned_xml_content = remove_characters(xml_content)

# Parse the cleaned XML content
try:
    root = ET.fromstring(cleaned_xml_content)
    tree = ET.ElementTree(root)

    # Save the modified XML back to a file
    tree.write('101.100_cleaned.xml')
    print("XML file cleaned successfully!")
except ET.ParseError as e:
    print("Error parsing XML:", e)
