from connect import *
from readsongs import *
 
def multiple_records():
    # create a list with records of songs to insert
    songlist = [
    ('Aurora Dawn', 'Sunset Melodies', 'jazz'),
    ('Sage Serenade', 'Ethereal Emotions', 'country'),
    ('Phoenix Blaze', 'Journey to Peace', 'metal'),
    ('Kai Harmony', 'Serenade of Solitude', 'r&b'),
    ('Harmony Rain', 'Dance of Delight', 'folk'),
    ('Luna Sky', 'Serenade of the Sky', 'folk'),
    ('Caden Melody', 'Journey to Peace', 'jazz'),
    ('Ryder Echo', 'Enchanted Embrace', 'rock'),
    ('Harmony Rain', 'Echoes of Enchantment', 'pop'),
    ('Lola Lyric', 'Echoes of Ecstasy', 'electronic'),
    ('Sage Serenade', 'Whimsical Wanderings', 'jazz'),
    ('Sage Serenade', 'Mystical Musings', 'r&b'),

    ]

    # insert the records from the songs list above into the songs table
    dbCursor.executemany("INSERT INTO songs(artist, title, genre) VALUES(?,?,?)" songsList)

 
        # display inserted records from the table
        read_songs() # call the read song function
dump_data()
