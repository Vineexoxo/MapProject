import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

covid_19=pd.read_csv("covid_19_india.csv")
# print(covid_19.head())  # prints first 5 table values.
# print(covid_19.info())  # Info about the csv file.

# print(covid_19.shape)   # prints no. of rows, no. of columns

# print(covid_19['State'].unique(),covid_19['State'].nunique())   # array of unique values of objects in State column, nunique for number of such unique objects.

# pivot_table acts like select stmt in sql.
# statewise=pd.pivot_table(covid_19,values=['Positive'],index='State',aggfunc='max',margins=True)
# print(statewise)