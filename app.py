import random
from flask import Flask, render_template, request, redirect, url_for
from models.models import db, Playlist, PlaylistItem
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
db.create_all(app=app)

@app.route("/")
def home():
    playlists = Playlist.query.all()
    tracks = PlaylistItem.query.all()

    playlistViewModelArray = []
    
    # Eventualy can join on query w/ sql but this works for now
    for playlist in playlists:
        tracksInCurrentPlaylist = []
        for track in tracks:
            if(track.playlist_id == playlist.id):
                tracksInCurrentPlaylist.append(track)             

        playlistViewModelArray.append({"playlist": playlist, "tracks": tracksInCurrentPlaylist})
        
    return render_template('home.html',playlistViewModelArray=playlistViewModelArray)

@app.route('/add-song', methods = ['POST'])
def addSong():
    song = request.form['song']
    playlistId = request.form['playlist-id']
    print(song)
    print(playlistId)

    newItem = PlaylistItem(track_title=song,spotify_track_id=random.random(),playlist_id=playlistId)
    db.session.add(newItem)
    db.session.commit()
    
    return redirect('/')
    
app.run(debug=True)
