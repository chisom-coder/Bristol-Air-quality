import mysql.connector
import pandas as pd

def create_database():
    try:
        # Connect to the database
        conn = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            # connection_timeout=300
        )

        # Create a database
        cur = conn.cursor()
        cur.execute("DROP DATABASE IF EXISTS `pollution-db2`")
        cur.execute("CREATE DATABASE `pollution-db2`")

        # Connect to the database
        conn = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='pollution-db2',
            #connection_timeout=300
        )
        print("Database created successfully!")
        return conn
    except Exception as e:
        print(f"Error creating database: {e}")
        return None

def create_tables(conn):
    try:
        cur = conn.cursor()
        # create the stations table
        cur.execute("""CREATE TABLE IF NOT EXISTS `stations`
                        (`SiteID` INTEGER NOT NULL,
                        `Location`  TEXT NOT NULL,
                        `geo_point_2d` TEXT NOT NULL,
                        PRIMARY KEY(`SiteID`));""")

        # create the readings table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS `Readings` (
                `readingsid` INT NOT NULL AUTO_INCREMENT,
                `Date Time` DATETIME NOT NULL,
                `NOx` FLOAT ,
                `NO` FLOAT ,
                `PM10` FLOAT ,
                `NVPM10` FLOAT ,
                `NVPM2.5` FLOAT ,
                `VPM10` FLOAT ,
                `PM2.5` FLOAT ,
                `VPM2.5` FLOAT ,
                `CO` FLOAT ,
                `O3` FLOAT ,
                `S03` FLOAT ,
                `Temperature REAL` FLOAT ,
                `RH` INT ,
                `Air Pressure` INT ,
                `DateStart` DATETIME ,
                `DateEnd` DATETIME ,
                `Current` TEXT(5) ,
                `Instrument Type` VARCHAR(32) ,
                `Stationid` INT NULL,
                PRIMARY KEY (`readingsid`),
                INDEX `Stationid_idx` (`Stationid` ASC),
                CONSTRAINT `Stationid`
                    FOREIGN KEY (`Stationid`)
                    REFERENCES `stations` (`SiteID`)
                    ON DELETE NO ACTION
                    ON UPDATE NO ACTION
            )
            ENGINE = InnoDB;
        """)

        # create the schema table
        cur.execute("""CREATE TABLE IF NOT EXISTS `schema`
                        (`Measure` TEXT NOT NULL,
                        `Description` TEXT NOT NULL,
                        `Unit` TEXT NOT NULL);""")
        conn.commit()
        print("Tables created successfully!")
    except Exception as e:
        print(f"Error creating tables: {e}")


def insert_data(conn):
    try:
        # Read in data from the CSV file
        data = pd.read_csv('clean.csv', low_memory=False)
        insert_data_to_mysql(conn, data)
    except Exception as e:
        print(f"Error: {e}")


def insert_data_to_mysql(conn, data):
    try:

        numeric_columns = data.select_dtypes(include=['number']).columns
        data[numeric_columns] = data[numeric_columns].fillna(0)

        # Replace NaN values with NULL
        data = data.fillna(0)



        # Insert station data
        station_data = data[['SiteID', 'Location', 'geo_point_2d']].drop_duplicates().reset_index(drop=True)
        cursor = conn.cursor()
        for row in station_data.itertuples(index=False):
            cursor.execute("INSERT IGNORE INTO `stations` (`SiteID`, `Location`, `geo_point_2d`) VALUES (%s, %s, %s)", row)

        # Insert readings data
        readings_data = data.drop(['Location', 'geo_point_2d'], axis=1)
        for index,row in readings_data.iterrows():
            
            if row['DateEnd'] == 'NULL':
                date_end = None
            else:
                date_end = row['DateEnd']
        
            query = "INSERT INTO `Readings` (`Date Time`, `NOx`, `NO`, `Stationid`, `PM10`,`NVPM10`,`NVPM2.5`,`VPM10`,`PM2.5`,`VPM2.5`,`CO`,`O3`,`RH`,`Air Pressure`, `DateStart`, `DateEnd`, `Current`, `Instrument Type`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (row['Date Time'], row['NOx'], row['NO'], row['SiteID'], row['PM10'],row['NVPM10'],row['NVPM2.5'],row['VPM10'],row['PM2.5'],row['VPM2.5'],row['CO'],row['O3'],row['RH'],row['Air Pressure'], row['DateStart'], date_end, row['Current'], row['Instrument Type'])
            cursor.execute(query, values)
            

        conn.commit()
        print("Data inserted successfully!")
    except Exception as e:
        print(f"Error inserting data: {e}")




def main():
    conn = create_database()
    if conn:
        create_tables(conn)
        insert_data(conn)
        conn.close()

if __name__ == '__main__':
    main()
