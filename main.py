import re
import os
import csv
import pytesseract
from PIL import Image

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\17244\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Function to extract Aadhaar card information from text
def extract_aadhaar_info(text):
    aadhaar_number = ""
    name = ""
    dob = ""

    # Regular expression patterns for Aadhaar card details
    aadhaar_number_pattern = r'\b\d{4}\s*\d{4}\s*\d{4}\b'  # Aadhaar number format (XXXX XXXX XXXX)
    dob_pattern = r'\d{2}/\d{2}/\d{4}'                       # Date of Birth format (DD/MM/YYYY)
    name_pattern = r'([A-Z\s\.]+)'                           # Flexible name pattern

    # List of common terms to ignore in Aadhaar cards
    ignore_terms = ['UIDAI', 'GOVT OF INDIA', 'GOVERNMENT', 'DEPARTMENT', 'CARD']

    # Extract Aadhaar number
    aadhaar_match = re.search(aadhaar_number_pattern, text)
    if aadhaar_match:
        aadhaar_number = aadhaar_match.group(0).replace(" ", "")  # Remove spaces if any

    # Extract DOB
    dob_match = re.search(dob_pattern, text)
    if dob_match:
        dob = dob_match.group(0)

    # Extract Name
    lines = text.splitlines()  # Split the text into lines
    name_found = False
    for line in lines:
        line = line.strip()

        # Skip any lines that contain common ignore terms
        if any(term in line.upper() for term in ignore_terms):
            continue  # Skip to the next line if ignore term is found

        # Extract the first valid name (not in ignore list)
        if re.match(name_pattern, line) and not name_found:
            name = line  # First match is the user's name
            break  # Stop after finding the name

    return aadhaar_number, name, dob

# Function to extract text from JPG using Tesseract OCR
def extract_text_from_image(image_file):
    try:
        image = Image.open(image_file)  # Open the image file
        text = pytesseract.image_to_string(image)  # Use Tesseract to extract text from the image
        return extract_aadhaar_info(text)  # Extract Aadhaar info from the text
    except Exception as e:
        print(f"Error processing image file {image_file}: {e}")
        return "", "", ""  # Return empty values in case of an error

# Directory containing image (JPG) files
image_directory = 'D:/django_employee_qr/DEMO/Aadhaar-Card-Data-Extractor'

# Output CSV file path
output_csv_file = 'D:/django_employee_qr/DEMO/OPEN RPA/output_aadhaar_details.csv'

# List to store extracted Aadhaar details from each image
extracted_aadhaar_info = []

# Iterate over all image files in the directory
for filename in os.listdir(image_directory):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):  # Check for image file formats
        image_file_path = os.path.join(image_directory, filename)
        # Extract information from the image file
        aadhaar_number, name, dob = extract_text_from_image(image_file_path)
        extracted_aadhaar_info.append({'Filename': filename, 'Aadhaar Number': aadhaar_number, 'Name': name, 'DOB': dob})
        print(f"Name: {name}")
        print(f"Aadhaar Number: {aadhaar_number}")
        print(f"Date of Birth: {dob}")

# Write the extracted information into a CSV file
with open(output_csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Filename', 'Aadhaar Number', 'Name', 'DOB']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in extracted_aadhaar_info:
        writer.writerow(item)

print("Extraction complete. Results saved in", output_csv_file)


