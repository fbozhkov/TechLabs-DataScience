import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ignore (settings for pycharm console)
pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)

# use parse_dates in order to keep the datetime dtype on the given column
df = pd.read_csv('intensive_care_beds_2020_cleaned.csv', parse_dates=['daten_stand'])
# extract county codes
code = df['gemeindeschluessel'][0:393]
# convert Pandas Series to a list
code = code.to_list()

# create an empty dictionary to store df_names as keys to each county's DataFrame
df_name = {}
# Create a DataFrame for each county
# DataFrames are named as " df_<county's code> "
for x in code:
    df_names = 'df_' + str(x)
    df_name[df_names] = df[df["gemeindeschluessel"] == x]
    df_name[df_names].index = df_name[df_names].daten_stand
    df_name[df_names] = df_name[df_names].drop('daten_stand', axis=1)


# Access to a given sub-DataFrame
aachen = df_name['df_5334']
aachen.to_csv('Intensive_Care_Aachen_2020.csv', date_format='%Y-%m-%d')
print (aachen)

