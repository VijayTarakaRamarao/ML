import pandas as pd
import numpy as np

df=pd.read_csv("C:/Users/Administrator/Desktop/ML_Assignment_2/data.csv")

mean_value=df['Calories'].mean()

df['Calories'].fillna(value=mean_value,inplace=True)

print(df.head(25))

print("\n")
# 2. 2 Show the basic statistical description about the data.
print(df.describe())

print("\n")
# 2. 3 Check if the data has null values. a. Replace the null values with the mean
df.fillna(df.mean(), inplace=True)
print(df.isnull().any())

print("\n")
# 2. 4 Select at least two columns and aggregate the data using: min, max, count, mean.
print(df.agg({'Duration':['min','max','count','mean'],'Pulse':['min','max','count','mean']}))

print("\n")
# 2. 5 Filter the dataframe to select the rows with calories values between 500 and 1000.
print(df.loc[(df['Calories']>500)&(df['Calories']<1000)])

print("\n")
# 2. 6 Filter the dataframe to select the rows with calories values > 500 and pulse < 100.
print(df.loc[(df['Calories']>500)&(df['Pulse']<100)])

print("\n")
# 2. 7 Create a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse”.
df_modified = df[['Duration','Pulse','Calories']]
print(df_modified.head())

print("\n")
# 2. 8 Delete the “Maxpulse” column from the main df dataframe
del df['Maxpulse']
print(df.head())

print("\n")
# 2. 9 Convert the datatype of Calories column to int datatype.
print(df.dtypes)
print("\n")
df['Calories'] = df['Calories'].astype(np.int64)
print(df.dtypes)

print("\n")
# 2. 10 Using pandas create a scatter plot for the two columns (Duration and Calories).
print(df.plot.scatter(x='Duration',y='Calories',c='DarkBlue'))