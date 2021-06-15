#Python Version: 3.9.4

import sqlite3 #import module

#invoke sqlite 3 then call the method 'connect'
conn = sqlite3.connect('db_assignment.db') #the connect method will create the db

with conn: #'with' the file open
    cur = conn.cursor()#stores the full function in a variable thats easier to read
    #Create the table with two columns.
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_dbassignment( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, \
        col_fileName TEXT NOT NULL)")
    conn.commit()

conn.close()

conn = sqlite3.connect('db_assignment.db')

#provided file names for tuple
fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

for x in fileList:
    if x.endswith('txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_dbassignment (col_filename) VALUES (?)", (x,))
            print(x)
            
conn.close()



