from config import FILE_NAME

def remove_duplicates(file_path):
    """Remove duplicate lines from a file while preserving order."""
    # Read lines from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Remove duplicates and maintain the original order
    unique_lines = list(dict.fromkeys(line.strip() for line in lines))

    # Write the unique lines back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in unique_lines:
            file.write(line + '\n')

    print("Duplicates have been successfully removed.")


# Specify the path to the file
remove_duplicates(FILE_NAME)
