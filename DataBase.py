#SACHIN ADD MORE SONGS
import sqlite3

class Database():
    def __init__(self):
        return

    def Create(self):
        db = sqlite3.connect('main.db')
        c = db.cursor()
        try:
          
          c.execute('''CREATE TABLE artists(
                      name_of_artist text,
                      times_played int
                   )
                    ''')
          db.commit()
          c.execute('''CREATE TABLE genre(
                      name_of_genre text,
                      times_played int
                   )
                    ''')
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
            
            
          c.execute("INSERT INTO main VALUES(:song,:artist,:genre,:popular,:times_played)",
                              {
                                  'song':'Night Changes',
                                  'artist':'One Direction',
                                  'genre':'Pop Rock',
                                  'popular':'True,
                                  'times_played':0
                              }
                            )
          db.commit()
          c.execute("INSERT INTO main VALUES(:song,:artist,:genre,:popular,:times_played)",
                              {
                                  'song':'Living life. In the night',
                                  'artist':'Sierra kid',
                                  'genre':'pop',
                                  'popular':'false',
                                  'times_played':0
                              }
                            )
          db.commit()
        except:
          return False
