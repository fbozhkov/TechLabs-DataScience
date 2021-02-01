import pandas as pd



pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
#search for a specific contained string assigning it to mask and then locating it
mask = np.column_stack([df['bundesland'].str.contains(r"\x1a", na=False) for col in df])
df.loc[mask.any(axis=1)]
#droping a row by index value
df = df.drop([72675])
#reseting the index labels after dropping a row
df = df.reset_index(drop=True)

df = pd.read_csv('May_June.csv')
print(df)