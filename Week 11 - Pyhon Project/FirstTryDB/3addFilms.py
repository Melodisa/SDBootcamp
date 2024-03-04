from connect import *

def insert_films():
    try:
        fTitle = input("Enter film title: ")
        fyearReleased = int(input("Enter the year the film was released: "))
        fRating = input("Enter the film rating: ")
        fduration = int(input("The duration of the film"))
        fgenre = input("The genre of the film")


        dbCursor.execute("INSERT INTO tblFilms VALUES(NULL,?,?,?,?,?)", (fTitle, fyearReleased, fRating, fduration, fgenre))

        dbCon.commit()

        print(f"{fTitle} inserted in the film table ")
    except sql.OperationalError as e:
        print(f"failed because:  {e}")

    except sql.ProgrammingError as pe:
        print(f"failed because of Programming Error:  {pe}")

    except sql.Error as er:
        print(f"failed because Error:  {er}")
if __name__ == "__main__":
    insert_films()  


