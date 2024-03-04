from connect import *

def insert_films():
    try:
        sTitle = input("Enter film title: ")
        syearReleased = input("Enter the year the film was released: ")
        sRating = input("Enter the film rating: ")


        dbCursor.execute("INSERT INTO tblFilms VALUES(NULL,?,?,?)", (sTitle, syearReleased, sRating))

        dbCon.commit()

        print(f"{sTitle} inserted in the film table ")
    except sql.OperationalError as e:
        print(f"failed because:  {e}")

    except sql.ProgrammingError as pe:
        print(f"failed because of Programming Error:  {pe}")

    except sql.Error as er:
        print(f"failed because Error:  {er}")
if __name__ == "__main__":
    insert_songs()  


