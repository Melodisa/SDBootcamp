from 2connect import *

def search_tblFilms():
    try:
        # search by SongID or Artist or Title or Genre
        field = input("Search by Film: ")

        if field == "Title":
            #search by SongID
            tblFilms = int(input("Enter FilmID: "))
            dbCursor.execute("SELECT * FROM Titles WHERE FilmID = ?", (FilmID,))
            row = dbCursor.fetchone()

            if row == None:
                print(f"No record with the SongID {FilmID} provided exiss in the table")
            else:
                print(row)
        elif field in ["Title" , "yearReleased" , "genre"]:
            #search by Artist or Title or Genre
            strInput = (input(f"Enter the value for the field {field} "))

            #SELECT * FROM songs WHERE "Artist" or "Title" or "Genre" LIKE "Dance" or "MJ" or "Pop"
            dbCursor.execute(f"SELECT * FROM films WHERE {field} LIKE '%{strInput}%' ")

            rows = dbCursor.fetchall() # return all records that match the strinput variable

            if not rows:
                print(f"No record(s) with field {field} matching {strInput}")
            else:
                # display all matching records base on the field and strInput
                for Title in rows:
                    print(Title)
        else:
            # where the field to search is not SongID,  Artist" , "Title" , "Genre"
            print(f"Search field {field} invalid!!!!")
    except sql.OperationalError as e:
        print(f"failed because:  {e}")

    except sql.ProgrammingError as pe:
         print(f"failed because of Programming Error:  {pe}")

    except sql.Error as er:
         print(f"failed because Error:  {er}")
if __name__ == "__main__":
    search_film()


