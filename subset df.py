import pandas as pd
import numpy as np

df = pd.read_csv('intensive_care_beds_2020_cleaned.csv')
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

# Access to a given sub-DataFrame
print (df_name['df_1055'])

