from connect import *

# create a subroutine to add songs to the songs table
def insert_songs():
    try:
        #SongID is an auto increment field no data is required
        # SongID, Artist, Title, Genre

        # create variables for each field to store the respective data from the input function
        sTitle = input("Enter song title: ")
        sArtist = input("Enter song artist: ")
        sGenre = input("Enter song genre: ")


        dbCursor.execute("INSERT INTO songs VALUES(NULL,?,?,?)", (sTitle, sArtist, sGenre))
        # dbCursor.execute("INSERT INTO songs (Title, Artist,Genre) VALUES(?,?,?)", (sTitle, sArtist, sGenre))
        dbCon.commit() # make the changes in the db table permanent 

        print(f"{sTitle} inserted in the songs table ")
    except sql.OperationalError as e:
        print(f"failed because:  {e}")

    except sql.ProgrammingError as pe:
         print(f"failed because of Programming Error:  {pe}")

    except sql.Error as er:
         print(f"failed because Error:  {er}")
if __name__ == "__main__":
    insert_songs()  # call the function


