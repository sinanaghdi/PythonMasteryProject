# import modules and global variables
from pathlib import Path
import shutil
base_dir = Path(r"C:\Users\Asus\Desktop\ComputerScienceBooks-master")
target_dir = base_dir / "sorted"

# declare categories and extensions
FILE_CATEGORIES = {
    "image":[".jpeg",".png"],
    "documents": [".pdf",".doc",".docx",".ppt","pptx"],
    "videos": [".mp4", ".wmv"],
    "audios": [".mp3",".wav",".aac","flac"],
    "archives": [".zip",".rar"]
}

# create directories based on categories
def create_categories_directories():
    for category,_ in FILE_CATEGORIES.items():
        (target_dir/ category).mkdir(parents=True,exist_ok=True)
    


# searching and categorizing files
def search_and_categorize_files():
    for file in base_dir.rglob("*"):
        for category,extension in FILE_CATEGORIES.items():
            if file.suffix in extension:
                try:
                    shutil.copy(file,target_dir / category)
                except shutil.SameFileError:
                    pass
                    
    


# run the application
create_categories_directories()
search_and_categorize_files()