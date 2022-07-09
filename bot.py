import sqlite3
import random
class AI():
    def __init__(self):
        return
    def Run(self):
        while True:
            a = input('Enter a song:')
            db = sqlite3.connect('userInformation.db')
            other = sqlite3.connect('main.db')
            c = db.cursor()
            d = other.cursor()
            d.execute('SELECT * FROM main WHERE song_name = :song',{
              'song':a
            }
                     )
            number = d.fetchone()
            number = number[4] + 1
            d.execute('UPDATE main SET times_played = :time WHERE song_name = :song',{'time':number,'song':a})
            other.commit()
            d.execute('SELECT * FROM main WHERE song_name = :song',{
              'song':a
            })
            result = d.fetchall()
            d.execute('SELECT artist FROM main WHERE song_name = :song',{'song':a})
            artist = d.fetchall()
            artist = artist[0][0]
            d.execute('SELECT * FROM main WHERE artist = :artist',{'artist':artist})
            newresult = d.fetchall()
            total = 0
            for i in range(0,len(newresult)):
              total = total+newresult[i][4]
            d.execute("SELECT * FROM artists WHERE name_of_artist = :artist",{'artist':artist})
            result = d.fetchall()
            if len(result)==0:
              d.execute("INSERT INTO artists VALUES (:artist_name,:times_played)",{'artist_name':artist,'times_played':total})
              other.commit()
              d.execute("SELECT * FROM artists")
              result = d.fetchall()
            elif len(result)!=0:
              d.execute("UPDATE artists SET times_played = :times WHERE name_of_artist = :artist",{'artist':artist,'times':total})
              other.commit()
            d.execute("SELECT * FROM artists")
            #FAVOURITE SONG
            d.execute("SELECT song_name,times_played FROM main ORDER BY times_played DESC")
            result = d.fetchall()
            favourite_song = result[0][0]
            song_played = result[0][1]
            d.execute("SELECT name_of_artist,times_played FROM artists ORDER BY times_played DESC")
            result = d.fetchall()
            favourite_artist = result[0][0]
            artist_played = result[0][1]
            d.execute('SELECT * FROM main WHERE song_name = :song',{
              'song':a
            })
            result = d.fetchall()
            d.execute('SELECT genre FROM main WHERE song_name = :song',{'song':a})
            genre = d.fetchall()
            genre = genre[0][0]
            d.execute('SELECT * FROM main WHERE genre = :artist',{'artist':genre})
            newresult = d.fetchall()
            total = 0
            for i in range(0,len(newresult)):
              total = total+newresult[i][4]
            d.execute("SELECT * FROM genre WHERE name_of_genre = :artist",{'artist':genre})
            result = d.fetchall()
            if len(result)==0:
              d.execute("INSERT INTO genre VALUES (:artist_name,:times_played)",{'artist_name':genre,'times_played':total})
              other.commit()
            elif len(result)!=0:
              d.execute("UPDATE genre SET times_played = :times WHERE name_of_genre = :artist",{'artist':genre,'times':total})
              other.commit()
            d.execute("SELECT * FROM genre")
            d.execute("SELECT * FROM genre ORDER BY times_played DESC")
            result = d.fetchall()
            favourite_genre = result[0][0]
            genre_played = result[0][1]
            c.execute("UPDATE info SET favourite_song = :fs,favourite_artist = :fa,song_played = :sp,artist_played = :ap,favourite_genre = :fg,genre_played = :gp WHERE information = :b",{
              'fs':favourite_song,
              'fa':favourite_artist,
              'sp':song_played,
              'ap':artist_played,
              'fg':favourite_genre,
              'gp':genre_played,
              "b":"True"
            })
            db.commit()

            d.execute("SELECT song_name,artist FROM main WHERE artist  = :artist",{'artist':favourite_artist})
            result = d.fetchall()
            d.execute("SELECT song_name,artist FROM main WHERE genre = :genre",{'genre':favourite_genre})
            newresult = d.fetchall()
            
            listOfSongs = []
          
            for i in range(0,len(result)):
              word = result[i][0]+' - '+result[i][1]
              listOfSongs.append(word)
            for i in range(0,len(newresult)):
              newword = newresult[i][0]+ ' - ' + newresult[i][1]
              listOfSongs.append(newword)
            d.execute("SELECT * FROM artists ORDER BY times_played DESC")
            artists = d.fetchall()
            try:
              first_fav = artists[1][0]
              d.execute("SELECT * FROM main WHERE artist = :artist",{'artist':first_fav})
              data = d.fetchall()
              for i in range(0,len(data)):
                song = data[i][0] + ' - ' + data[i][1]
                listOfSongs.append(song)
            except:
              pass
            try:
              first_fav = artists[2][0]
              d.execute("SELECT * FROM main WHERE artist = :artist",{'artist':first_fav})
              data = d.fetchall()
              for i in range(0,len(data)):
                song = data[i][0] + ' - ' + data[i][1]
                listOfSongs.append(song)
            except:
              pass  
            for i in range(0,len(listOfSongs)):
              value = a+' - '+artist
              try:
                if listOfSongs[i] == value:
                  listOfSongs.remove(listOfSongs[i])
                else:
                  pass
              except:
                pass
            randomindex = random.randint(0,len(listOfSongs))
            print('Suggestion: ',listOfSongs[randomindex])
                
              
            
              
                
