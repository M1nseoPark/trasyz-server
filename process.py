import pandas as pd
import sqlite3

# Read csv file
df = pd.read_csv("pm_info2.csv")

# Connect to (create) database
database = "db.sqlite3"
conn = sqlite3.connect(database)
dtype = {
    "name" : "CharField",
    "address" : "CharField",
    "latitude" : "FloatField",
    "longitude" : "FloatField",
    "kickboard" : "IntegerField",
    "bicycle" : "IntegerField"
}
df.to_sql(name="manager_parkinglot", con=conn, if_exists='replace', dtype=dtype, index=True, index_label="id")
conn.close()