import os
import shutil
from pathlib import Path

def create_file_sorter():
    """
    A basic file sorter that organizes files by their type/extension
    """
    
    # Define file type categories - this is a dictionary where keys are folder names
    # and values are lists of file extensions that belong in those folders
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm'],
        'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Spreadsheets': ['.xls', '.xlsx', '.csv', '.ods'],
        'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c']
    }
    
    def get_file_category(file_extension):
        """
        Takes a file extension and returns which category it belongs to
        
        Args:
            file_extension (str): The file extension (like '.jpg')
            
        Returns:
            str: The category name, or 'Others' if no match found
        """
        file_extension = file_extension.lower()  # Convert to lowercase for comparison
        
        # Loop through our file_types dictionary
        for category, extensions in file_types.items():
            if file_extension in extensions:
                return category
        
        # If we didn't find a match, put it in 'Others'
        return 'Others'
    
    def sort_files(source_folder, create_folders=True):
        """
        Sort files in the source folder into subfolders by type
        
        Args:
            source_folder (str): Path to the folder containing files to sort
            create_folders (bool): Whether to create category folders if they don't exist
        """
        
        # Convert string path to Path object (more modern way to handle paths)
        source_path = Path(source_folder)
        
        # Check if the source folder exists
        if not source_path.exists():
            print(f"Error: The folder '{source_folder}' does not exist!")
            return
        
        if not source_path.is_dir():
            print(f"Error: '{source_folder}' is not a directory!")
            return
        
        # Keep track of what we've done
        moved_files = 0
        created_folders = []
        
        # Get all files in the source directory (not subdirectories)
        files = [f for f in source_path.iterdir() if f.is_file()]
        
        if not files:
            print("No files found to sort!")
            return
        
        print(f"Found {len(files)} files to sort...")
        
        # Process each file
        for file_path in files:
            # Get the file extension
            file_extension = file_path.suffix  # .suffix gets the file extension
            
            # Determine which category this file belongs to
            category = get_file_category(file_extension)
            
            # Create the destination folder path
            destination_folder = source_path / category
            
            # Create the category folder if it doesn't exist and we're allowed to
            if create_folders and not destination_folder.exists():
                destination_folder.mkdir(parents=True, exist_ok=True)
                created_folders.append(category)
                print(f"Created folder: {category}")
            
            # Create the full destination path for this file
            destination_path = destination_folder / file_path.name
            
            # Handle case where file already exists in destination
            counter = 1
            original_destination = destination_path
            while destination_path.exists():
                # Add a number to make filename unique
                stem = original_destination.stem  # filename without extension
                suffix = original_destination.suffix  # file extension
                destination_path = destination_folder / f"{stem}_{counter}{suffix}"
                counter += 1
            
            try:
                # Move the file (you could use shutil.copy2() instead to copy)
                shutil.move(str(file_path), str(destination_path))
                print(f"Moved: {file_path.name} → {category}/")
                moved_files += 1
                
            except Exception as e:
                print(f"Error moving {file_path.name}: {e}")
        
        # Summary
        print(f"\nSorting complete!")
        print(f"Files moved: {moved_files}")
        if created_folders:
            print(f"Folders created: {', '.join(created_folders)}")

    return sort_files

# Create our file sorter function
file_sorter = create_file_sorter()

# Example usage:
if __name__ == "__main__":
    # Replace this path with the folder you want to sort
    folder_to_sort = input("Enter the path to the folder you want to sort: ")
    
    # Sort the files
    file_sorter(folder_to_sort)
