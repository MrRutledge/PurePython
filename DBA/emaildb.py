import sqlite3

## making a connection
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

#check if the data exists and drop it if it does
cur.execute('DROP TABLE IF EXISTS Counts')

#create a table
cur.execute('''CREATE TABLE Counts(email TEXT, count INTEGER)''')
#
##
#As user to enter the file they want to analyse
fname = input('Enter file ya:')
if (len(fname)<1): fname='../Data/mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count From Counts WHERE email = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email,count) VALUES (?,1)''',(email,))
    else:
        cur.execute('UPDATE Counts Set count = count +1  WHERE email = ?', (email,))
    
    conn.commit()
    sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

    for row in cur.execute(sqlstr):
        print(str(row[0]),row[1])

cur.close()
