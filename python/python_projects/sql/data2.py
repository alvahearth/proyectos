import sqlite3

#Make a connection to a database(AKA creates a file if it doesn't exist)
connection = sqlite3.connect("mydb.sqlite")

#the cursor method enables the modification of data like .open() in files)
cursor = connection.cursor()

#the execute command is able to put or take away information from the table

#the DROP TABLE IF EXISTS ensures that the table won't be created again if it exists 
cursor.execute("DROP TABLE IF EXISTS tracks")

#the CREATE TABLE command creates a new table, and then you especify the contents in tuples
#the sintax is like this (CREATE TABLE z name (x name TYPE, y name TYPE)")
cursor.execute("CREATE TABLE tracks (name TEXT,plays INTEGER)")

#with the INSERT command you insert new rows in the table, the FROM command specify in wich table you are inserting
#the sintax is like this (y name = x name,y name = x name) and the VALUES (something,something) the ? means a placeholder
cursor.execute("INSERT INTO tracks (name,plays) VALUES (?,?)",
            ("Everything",30))
cursor.execute("INSERT INTO tracks (name,plays) VALUES (?,?)",
            ("Running in the night",25))

#the commit() method forces the data to be updated
connection.commit()

#the SELECT command retrieves the rows we created and we can indicate which column we would like
#the sintax is like this SELECT column,cloumn FROM x table
cursor.execute("SELECT name,plays FROM tracks")

#we can do a loop for the selected rows
for row in cursor:
    print(row)

#The DELETE command deletes the rows we have just created so the program can be run again 
cursor.execute("DELETE FROM tracks WHERE plays < 100")

#another commit to force update of the data
connection.commit()

#and we close the connection
connection.close()