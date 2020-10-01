import mysql.connector
from uuid import uuid4

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="MyMusicApp"
)
cursor = db.cursor()

genres = ['Rock', 'Pop', 'Rap', 'R&B']

def get_song_data_by_id(id):
    sql = "SELECT * FROM songs where id = '%s'" % id
    cursor.execute(sql)
    song = cursor.fetchone()
    return song

def get_songs(id, name, genre, artist, length, path, ranking):
    sql = '''
        SELECT *
        FROM songs
        WHERE'''
    if id: sql += 'id = "' + id + '" or '
    if name: sql += 'name = "' + name + '" or '
    if genre: sql += 'genre = "' + genre + '" or '
    if artist: sql += 'artist = "' + artist + '" or '
    if length: sql += 'length = ' + length + ' or '
    if path: sql += 'path = "' + path + '" or '
    if ranking > 0: sql += 'ranking = ' + ranking

    if sql[-5:] == 'WHERE': sql = sql[:-5]
    if sql[-4:] == ' or ': sql = sql[:-4]

    cursor.execute(sql)
    songs = cursor.fetchall()
    # print songs
    return songs

def insert_song(id, name, genre, artist, length, path, ranking):
    if (ranking < 0 or ranking > 5): return # need to be 0-5
    if genre not in genres: return # not in enum
    sql = '''
        INSERT INTO songs
        (id, name, genre, artist, length, song_mp3_file_path, ranking)
        VALUES
        ('%s', '%s', '%s', '%s', %d, '%s', %d)''' % (id, name, genre, artist, length, path, ranking)
    cursor.execute(sql)
    db.commit()
    # if not inserted correctly then row count should be 0 (falsy)
    return cursor.rowcount

def update_by_id(id, name, genre, artist, length, path, ranking):
    if (ranking < 0 or ranking > 5): return # need to be 0-5
    if genre not in genres: return # not in enum
    song = get_song_data_by_id(id)
    sql = '''
        UPDATE songs
        SET
        name = "%s", genre = "%s", artist = "%s", length = "%d", path = "%s", ranking = "%s"
        WHERE id = "%s"'''
    cursor.execute(sql % (
        name if name else song.name,
        genre if genre else song.genre,
        artist if artist else song.artist,
        length if length else song.length,
        path if path else song.path,
        ranking if ranking else song.ranking,
        id
        )
    )
    db.commit()
    return cursor.rowcount

def delete_song_by_id(id):
    sql = '''
        DELETE FROM songs
        WHERE id = "%s"''' % id
    cursor.execute(sql)
    db.commit()
    # if not inserted correctly then row count should be 0 (falsy)
    return cursor.rowcount

# get_songs("", "", "", "", 0, "", -1)
# get_songs("", "Song1", "", "", 0, "", -1)
