from datetime import date
import os
import shutil

# Prompt user to enter Project Number_Client Site Name and Number
SiteID = input("What is your Site Name or Number? Example 10876543: ")

# Force capitalization if lowercase letters are typed
SiteID = SiteID.upper()

# Create main folder with Project Number_Client Site Name and Number and current date
folder_name = f"{SiteID}-{str(date.today().month).zfill(2)}-{str(date.today().day).zfill(2)}-{date.today().year}"

# Define a list of subfolders
subfolders = ["Overall", "Access Road", "Cable Run", "BSO", "TSO", "Civil", "Down Look", "Center", "Uplook", "Orbitals", "Verticals", "Array 1", "Array 2", "Array 3"]

# Define the base directory
base_directory = r"C:\WiseSkys\FlightDeck\All New Flights"

# Create the main folder in the specified directory
full_output_path = os.path.join(base_directory, folder_name)
os.makedirs(full_output_path)

# Create subfolders within the main folder in the specified directory
for subfolder in subfolders:
    os.mkdir(os.path.join(full_output_path, subfolder))

# Specify the source directory of the PDF files
pdf_source_directory = r"C:\WiseSkys\FlightDeck\orig"

# Specify the destination directory for the Overall folder
overall_folder_path = os.path.join(full_output_path, "Overall")

# List of PDF files to be copied
pdf_files = ["VTS AT&T Civil Shot Sheet v1.2.pdf", "VTS HARP v1.pdf", "VTS Tower Shot Sheet v1.3.pdf", "VTS Rooftop Shot Sheet v1.2.pdf"]

# Copy each PDF file to the Overall folder
for pdf_file in pdf_files:
    source_path = os.path.join(pdf_source_directory, pdf_file)
    destination_path = os.path.join(overall_folder_path, pdf_file)
    shutil.copyfile(source_path, destination_path)

print("Click [All New Flights C:] Button to access your Folder workspace.")
