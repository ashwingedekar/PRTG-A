import xml.etree.ElementTree as ET

def remove_invalid_characters(xml_file, output_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Function to remove invalid characters
    def remove_invalid_chars(text):
        return ''.join(c for c in text if ord(c) != 65533)  # U+FFFD

    # Recursively remove invalid characters from all text nodes
    def remove_invalid_chars_recursive(element):
        if element.text:
            element.text = remove_invalid_chars(element.text)
        for child in element:
            remove_invalid_chars_recursive(child)

    # Remove invalid characters recursively
    remove_invalid_chars_recursive(root)

    # Write the modified XML to a new file
    tree.write(output_file, encoding='utf-8')

# Usage
remove_invalid_characters('101.100_latest.xml', 'clean.xml')
