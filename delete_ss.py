#This is to clean up all screenshots on my desktop

import os
import glob

desktop_path = "/Users/im/Desktop"

png_files = glob.glob(os.path.join(desktop_path,"*.png"))

deleted = 0

for file in png_files:
    try:
        os.remove(file)
        print(f"Deleted: {file}")
        deleted += 1  
    except Exception as e:
        print(f"Error deleting: {file}: {e}")