from connect import *

def read_films():
    try:
        dbCursor.execute("SELECT * FROM tblFilms")
        allFilms = dbCursor.fetchall() 

        if allFilms:
            print("FilmID     | Title                        | yearReleased         |Rating    |Duration |Genre   ")
            print("*" * 100)

            for Films in allFilms:
                print(f"| {Films[0]:7} | {Films[1]:30} | {Films[2]:12} | {Films[3]:10} | {Films[4]:10} | {Films[5]:20} |")
                print("-" * 100)
        else:
            print("No Film found in the Film table")
    
    except sql.OperationalError as e:
        print(f"failed because:  {e}")

    except sql.ProgrammingError as pe:
        print(f"failed because of Programming Error:  {pe}")

    except sql.Error as er:
        print(f"failed because Error:  {er}")
if __name__ == "__main__":
    read_films()




