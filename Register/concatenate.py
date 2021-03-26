import pandas as pd
import numpy as np
from glob import glob

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)

old_df = pd.read_csv('intensive_care_beds_complete_df.csv')

stock_files = sorted(glob('C:/Users/filip/PycharmProjects/Time Series/Register/Intensiveregister_*.csv'))

update_combined = pd.concat((pd.read_csv(file).assign(filename = file)
                             for file in stock_files), ignore_index = True)
update_combined = update_combined.drop(['betten_belegt_nur_erwachsen', 'betten_frei_nur_erwachsen', 'filename', ], axis=1)
update_combined.to_csv('final_data.csv')

final_data = pd.concat([old_df, update_combined], ignore_index=True)