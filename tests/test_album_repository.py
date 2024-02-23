from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When when I call #all in the AlbumRepository
I get all the albums back in a list
"""

def test_get_all_albums(db_connection):
    db_connection.seed("seeds/record_store_html.sql")
    repository = AlbumRepository(db_connection)
    result = repository.all()
    assert result ==[
        Album(1, "Doolittle", 1989, 1),
        Album(2, "Surfer Rosa", 1988, 1)
    ]

"""
When we call AlbumRepository #create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/record_store_html.sql")
    repository = AlbumRepository(db_connection)

    created_album = repository.create(Album(None, "Arrival", 1976, 2))
    assert created_album == Album(3, "Arrival", 1976, 2)

    result = repository.all()
    assert result == [
        Album(1, "Doolittle", 1989, 1),
        Album(2, "Surfer Rosa", 1988, 1),
        Album(3, "Arrival", 1976, 2)
    ]


"""
When we call AlbumRepository #find with a specific id
We get the record attached to this id.
"""

def test_find_album_with_id(db_connection):
    db_connection.seed("seeds/record_store_html.sql")
    repository = AlbumRepository(db_connection)
    result = repository.find(2)
    assert result == Album(2, 'Surfer Rosa', 1988, 1)




