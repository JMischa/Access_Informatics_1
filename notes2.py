__author__ = "Mischa Jampen"
import os

def update_author_in_files(folder_path):
    # List all files in the specified folder
    files = [f for f in os.listdir(folder_path) if f.endswith(".py")]

    # Iterate through each Python file and update __author__ on the first line
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            content = file.readlines()

        # Update the first line with __author__ = "Mischa Jampen"
        content[0] = '__author__ = "Mischa Jampen"\n'

        # Write back to the file
        with open(file_path, 'w') as file:
            file.writelines(content)

        print(f"Updated {file_name} in {folder_path}")

if __name__ == "__main__":
    # Replace the following path with the correct path on your Mac
    base_folder = "/Users/mischajampen/Developer/Python/Access_Informatics_1"

    # Call the function to update __author__ in Python files
    update_author_in_files(base_folder)

