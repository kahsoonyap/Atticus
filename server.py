from flask import Flask

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
        song = request.args.get('song')
        # db.insertsong
        return "render_template('create', song=song)"
    else:
        print "Wrong rest method"
    return "create"

@app.route('/delete', methods=['GET', 'DELETE'])
def delete():
    if request.method == 'GET':
        print "land on /delete GET"
        return "render_template('delete')"
    elif request.method == 'POST':
        print "sent request to /delete"
        id = request.args.get('id')
        # db.deletesongbyid
        return "render_template('delete', song=song)"
    else:
        print "Wrong rest method"
    return "Create"

@app.route('/play', methods=['GET'])
def play():
    if request.method == 'GET':
        print "land on /play GET"
    else:
        return "Wrong rest method"
    return "play"

@app.route('/update', methods=['GET', 'PUT'])
def update():
    if request.method == 'GET':
        print "land on /update GET"
        return "render_template('update')"
    elif request.method == 'PUT':
        print "land on /update PUT"

        return "render_template('update', song=song)"
    else:
        return "Wrong rest method"
    return "update"

def get_song(id="", name="", genre="", artist="", length=0, path="", ranking=0):
    songs = []
    # songs = db.getsongs
    return songs



app.run()
