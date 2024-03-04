from connect import *

def update_tblFilms():
    try:
       
       FilmID = int(input("Enter the FilmID of the film to be updated: "))
       dbCursor.execute(f"SELECT * FROM tblFilms WHERE FilmID = {FilmID}")

    
       row = dbCursor.fetchone()


       if row == None:
           print(f"No record with the FilmID {FilmID} exists")
       else:
           fieldName = input("Enter the field (Title, Rating or Genre): ").title()
           fieldValue = input(f"Enter the value for {fieldName}: ")

            #UPDATE songs SET Artist or Title or Genre = ArtistValue or TitleValue or GenreValue WHERE SongID = 1/2/3/4/5...
           dbCursor.execute(f"UPDATE films SET {fieldName} = ? WHERE FilmID = ? ", (fieldValue,FilmID))
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
     