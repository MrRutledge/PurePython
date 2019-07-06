import sqlite3

# make a connection
conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

#Populating the database with data
cur.execute('INSERT INTO Tracks (title,plays) VALUES (?, ?)',
            ('Thundurstruck',20))
cur.execute('INSERT INTO Tracks (title,plays) VALUES (?, ?)',
            ('MY Way', 15))
cur.execute('INSERT INTO Tracks (title,plays) VALUES (?, ?)',
            ('Go to hell', 15))
#commiting the update
conn.commit()

#print the data in the database '''Music.sqlite(Tracks)'''
print('Tracks')

cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
    print(row)

cur.execute('DELETE FROM Tracks WHERE plays < 20')
conn.commit()

cur.close()

