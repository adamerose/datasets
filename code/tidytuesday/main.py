import os
import sys
import shutil

rootdir = 'data'
destdir = 'flat_data'
for root, subdirs, files in os.walk(rootdir):
    for file in files:
        file_path = os.path.join(root,file)
        if file.endswith('.csv'):
            x = root.split("\\")[-1]
            new_name = f'{x}_{file}'
            print(file_path, new_name)
            shutil.copy(file_path, os.path.join(destdir, new_name))