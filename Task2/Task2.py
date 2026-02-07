import pandas as pd

df= pd.read_csv('T2Data.csv')

df['Salary'] = df['Salary'].fillna(df.groupby('Department')['Salary'].transform('median'))
"""
 I changed the column Salary to fill all the Np.Nans that are they into Median,
   but the medinas are grouped acoording to the departments, so thats why i added df.groupby('Department)as well
   
"""
#now i will check if everything worked out correctly by suming the number of nulls

print(df.isnull().sum())
print(df['Salary'])

#Why is Goruped Imputation better than Global Imputation?
"""
IN a company people are paid differently in each department, if we replace all null values to the median of the entire slary column,
we will underestimate the salary of a Project Mangager and overestimate the salary of a janitor,
so thats why I took the median of the salary department wise, that way the null values will be replaced more accurately
"""