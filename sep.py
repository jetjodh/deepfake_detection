import pandas as pd 
import shutil
import os

data = pd.read_json('dfdc_train_part_49/metadata.json')
data = data.T
data['file'] = data.index

files = os.listdir('dfdc_train_part_49/audio') 
for i in range(len(files)):
    for x in range(len(data.file)):
        if files[i].split('.')[0]==data.file[x].split('.')[0]:
            if data.split[x]=='train':
                if data.label[x]=='FAKE':
                    shutil.move(r'D:\Projects\fake\dfdc_train_part_49\audio\\'+files[i],r'D:\Projects\fake\dfdc_train_part_49\audio\train\FAKE')
                else:
                    shutil.move(r'D:\Projects\fake\dfdc_train_part_49\audio\\'+files[i],r'D:\Projects\fake\dfdc_train_part_49\audio\train\REAL')
            else:
                if data.label[x]=='FAKE':
                    shutil.move(r'D:\Projects\fake\dfdc_train_part_49\audio\\'+files[i],r'D:\Projects\fake\dfdc_train_part_49\audio\test\FAKE')
                else:
                    shutil.move(r'D:\Projects\fake\dfdc_train_part_49\audio\\'+files[i],r'D:\Projects\fake\dfdc_train_part_49\audio\test\REAL')
