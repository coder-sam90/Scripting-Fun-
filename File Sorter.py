import os
import shutil
from pathlib import Path

def create_file_sorter():
  #making lists for multiple file types under a catagory. 
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
      
      #We need to change the file ext to all lowercase since the file extensions are lowercase. 
      file_extension = file_extension.lower()
      #For loop for our items
      for category, extensions in file_types.items():
            if file_extension in extensions:
                return category
              # If we didn't find a match, put it in 'Others'
              return 'Others'
