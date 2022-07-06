import sqlite3
import youtube_dl
import pytube
import urllib.request
import re

db = sqlite3.connect('songs.db')
c = db.cursor()
c.execute('''
        CREATE TABLE IF NOT EXISTS songs(
            songname text,
            played int,
            genre text,
            popular text,
            artist text
            )
        ''')
db.commit()



