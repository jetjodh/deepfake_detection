import os

for path, subdirs, files in os.walk(r'D:\Projects\fake'):
    for name in subdirs:
        if('REAL' in name):
            file_path = os.path.join(path,name)
            new_name = os.path.join(path,name).replace('REAL','0')
            os.rename(file_path, new_name)  