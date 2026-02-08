import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sqlalchemy import create_engine

df = pd.read_csv('dataNew.csv')

df.fillna(df.median(), inplace = True)

X = df.drop('Potability', axis=1)
y = df['Potability']

model = GaussianNB()
model.fit(X, y)
df['Predicted_Potability'] = model.predict(X)

df['Predicted_Potability'] = model.predict(X)


try:
    engine = create_engine('sqlite:///task1.db')
    df.to_sql('task1', con=engine, if_exists='replace', index=False)
    print("Success: Data pushed to MySQL 'task1' table.")
except Exception as e:
    print(f"Database Error: {e}")
    # Fallback: Save to a new CSV with the predicted values if MySQL is not connected
    df.to_csv('water_quality_results.csv', index=False)
    print("Saved to CSV as a fallback.")