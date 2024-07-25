# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 10:38:42 2024

@author: khali
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

df= pd.read_csv("product_price.csv")
mean_price= df['Prix'].mean()
std_prix=  df['Prix'].std()
print(f'Moyenne:{mean_price},Ecart-Type:{std_prix}')

plt.figure(figsize=(10,5))
sns.histplot(df["Prix"],kde=True)
plt.xlabel("Prix")
plt.ylabel("Fréquence")
plt.title("distrubition des prix")
plt.show()