from connect import *

def update_song():
    try:
       #SongID is primary key field
       FilmID = int(input("Enter the FilmID of the record to be updated: "))
       dbCursor.execute(f"SELECT * FROM films WHERE FilmID = {FilmID}")

       #The fetchone method a unique(one) record
       row = dbCursor.fetchone()

       #None is a singleton object that checks if a value is present
       if row == None:
           print(f"No record with the FilmID {FilmID} exists")
       else:
            sTitle = input("Enter film title: ")
            syearReleased = input("Enter year released: ")
            sRating = input("Enter film rating: ")
           
           

            #UPDATE songs SET Artist or Title or Genre = ArtistValue or TitleValue or GenreValue WHERE SongID = 1/2/3/4/5...
            dbCursor.execute("UPDATE films SET Title = ?, yearReleased = ?, Genre = ? WHERE FilmID = ?", (sTitle, syearReleased, sRating,FilmID ))
            dbCon.commit()
            print(f"Record with FilmID {FilmID} Updated")

    except sql.OperationalError as e:
        print(f"failed because:  {e}")

    except sql.ProgrammingError as pe:
         print(f"failed because of Programming Error:  {pe}")

    except sql.Error as er:
         print(f"failed because Error:  {er}")
if __name__ == "__main__":
      update_song()
     