import sqlite3 as sql # import the sqlite3 module and assigned it an alias

try:
    # to use  sqlite(sql) module we start by creating a variable(object)
    # to hold the path to folder(file)
    # use connect function to open folder path then file
    with sql.connect("Week 10 Codebase/Pt9_10DB/dfe6w4.db") as dbCon: # dbCon hold the folder and file path
        #use to execute sql statement with the execute method
        dbCursor = dbCon.cursor()

except sql.OperationalError as e: # raise sql error
    # handling the error 
    print(f"Connection Failed: {e}")

       

