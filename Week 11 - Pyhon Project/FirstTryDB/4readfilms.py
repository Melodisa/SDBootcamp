from 2connect.py import *

def read_tblFilms():
    try:
        dbCursor.execute("SELECT * FROM tblFilms")
        alltblFilms = dbCursor.fetchall() 

        if alltblFilms:
            " index    0       1                                2                                3    "
            print("Title     | Genre                       | yearReleased                          |Rating  ")
            print("*" * 100)

            for atblFilms in alltblFilms:
                print(f"{atblFilms[0]:10} | {atblFilms[1]:30} | {atblFilms[2]:30} | {atblFilms[3]:20}")
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
    read_songs()




