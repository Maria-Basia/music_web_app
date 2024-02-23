import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


@app.route("/albums", methods = ["GET"])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template('albums/all_albums.html', albums = albums)



@app.route('/albums/<int:id>', methods=['GET'])
def get_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.find(id)
    artist_repository = ArtistRepository(connection)
    artist = artist_repository.find(album.artist_id)
    return render_template('albums/single_album.html', album=album, artist = artist)


@app.route("/albums", methods = ['POST'])
def post_albums():
    if 'title' and 'release_year' and 'artist_id' not in request.form:
        return "You need to submit a title, release year and artist id!", 400
    else:
        album_title = request.form['title']
        album_release_year = request.form['release_year']
        artist_id = request.form['artist_id']
        connection = get_flask_database_connection(app)
        repository = AlbumRepository(connection)
        album = Album(None, album_title, album_release_year, artist_id)
        repository.create(album)
        return "Album created successfully"


@app.route("/artists", methods = ["GET"])
def get_artists():
    connection = get_flask_database_connection
    artist_repository = ArtistRepository(connection)
    artists = artist_repository.all()
    return render_template('/artists/all_artists.html', artists = artists)



# @app.route("/albums", methods = ['GET'])
# def get_albums():
#     connection = get_flask_database_connection(app)
#     repository = AlbumRepository(connection)
#     album_list= repository.all()
#     return str(album_list) 



# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
