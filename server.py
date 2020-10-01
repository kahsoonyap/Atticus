from flask import Flask

app = Flask(__name__)

@app.route('/')
def landing():
    return "Hello Landing"

@app.route('/create', methods=['GET', 'POST'])
def create():
    return "Create"

@app.route('/delete', methods=['GET', 'DELETE'])
def delete():
    return "delete"

@app.route('/play', methods=['GET'])
def play():
    return "play"

@app.route('/update', methods=['GET', 'PUT'])
def update():
    return "update"


app.run()
