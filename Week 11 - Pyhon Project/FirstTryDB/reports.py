from connect import *

def all_films():
    try: 
        dbCursor.execute("SELECT * FROM tblFilms")
        allFilms = dbCursor.fetchall()

        for film in allFilms: 
            print(film)

    except sql.OperationalError as e:
        print(f"failed because:  {e}")

    except sql.ProgrammingError as pe:
        print(f"failed because of Programming Error:  {pe}")

    except sql.Error as er:
        print(f"failed because Error:  {er}")

def genre():
    try:
        fgenre = (input("Search by film genre (case sensistive): "))
        dbCursor.execute("SELECT * FROM tblFilms WHERE genre = ?", (fgenre,))

        rows = dbCursor.fetchall() 
        if not rows:
            print("No films found with that genre")
        else:
            for row in rows:
                print(row)
    
    except sql.OperationalError as e:
        print(f"failed because:  {e}")

    except sql.ProgrammingError as pe:
        print(f"failed because of Programming Error:  {pe}")

    except sql.Error as er:
        print(f"failed because Error:  {er}")

def year():
    try:
        fyear = int(input("Search by film year:  "))
        dbCursor.execute("SELECT * FROM tblFilms WHERE yearReleased = ?", (fyear,))

        rows = dbCursor.fetchall() 
        if not rows:
            print("No films found within that year")
        else:
            for row in rows:
                print(row)
    
    except sql.OperationalError as e:
        print(f"failed because:  {e}")

    except sql.ProgrammingError as pe:
        print(f"failed because of Programming Error:  {pe}")

    except sql.Error as er:
        print(f"failed because Error:  {er}")

def rating():
    try:
        frating = (input("Search by film rating (case sensistive): "))
        dbCursor.execute("SELECT * FROM tblFilms WHERE rating = ?", (frating,))

        rows = dbCursor.fetchall() 
        if not rows:
            print("No films found with that rating")
        else:
            for row in rows:
                print(row)
    
    except sql.OperationalError as e:
        print(f"failed because:  {e}")

    except sql.ProgrammingError as pe:
        print(f"failed because of Programming Error:  {pe}")

    except sql.Error as er:
        print(f"failed because Error:  {er}")


if __name__ == "__main__":
    all_films()
    genre()
    year()
    rating()
    


