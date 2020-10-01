from flask import Flask
from uuid import uuid4

app = Flask(__name__)

@app.route('/')
def landing():
    return "Hello Landing"

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        print "land on /create GET"
        return "render_template('create')"

    elif request.method == 'POST':
        print "sent request to /create POST"
        name = request.args.get('name')
        genre = request.args.get('genre')
        length = request.args.get('length')
        path = request.args.get('path')
        id = uuid4()
        # success = db.insert_song(id=id, name=name, genre=genre, length=length, path=path, ranking=0)
        success = "success"
        if success:
            return "render_template('create_success')"
        else:
            return "render_template('error')"

    else:
        print "Wrong rest method"
        return "render_template('error')"


@app.route('/delete', methods=['GET', 'DELETE'])
def delete():
    if request.method == 'GET':
        print "land on /delete GET"
        return "render_template('delete')"

    elif request.method == 'POST':
        print "sent request to /delete"
        id = request.args.get('id')
        # success =  db.delete_song_by_id(id)
        success = "success"
        if success:
            return "render_template('delte_success')"
        else:
            return "render_template('error')"

    else:
        print "Wrong rest method"
        return "render_template('error')"


@app.route('/play', methods=['GET'])
def play():
    if request.method == 'GET':
        print "land on /play GET"
        id = request.args.get('id')
        # song_data = db.get_song_data_by_id()
        song_data = "song_data"
        if song_data:
            return "render_template('play', song_data=song_data)"
        else:
            return "render_template('error')"

    else:
        return "Wrong rest method"
        return "render_template('error')"


@app.route('/update', methods=['GET', 'PUT'])
def update():
    if request.method == 'GET':
        print "land on /update GET"
        id = request.args.get('id')
        name = request.args.get('name')
        genre = request.args.get('genre')
        length = request.args.get('length')
        path = request.args.get('path')
        ranking = request.args.get('ranking')
        return "render_template('update', id=id, name=name, genre=genre, length=length, path=path, ranking=ranking)"

    elif request.method == 'PUT':
        print "land on /update PUT"
        id = request.args.get('id')
        name = request.args.get('name')
        genre = request.args.get('genre')
        length = request.args.get('length')
        path = request.args.get('path')
        ranking = request.args.get('ranking')
        # updated = db.update_by_id(name=name, genre=genre, length=length, path=path, ranking=ranking)
        updated = "success"
        if updated:
            return "render_template('update_successful')"
        else:
            return "render_template('could_not_update')"

    else:
        return "Wrong rest method"
        return "render_template('error')"


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        print "land on /search GET"
        return "render_template('search')"

    elif request.method == 'POST':
        print "land on /search POST"
        id = request.args.get('id')
        name = request.args.get('name')
        genre = request.args.get('genre')
        length = request.args.get('length')
        path = request.args.get('path')
        ranking = request.args.get('ranking')

        songs = get_songs(id, name, genre, artist, length, path, ranking)
        if len(songs) == 0:
            return "render_template('no_songs_found')"
        elif len(songs) == 1:
            return "render_template('song_found', song=songs[0])"
        else:
            return "render_template('many_songs', songs=songs)"
    else:
        return "Wrong rest method"
        return "render_template('error')"


def get_songs(id="", name="", genre="", artist="", length=0, path="", ranking=0):
    # songs = db.get_songs
    songs = []
    if songs:
        return songs
    else:
        print "Could not find songs"
        return


app.run()
