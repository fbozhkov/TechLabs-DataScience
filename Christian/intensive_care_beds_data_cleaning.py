import pandas as pd
import numpy as np

path = "/Users/christianye/Desktop/TechLab_Vaccine_Project/Data/Intensive_care_beds_complete"
care_beds = pd.read_csv(path + "/intensive_care_beds_complete_df.csv")

# große Städte
Frankfurt = care_beds.loc[care_beds['gemeindeschluessel'] == 06412.0]
Hamburg = care_beds.loc[care_beds['gemeindeschluessel'] == 02000.0]
Koeln = care_beds.loc[care_beds['gemeindeschluessel'] == 05315.0]
Muenchen = care_beds.loc[care_beds['gemeindeschluessel'] == 9162]
Berlin = care_beds.loc[care_beds['gemeindeschluessel'] == 11000]
Duesseldorf = care_beds.loc[care_beds['gemeindeschluessel'] == 05111.0]


Aachen = care_beds.loc[care_beds['gemeindeschluessel'] == 05334.0]
Hamm = care_beds.loc[care_beds['gemeindeschluessel'] == 05915.0]
# kleine Städte
gemeinde1001 = care_beds.loc[care_beds['gemeindeschluessel'] == 1001.0]
gemeinde16073 = care_beds.loc[care_beds['gemeindeschluessel'] == 16073]


mean_standorte = Frankfurt["anzahl_standorte"].mean()
#standorte_list = Frankfurt["anzahl_standorte"]

#Frankfurt.set_index("daten_stand")
print(Frankfurt.index)

city = Duesseldorf

mean_standorte = city["anzahl_standorte"].mean()

for index in city.index:
    if city["anzahl_standorte"][index] < mean_standorte:
        if index > city.index.min() and index < city.index.max():
            val1 = city["betten_frei"].shift(1)[city.index == index]
            val2 = city["betten_frei"][city.index == index]
            val3 = city["betten_frei"].shift(-1)[city.index == index]
            average = int((val1+val2+val3)/3)
            city["betten_frei"][index] = average

print(city)
print(city.index.min())
#for daten_stand in Frankfurt.loc[:, "daten_stand"]:
#    df = Frankfurt[Frankfurt["daten_stand"] == daten_stand]
#    #print(df[["anzahl_standorte"]].all)
#    #print(type(df[["anzahl_standorte"]]))
#    print(mean_standorte)
#    print(df)
#    print(df["anzahl_standorte"])
#    if df["anzahl_standorte"] < mean_standorte:
#        print("hi")
