from connect import *
 
def read_songs():
    try:
        "method 1"
        # allSongs = dbCursor.execute("SELECT * FROM songs").fetchall()
 
 
        # or
 
        "method 2"
        dbCursor.execute("SELECT * FROM songs")
        allSongs = dbCursor.fetchall() # the fetchall method retrieve all selected songs/rows/records
 
        if allSongs:
            # format output
            " index    0       1       2         3    "
            print("SongID | Artist | Title  | Genre  ")
            print("*" * 60)
 
            for aSong in allSongs:
                print(f"{aSong[0]:5} | {aSong[1]:30} | {aSong[2]:30} | {aSong[3]:20}")
        else:
            print("No Song found in the songs table")
   
    except sql.OperationalError as e:
        print(f"failed because:  {e}")
 
    except sql.ProgrammingError as pe:
         print(f"failed because of Programming Error:  {pe}")
 
    except sql.Error as er:
         print(f"failed because Error:  {er}")
read_songs()
 