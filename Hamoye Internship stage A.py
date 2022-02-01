import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
sns.set(style="white", color_codes=True)
df = pd.read_csv("D:\FoodBalanceSheets_E_Africa_NOFLAG.csv",encoding='ISO-8859-1')
#Question 11
x = df.groupby('Item').agg({'Y2014': ['sum'],'Y2017':['sum']})
print(x)
#Question 12
grouped_mean_answer = df['Y2015'].mean()
grouped_mean__answer_final = np.round(grouped_mean,decimals= 3)
print(grouped_mean_final)
grouped_std_answer  =df['Y2015'].std()
grouped_std_answer_final = np.round(grouped_std,decimals= 3)
print(grouped_std_final)
#Question 13
total_number_of_missing_data = df['Y2016'].isnull().sum()  
print(total_number_of_missing_data)
total_percentage_final = np.round(((total_number_of_missing_data/len(df['Y2016']))*100),decimals=2)
print(total_percentage_final)
#Question 14
df.corr(method='kendall')
#Question 15
df.groupby('Element').agg({'Y2014': ['sum'], 'Y2015': ['sum' ], 'Y2016': ['sum'], 'Y2017': ['sum' ], 'Y2018': ['sum']})
#Question 16
df.groupby('Element').agg({'Y2014':['sum']})
#Question 17
df.groupby('Element').agg({'Y2014': ['sum'], 'Y2015': ['sum' ], 'Y2016': ['sum'], 'Y2017': ['sum' ], 'Y2018': ['sum']})
#Question 18
df.groupby('Element').agg({'Y2018': ['sum']})
#Question 20
df.nunique()