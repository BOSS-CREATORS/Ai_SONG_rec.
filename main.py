#SONGS HAVE BEEN FILLED DO NOT TOUCH ANYTHING


####################################################
#               SONG RECOMMENDATIONS               #
####################################################


import sqlite3

#############################################################
class Database():
    def __init__(self):
        return

    def Create(self):
        db = sqlite3.connect('main.db')
        c = db.cursor()
        try:
            c.execute('''CREATE TABLE main(
                              song_name text,
                              artist text,
                              genre text,
                              popular text,
                              times_played int
                              )
                              ''')
            db.commit()
            c.execute("INSERT INTO main VALUES(:song,:artist,:genre,:popular,:times_played)",
                                {
                                    'song':'Believer',
                                    'artist':'Imagine Dragons',
                                    'genre':'pop rock',
                                    'popular':'true',
                                    'times_played':0
                                }
                              )
            db.commit()
            c.execute("INSERT INTO main VALUES(:song,:artist,:genre,:popular,:times_played)",
                                {
                                    'song':'Dynamite',
                                    'artist':'BTS',
                                    'genre':'korean pop',
                                    'popular':'true',
                                    'times_played':0
                                }
                              )
            db.commit()
            c.execute("INSERT INTO main VALUES(:song,:artist,:genre,:popular,:times_played)",
                                {
                                    'song':'Butter',
                                    'artist':'BTS',
                                    'genre':'korean pop',
                                    'popular':'true',
                                    'times_played':0
                                }
                              )
            db.commit()
            c.execute("INSERT INTO main VALUES(:song,:artist,:genre,:popular,:times_played)",
                                {
                                    'song':'Thunder',
                                    'artist':'Imagine Dragons',
                                    'genre':'pop rock',
                                    'popular':'true',
                                    'times_played':0
                                }
                              )
            db.commit()
            c.execute("INSERT INTO main VALUES(:song,:artist,:genre,:popular,:times_played)",
                                {
                                    'song':'Senorita',
                                    'artist':'Shawn Mendes',
                                    'genre':'Pop',
                                    'popular':'true',
                                    'times_played':0
                                }
                              )
            db.commit()
            c.execute("INSERT INTO main VALUES(:song,:artist,:genre,:popular,:times_played)",
                                {
                                    'song':'Stitches',
                                    'artist':'Shawn Mendes',
                                    'genre':'Pop',
                                    'popular':'true',
                                    'times_played':0
                                }
                              )
            db.commit()
            c.execute("INSERT INTO main VALUES(:song,:artist,:genre,:popular,:times_played)",
                                {
                                    'song':'Savage Love',
                                    'artist':'Jason Derulo',
                                    'genre':'Pop',
                                    'popular':'true',
                                    'times_played':0
                                }
                              )
            db.commit()
            c.execute("INSERT INTO main VALUES(:song,:artist,:genre,:popular,:times_played)",
                                {
                                    'song':'Waiting for Love',
                                    'artist':'Avicii',
                                    'genre':'Progressive House',
                                    'popular':'true',
                                    'times_played':0
                                }
                              )
            db.commit()
            c.execute("INSERT INTO main VALUES(:song,:artist,:genre,:popular,:times_played)",
                                {
                                    'song':'Wake me up',
                                    'artist':'Avicii',
                                    'genre':'Progressive House',
                                    'popular':'true',
                                    'times_played':0
                                }
                              )
            db.commit()
            c.execute("INSERT INTO main VALUES(:song,:artist,:genre,:popular,:times_played)",
                                {
                                    'song':'Let me down slowly',
                                    'artist':'Alec Benjamin',
                                    'genre':'Pop',
                                    'popular':'true',
                                    'times_played':0
                                }
                              )
            db.commit()
            c.execute("INSERT INTO main VALUES(:song,:artist,:genre,:popular,:times_played)",
                                {
                                    'song':'Bad at love',
                                    'artist':'Halsey',
                                    'genre':'Pop',
                                    'popular':'false',
                                    'times_played':0
                                }
                              )
            db.commit()
            c.execute("INSERT INTO main VALUES(:song,:artist,:genre,:popular,:times_played)",
                                {
                                    'song':'Without Me',
                                    'artist':'Halsey',
                                    'genre':'Pop',
                                    'popular':'true',
                                    'times_played':0
                                }
                              )
            db.commit()
            c.execute("INSERT INTO main VALUES(:song,:artist,:genre,:popular,:times_played)",
                                {
                                    'song':'Animals',
                                    'artist':'Martin Garrix',
                                    'genre':'Progressive House',
                                    'popular':'true',
                                    'times_played':0
                                }
                              )
            db.commit()
            c.execute("INSERT INTO main VALUES(:song,:artist,:genre,:popular,:times_played)",
                                {
                                    'song':'jealousy,jealousy',
                                    'artist':'Olivia Rodrigo',
                                    'genre':'pop rock',
                                    'popular':'false',
                                    'times_played':0
                                }
                              )
            db.commit()
            c.execute("INSERT INTO main VALUES(:song,:artist,:genre,:popular,:times_played)",
                                {
                                    'song':'In the name of love',
                                    'artist':'Martin Garrix',
                                    'genre':'Progressive House',
                                    'popular':'false',
                                    'times_played':0
                                }
                              )
            db.commit()
        except:
            return 'Table Exists'

result = Database().Create()
#############################################################

class UserInformation():
    def __init__(self):
        return

    def Create(self):
        try:
            db = sqlite3.connect('userInformation.db')
            c = db.cursor()
            c.execute('''CREATE TABLE info(
                    favourite_song text,
                    favourite_artist text,
                    artist_played int,
                    song_played int
                    '''
                    )

            db.commit()
            return 'Created file'
        except:
            return 'File path already exists'

Var = UserInformation().Create()
print(Var)

class AI():
    def __init__(self):
        return
    def Run(self):
        while True:
            a = input('Enter a song:')
            a = a.lower()
            db = sqlite3.connect('userInformation.db')
            







