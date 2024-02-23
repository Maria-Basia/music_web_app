from lib.artist_repository import ArtistRepository
from lib.artist import Artist

"""
When when I call #all in the AlbumRepository
I get all the albums back in a list
"""

def test_get_all_artists(db_connection):
    db_connection.seed("seeds/record_store_html.sql")
    repository = ArtistRepository(db_connection)
    result = repository.all()
    assert result ==[
        Artist(1, 'Pixies', 'Rock'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz')
    ]



"""
When we call ArtistRepository #create
We get a new Artist in the database.
"""
def test_create_artist(db_connection):
    db_connection.seed("seeds/record_store_html.sql")
    repository = ArtistRepository(db_connection)

    created_artist = repository.create(Artist(None, "Red Hot Chilly Peppers", "Rock"))
    assert created_artist == Artist(5, "Red Hot Chilly Peppers", "Rock")

    result = repository.all()
    assert result == [
        Artist(1, 'Pixies', 'Rock'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz'),
        Artist(5, "Red Hot Chilly Peppers", "Rock")
    ]


"""
When we call AlbumRepository #find with a specific id
We get the record attached to this id.
"""

def test_find_artist_with_id(db_connection):
    db_connection.seed("seeds/record_store_html.sql")
    repository = ArtistRepository(db_connection)
    result = repository.find(2)
    assert result == Artist(2, 'ABBA', 'Pop')