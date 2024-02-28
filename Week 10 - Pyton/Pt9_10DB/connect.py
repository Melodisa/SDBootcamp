import sqlite3 as sql # import the sqlite3 module and assign it an alias

try:
    # to use sqlite(sql) module we start by creating a variable(object)
    # to hold the path to folder (path)

# use connect function to open folder path then file
    with sql.connect("Week 10 - Pyton\Pt9_10DB/db.db") as dbCon:
        
        # use to execute sql statement with the execute method
        dbCursor = dbCon.cursor()

except sql.OperationalError as e: # raise sql error
 #handling the error
    print(f"Connection failed: {e}")

    
         

