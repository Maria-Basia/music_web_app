from lib.album import Album

class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * from albums")
        albums = []
        for row in rows:
            album = Album(row['id'], row['title'], row['release_year'], row['artist_id'])
            albums.append(album)
        return albums
    

    def create(self, album):
        rows = self._connection.execute("INSERT INTO albums (title, release_year, artist_id) VALUES(%s, %s, %s) RETURNING id", [album.title, album.release_year, album.artist_id])
        row = rows[0]
        album.id = row["id"]
        return album
    
    # Find a single book by its id
    def find(self, album_id):
        rows = self._connection.execute(
            'SELECT * from albums WHERE id = %s', [album_id])
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])

