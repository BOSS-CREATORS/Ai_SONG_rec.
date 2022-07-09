import sqlite3

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
              song_played int,
              favourite_genre text,
              genre_played int,
              information text
              )
              '''
              )
      db.commit()
      c.execute("INSERT INTO info VALUES(:a,:a,:a,:a,:a,:a,:b)",{'a':'None','b':'True'})
      db.commit()
    except:
      pass
