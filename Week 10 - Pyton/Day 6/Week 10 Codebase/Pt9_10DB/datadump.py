from connect import *
from readsongs import *
 
def dump_data():
    # open folder/file....
    with open("folder/file.t..t.") as dumpfile:
        # read the contents saved in the dumpfile variable and pass it to sqlInsertScript variable
        sqlInsertScript = dumpfile.read()
 
        # write the content found/stored the sqlInsertScript variable to the table
        dbCursor.executescript(sqlInsertScript)
 
        # display inserted records from the table
        read_songs() # call the read song function
dump_data()
has context menu