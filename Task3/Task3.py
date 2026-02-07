import pandas as pd

df = pd.read_csv('DataT3.csv')

print(df.columns)

df['Timestamp'] = pd.to_datetime(df['Timestamp'])

#identifing the duplicate ids
duplicates = df[df.duplicated('Transaction_ID', keep=False)] 
print(f"Found {len(duplicates)} duplicate records.")

df_cleaned = df.sort_values('Timestamp').drop_duplicates('Transaction_ID', keep = 'last')

print(df_cleaned)