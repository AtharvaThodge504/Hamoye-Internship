# importing pandas package
import pandas as pd

# making data frame from csv file
df = pd.read_csv(""D:\FoodBalanceSheets_E_Africa_NOFLAG.csv"")

# We are going to find aggregation for these columns
df.aggregate({"Item":['sum', 'Y2014'],
			"Item":['sum', 'Y2017']})

