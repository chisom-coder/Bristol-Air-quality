import pandas as pd
import time
t0=time.time()
df = pd.read_csv('air-quality-data-2003-2022.csv', delimiter=';', low_memory=False)
print(len(df))
df.shape

# Convert the Timestamp column to a datetime format
df['Date Time'] = pd.to_datetime(df['Date Time'])

# Filter the DataFrame to keep only the records after 00:00 1 Jan 2010
df = df[df['Date Time'] >= '2010-01-01 00:00:00']
print(len(df))
df.shape

# Save the filtered DataFrame to a new CSV file
df.to_csv('crop.csv', index=False)

t1=time.time()
total= t1-t0
print(total)