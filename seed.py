import mysql.connector
from uuid import uuid4

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
)
cursor = db.cursor()
#
# try:
#     cursor.execute("DROP DATABASE MyMusicApp")
#     cursor = db.cursor()
# except:
#     print "error drop"

sql = '''
    CREATE DATABASE MyMusicApp
    '''
cursor.execute(sql)


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="MyMusicApp"
)
cursor = db.cursor()
sql = '''
    CREATE TABLE songs
    (id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    genre ENUM("Rock", "Pop", "Rap", "R&B") NOT NULL,
    artist VARCHAR(255) NOT NULL,
    length INT,
    song_mp3_file_path VARCHAR(2055) NOT NULL,
    ranking INT)
    '''
cursor.execute(sql)


sql = '''
    INSERT INTO songs
    (id, name, genre, artist, length, song_mp3_file_path, ranking)
    VALUES
    ('%s', '%s', '%s', '%s', %d, '%s', %d)
    '''
cursor.execute(sql % (str(uuid4()), "Song1", "Rock", "Name1", 111,  "some path1", 5))
cursor.execute(sql % (str(uuid4()), "Song2", "Pop",  "Name2", 222,  "some path2", 4))
cursor.execute(sql % (str(uuid4()), "Song3", "Rap",  "Name3", 333,  "some path3", 3))
cursor.execute(sql % (str(uuid4()), "Song4", "R&B",  "Name4", 444,  "some path4", 2))
cursor.execute(sql % (str(uuid4()), "Song5", "Pop",  "Name5", 5,    "some path5", 1))
cursor.execute(sql % (str(uuid4()), "Song6", "Rock", "Name6", 66,   "some path6", 2))
cursor.execute(sql % (str(uuid4()), "Song7", "Rock", "Name7", 2007, "some path7", 0))
