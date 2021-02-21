###
###    Test file, while I get everything to work properly
###    When something works I will put it in the Jupyter Notebook
###
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)

def get_df_name(df):

    name =[x for x in globals() if globals()[x] is df][0]
    return name

# read the Aachen Intensive Care dataset
aachen = pd.read_csv('Intensive_Care_Aachen_2020.csv', index_col='daten_stand', parse_dates=True)

# preprocessing
aachen = aachen.drop(['gemeindeschluessel', 'bundesland', 'anzahl_meldebereiche'], axis=1)

#define function for ADF test

def adf_test(timeseries):
    #Perform Dickey-Fuller test:
    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
       dfoutput['Critical Value (%s)'%key] = value
    print (dfoutput)
    if dftest[1] < 0.05 :
        print('p-value: ' + str(dftest[1]) + ' < 0.05 => the series is stationary')
    else:
        print('p-value: ' + str(dftest[1]) + ' > 0.05 => the series is non-stationary')


# apply adf test on the 'faelle_covid_aktuell_beatmet' series
adf_test(aachen['faelle_covid_aktuell_beatmet'])


# define KPSS
def kpss_test(timeseries):
    print ('Results of KPSS Test:')
    kpsstest = kpss(timeseries, regression='c', nlags='legacy')
    kpss_output = pd.Series(kpsstest[0:3], index=['Test Statistic','p-value','Lags Used'])
    for key,value in kpsstest[3].items():
        kpss_output['Critical Value (%s)' % key] = value
    print(kpss_output)
    if kpsstest[1] < 0.05 :
        print('p-value: ' + str(kpsstest[1]) + ' < 0.05 => the series is non-stationary')
    else:
        print('p-value: ' + str(kpsstest[1]) + ' > 0.05 => the series is stationary')


kpss_test(aachen['faelle_covid_aktuell_beatmet'])

# Trying to transform to stationary time series by taking the difference
aachen_stationary = aachen.diff().dropna()

train = aachen.faelle_covid_aktuell_beatmet[:'2020-11']
test = aachen.faelle_covid_aktuell_beatmet['2020-12':]

print('\nDickey-Fuller Test on ' + get_df_name(aachen_stationary))
adf_test(aachen_stationary['faelle_covid_aktuell_beatmet'])
'''
plt.plot(aachen_stationary.faelle_covid_aktuell_beatmet)
plt.title("Aachen Differencing with p-value=0.042277")
# solves overlapping dates on x-axis
plt.gcf().autofmt_xdate()
'''

aachen_stationary_x2 = aachen.diff().diff().dropna()

print('\nDickey-Fuller Test on ' + get_df_name(aachen_stationary_x2))
adf_test(aachen_stationary_x2['faelle_covid_aktuell_beatmet'])

aachen_log = np.log(aachen/aachen.shift(1))
# preprocessing
aachen_log = aachen_log.drop(aachen_log.index[0])
aachen_log = aachen_log.replace([np.inf, -np.inf, np.nan], 0)

print('\nDickey-Fuller Test on ' + get_df_name(aachen_log))
adf_test(aachen_log['faelle_covid_aktuell_beatmet'])