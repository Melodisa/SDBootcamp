
from connect import * 2connect.py

dbCursor.execute(""" 
CREATE TABLE "tblFilms" (
	"FilmID"  INTEGER NOT NULL UNIQUE,
	"Title"	TEXT,
	"yearReleased"	INTEGER NOT NULL,
	"Rating"	TEXT,
	"Duration"	INTEGER,
    "Genre"   TEXT                     
)""")


