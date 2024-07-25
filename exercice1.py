# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 10:09:54 2024

@author: khali
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

#lecture
df =pd.read_csv("temperature_data.csv")

#conversion de date
df['Date']= pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
# courbe
plt.figure(figsize=(10,5))
plt.plot(df.index, df['Temperature'],label="temperature en fonction de date")
#regression
x= (df.index-df.index[0]).days
slope, intercept,r_value,p_value,std_err=linregress(x,df['Temperature'])
plt.plot(df.index, intercept+slope *x,'r',label='Tendance')
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Tendance")