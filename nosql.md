# NOSQL DATABASE MANAGEMENT SYSTEM USED TO MODEL DATA FOR COLSTON AVENUE(MONGODB)
I used MongoDB to model data for location: COLSTON AVENUE,MongoDB is a popular NoSQL document-oriented database that stores data in flexible, JSON-like documents, which makes it easy to represent complex hierarchical relationships.As a document database, MongoDB makes it easy for developers to store structured or unstructured data. It uses a JSON-like format to store documents. This format directly maps to native objects in most modern programming languages, making it a natural choice for developers, as they don’t need to think about normalizing data. MongoDB can also handle high volume and can scale both vertically or horizontally to accommodate large data loads.

One of the key benefits of MongoDB is its ability to store and manage unstructured data, which makes it well-suited for a wide range of applications, including content management systems, mobile applications, and Internet of Things (IoT) solutions. It is also known for its ease of use and quick development times due to its flexible schema and ability to store related data in a single document.

As a document base database MongoDB has the following attributes: 
Key-Value fields
Polymorphism
JSON/BSON format
Array
Sub-documents

## Implementation and processes
i downloaded and installed MongoDB from www.mongodb.com. 
Then i used PIP3 to install PyMongo, and afterwards launched mongoDB compass and established a connection to the server on localhost: 27017.
Using Python environment, i imported pymongo, and proceeded to make a connection to the localhost ip address. 
I created mongoobject Client which i called ,  nosqlclient database called pollutionDataBase and collection called readings.

Find the codes below:

import pymongo
import pandas as pd

try:
    ## To create a MongoClient object and connect to a MongoDB database
    nosqlclient = pymongo.MongoClient("mongodb://localhost:27017/")
    database_name = "pollutionDataBase"
    db_names = nosqlclient.list_database_names()

    if database_name in db_names:
        nosqlclient.drop_database(database_name)
    
    database = nosqlclient[database_name]
    collection = database['readings']

    station_data = {
        "station_id" : 501,
        "location": "Colston Avenue",
        "geo_point_2d": "51.455269382758324, -2.596648828557916"
    }

    readings = []
    df = pd.read_csv('Data/clean.csv', low_memory=False, sep=",")

    count =0
    for index, row in df.iterrows():
        if count == 1000:
            break
    
        site_id =  row['SiteID']
        if site_id == 501:
            reading_data = {
                "Data Time": "2019-07-02T05:00:00+00:00",
                "Nox" : 36.3258,
                "NO2": 19.9612,
                "NO" : 10.6792,
                "PM10": 11.325,
                "NVPM10": "null",
                "VPM10": "null",    
                "NVPM2.5": "null",
                "PM2.5": "null",
                "VPM2.5": "null",
                "CO": "null",
                "O3": "null",
                "SO2": "null",
                "Temperature": 15.6,
                "RH": "null",   
                "Air Pressure": "null",
                "DateStart": "2018-11-30T00:00:00+00:00",
                "DateEnd": "null",
                "current": "TRUE",
                "Instrument Type": "Continuous (Reference)"
            }

            readings.append(reading_data)
            count +=1
        

    final_object = {
        "station": station_data,
        "readings": readings
    }

    collection.insert_one(final_object)

except Exception as ex:
    print(f"Error occured: {ex}")

I was able to extract data for  station, called  colston  Avenue School.
On the python environment i converted it to a JSON format then insert the data to the collection and then imported to mongoDB, which gives the output displayed below. 


Note: only 2 rows of the output is displayed below for reference purpose.


[{
  "_id": {
    "$oid": "645ba3ed92aad0fcc6164c5b"
  },
  "station": {
    "station_id": 501,
    "location": "Colston Avenue",
    "geo_point_2d": "51.455269382758324, -2.596648828557916"
  },
  "readings": [
    {
      "Data Time": "2019-07-02T05:00:00+00:00",
      "Nox": 36.3258,
      "NO2": 19.9612,
      "NO": 10.6792,
      "PM10": 11.325,
      "NVPM10": "null",
      "VPM10": "null",
      "NVPM2.5": "null",
      "PM2.5": "null",
      "VPM2.5": "null",
      "CO": "null",
      "O3": "null",
      "SO2": "null",
      "Temperature": 15.6,
      "RH": "null",
      "Air Pressure": "null",
      "DateStart": "2018-11-30T00:00:00+00:00",
      "DateEnd": "null",
      "current": "TRUE",
      "Instrument Type": "Continuous (Reference)"
    },
    {
      "Data Time": "2019-07-02T05:00:00+00:00",
      "Nox": 36.3258,
      "NO2": 19.9612,
      "NO": 10.6792,
      "PM10": 11.325,
      "NVPM10": "null",
      "VPM10": "null",
      "NVPM2.5": "null",
      "PM2.5": "null",
      "VPM2.5": "null",
      "CO": "null",
      "O3": "null",
      "SO2": "null",
      "Temperature": 15.6,
      "RH": "null",
      "Air Pressure": "null",
      "DateStart": "2018-11-30T00:00:00+00:00",
      "DateEnd": "null",
      "current": "TRUE",
      "Instrument Type": "Continuous (Reference)"
    },

















https://www.mongodb.com/why-use-mongodb
https://www.mongodb.com/blog/post/simplifying-iot-connectivity-mydevices-mongodb#:~:text=Database%20requirements%20for%20IoT%20and,(AWS%2C%20Azure%2C%20GCP)