from app import app, socketio,emit
from flask import render_template


values = {
    'slider1':25,
    'slider2':0
}
@app.route('/')
def hello_world():
    return render_template('index.html', title="Home page", **values)

# Handler for a message recieved over 'connect' channel
@socketio.on('connect')
def test_connect():
    emit('after connect',  {'data':'Lets dance'})