import pandas as pd

# Define input and output file names
input_file = 'clean.csv'
output_file = 'insert-102.sql'

# Define columns to read and their data types
columns = ['Date Time', 'NOx', 'NO2', 'NO', 'SiteID', 'PM10', 'NVPM10', 'VPM10', 'NVPM2.5', 'PM2.5', 'VPM2.5', 'CO', 'O3', 'SO2', 'Temperature', 'RH', 'Air Pressure', 'Location', 'geo_point_2d', 'DateStart', 'DateEnd', 'Current', 'Instrument Type']
dtypes = {'Date Time': 'str', 'NOx': 'float', 'NO2': 'float', 'NO': 'float', 'SiteID': 'int', 'PM10': 'float', 'NVPM10': 'float', 'VPM10': 'float', 'NVPM2.5': 'float', 'PM2.5': 'float', 'VPM2.5': 'float', 'CO': 'float', 'O3': 'float', 'SO2': 'float', 'Temperature': 'float', 'RH': 'float', 'Air Pressure': 'float', 'Location': 'str', 'geo_point_2d': 'str', 'DateStart': 'str', 'DateEnd': 'str', 'Current': 'int', 'Instrument Type': 'str'}

# Define number of inserts to generate
num_inserts = 100

# Read the CSV file into a dataframe
data = pd.read_csv(input_file, usecols=columns, dtype=dtypes, nrows=num_inserts)

# Convert 'Date Time' column to datetime data type
data['Date Time'] = pd.to_datetime(data['Date Time'])

# Generate SQL insert statements
sql = ''
for index, row in data.iterrows():
    values = row.tolist()
    values[0] = values[0].strftime('%Y-%m-%d %H:%M:%S')  # Convert datetime object to string in the required format
    sql_values = ','.join(str(v) if pd.notna(v) else 'NULL' for v in values)
    sql += f"INSERT INTO main_data VALUES ({sql_values});\n"

# Write SQL insert statements to file
with open(output_file, 'w') as f:
    f.write(sql)

print(f"Done. SQL insert statements written to {output_file}")
