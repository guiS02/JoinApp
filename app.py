import os
import pandas as pd

files_to_join = 'YourLocationHere'

df = []

for file in os.listdir(files_to_join):
    if file.endswith('.xlsx'):
        print('load file {0}...'.format(file))
        df.append(pd.read_excel(os.path.join(files_to_join, file)))

print(len(df))

df_principal = pd.concat(df, axis=0)
df_principal.to_excel('YourLocationHere\yourNewFile.xlsx', index=False)
