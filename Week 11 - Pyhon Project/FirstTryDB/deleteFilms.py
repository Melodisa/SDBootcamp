from connect import *

def delete_song():
    try:
       #SongID is primary key field
       FilmID = int(input("Enter the FilmID of the record to be deleted: "))
       dbCursor.execute(f"SELECT * FROM tblFilms WHERE FilmID = {FilmID}")

       #The fetchone method a unique(one) record
       row = dbCursor.fetchone()

       if row == None:
           print(f"Delete is not possible as no record with the FilmID {FilmID} exists!!!")
       else:
           dbCursor.execute("DELETE FROM songs WHERE FilmID = ?",(FilmID,))
           dbCon.commit()
           print(f"The record {FilmID}  deleted from the film ID table")
    
    except sql.OperationalError as e:
        print(f"failed because:  {e}")

    except sql.ProgrammingError as pe:
         print(f"failed because of Programming Error:  {pe}")

    except sql.Error as er:
         print(f"failed because Error:  {er}")       

if __name__ == "__main__":
    delete_song()
