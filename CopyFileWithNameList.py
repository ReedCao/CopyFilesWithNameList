import pandas as pd

df_files = pd.read_csv('NeedVerified.csv')
df_files

import shutil, os
for f in df_files['Filename']:
    print(f)
    shutil.copy(".\\车头照片\\" + f, 'dest_folder')
