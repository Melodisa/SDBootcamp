import sqlite3 as sql # import the sqlite3 module and assigned it an alias

try:

    with sql.connect("FirstTryDB/Sqlconnect.DB") as dbCon: 
        dbCursor = dbCon.cursor()

except sql.OperationalError as e:  
    print(f"Connection Failed: {e}")


