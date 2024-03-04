from connect import *

def search_song():
    try:
        # dbCursor.execute("SELECT * FROM songs ORDER BY Title DESC")
        # dbCursor.execute("SELECT * FROM songs ORDER BY SongID DESC")
        # dbCursor.execute("SELECT * FROM songs WHERE Genre = 'Pop' ")
        dbCursor.execute("SELECT * FROM songs WHERE Genre NOT LIKE 'Pop' ")

        allsongs = dbCursor.fetchall()
        for songs in allsongs:
            print(songs)
       
   
    except sql.OperationalError as e:
        print(f"failed because:  {e}")

    except sql.ProgrammingError as pe:
         print(f"failed because of Programming Error:  {pe}")

    except sql.Error as er:
         print(f"failed because Error:  {er}")
if __name__ == "__main__":
    search_song()


