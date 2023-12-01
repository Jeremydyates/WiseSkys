from datetime import datetime, timezone
import os

# Prompt user to enter BU Number
SiteID = input("What is your BU Number? Example 812345: ")

# Force capitalization if lowercase letters are typed
SiteID = SiteID.upper()

# Get the current date in the local time zone
current_date = datetime.now(timezone.utc).astimezone().date()

# Get the path to the user's desktop
desktop_path = os.path.expanduser("~/Desktop")

# Create the full output directory path directly on the desktop
folder_name = f"{SiteID}-{str(current_date.month).zfill(2)}-{str(current_date.day).zfill(2)}-{current_date.year}"
full_output_path = os.path.join(desktop_path, folder_name)

# Create the specified output directory
os.makedirs(full_output_path)

# Specify the desired output file location
output_file_path = os.path.join(full_output_path, "Propeller_process_download_csv_replaces_this.csv")

# Create subfolders within the main folder
os.mkdir(os.path.join(full_output_path, "360"))
os.mkdir(os.path.join(full_output_path, "FLT_1"))
os.mkdir(os.path.join(full_output_path, "FLT_2"))
os.mkdir(os.path.join(full_output_path, "FLT_3"))
os.mkdir(os.path.join(full_output_path, f"Remove-{folder_name}"))
os.mkdir(os.path.join(full_output_path, "FLT_1", "Photos"))
os.mkdir(os.path.join(full_output_path, "FLT_2", "Photos"))
os.mkdir(os.path.join(full_output_path, "FLT_3", "Photos"))

# Create and write to CSV file using the specified path
with open(output_file_path, "w") as csv_file:
    csv_file.write(SiteID)

print(f"Click [{folder_name}] on your desktop to access your folder workspace.")
