# this search file searches for songs, is also called reports


from connect import *
 
def search_song():
    try:
        # search by SongID or Artist or Title or Genre
        field = input("Search by SongID or Artist or Title or Genre: ")
 
        if field == "SongID":
            #search by SongID
            songID = int(input("Enter SongID: "))
            dbCursor.execute("SELECT * FROM songs WHERE SongID = ?", (songID,))
            row = dbCursor.fetchone()
 
            if row == None:
                print(f"No record with the SongID {songID} provided exiss in the table")
            else:
                print(row)
        elif field in ["Artist" , "Title" , "Genre"]:
            #search by Artist or Title or Genre
            strInput = (input(f"Enter the value for the field {field}"))
 
            #SELECT * FROM songs WHERE "Artist" or "Title" or "Genre" LIKE "Dance" or "MJ" or "Pop"
            dbCursor.execute(f"SELECT * FROM songs WHERE {field} LIKE '%{strInput}%' ")
 
            rows = dbCursor.fetchall() # return all records that match the strinput variable
 
            if not rows:
                print(f"No record(s) with field {field} matching {strInput}")
            else:
                # display all matching records base on the field and strInput
                for records in rows:
                    print(records)
        else:
            # where the field to search is not SongID,  Artist" , "Title" , "Genre"
            print(f"Search field {field} invalid!!!!")
    except sql.OperationalError as e:
        print(f"failed because:  {e}")
 
    except sql.ProgrammingError as pe:
         print(f"failed because of Programming Error:  {pe}")
 
    except sql.Error as er:
         print(f"failed because Error:  {er}")
search_song()
 
 
 

