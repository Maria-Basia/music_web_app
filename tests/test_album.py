from lib.album import Album

"""
When I construct an Album with the fields id, title, release_year and atrist_id
they reflected in the album properties
"""

def test_constructs_with_fields():
    album = Album(1, 'Californication', 1999, 1)
    assert album.id == 1
    assert album.title == 'Californication'
    assert album.release_year == 1999
    assert album.artist_id == 1

def test_equality():
    album_1 = Album(1, 'Californication', 1999, 1)
    album_2 = Album(1, 'Californication', 1999, 1)
    assert album_1 == album_2

def test_formatting():
    album_1 = Album(1, 'Californication', 1999, 1)
    assert str(album_1) == "Album(1, Californication, 1999, 1)"




