import pandas as pd
import sys

df=pd.read_csv("fercform1electricutilitydata19942019.csv")
alaska_total_energy=df[ (df['Utility Name']=="Alaska Electric Light and Power Company")][['Total Energy Sales (MWh)']]
print(alaska_total_energy.max())

#print(df[(df['Utility Name']=="Alaska Electric Light and Power Company")][['Reporting Year']])