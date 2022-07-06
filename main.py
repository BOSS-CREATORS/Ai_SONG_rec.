import sqlite3
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
Song1 = ('beliver,,'',,'')
Song2 = ()
Song3 = ()
Song4 = ()
Song5 = ()
Song6 = ()
Song7 = ()
Song8 = ()
Song9 = ()
Song10 = ()
Song11 = ()
Song12 = ()
Song13 = ()
Song14 = ()
Song15 = ()



