from datetime import date
import os

# Prompt user to enter Project Number_Client Site Name and Number
SiteID = input("What is your Project Number, Client Site Name, or Number? Example 876543 or DEGRR00001A: ")

# Force capitalization if lowercase letters are typed
SiteID = SiteID.upper()

# Create main folder with Project Number_Client Site Name and Number and current date
folder_name = f"{SiteID}-{str(date.today().month).zfill(2)}-{str(date.today().day).zfill(2)}-{date.today().year}"

# Define a list of subfolders
subfolders = ["Hot Spot", "Access Road", "Model1", "Model2", "Model3"]

# Get the path to the user's desktop
desktop_path = os.path.expanduser("~/Desktop")

# Create the main folder directly on the desktop
full_output_path = os.path.join(desktop_path, folder_name)
os.makedirs(full_output_path)

# Create subfolders within the main folder on the desktop
for subfolder in subfolders:
    os.mkdir(os.path.join(full_output_path, subfolder))

#print(f"Folders have been created for {SiteID} on the desktop.")
print(f"Click [{folder_name}] on your desktop to access your Folder workspace.")
