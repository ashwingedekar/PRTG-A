import xml.etree.ElementTree as ET

def remove_invalid_characters(xml_file, output_file):
    try:
        # Parse the XML file
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        # Function to remove invalid characters
        def remove_invalid_chars(text):
            return text.replace('�C', '')

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
        print("XML file cleaned successfully!")
        
    except ET.ParseError as e:
        # Print the error and the problematic line/column
        print(f"XML ParseError: {e}")
        with open(xml_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            print(f"Problematic line: {lines[e.position[0]-1]}")
            print(f"Error occurred at line {e.position[0]}, column {e.position[1]}")

# Usage: Replace 'input.xml' with the path to your input XML file
# and 'output.xml' with the path to the output file where you want the cleaned XML to be saved.
remove_invalid_characters('101.100_latest.xml', 'ooutput.xml')
