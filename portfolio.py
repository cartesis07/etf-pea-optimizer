import pandas as pd 

portfolio = pd.read_csv("portfolio.csv")

print(portfolio.head())

print(portfolio.isna().sum())