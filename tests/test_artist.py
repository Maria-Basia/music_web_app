from lib.artist import Artist

"""
When I construct an Album with the fields id, title, release_year and atrist_id
they reflected in the album properties
"""

def test_constructs_with_fields():
    artist = Artist(1, 'Pixies', 'Rock')
    assert artist.id == 1
    assert artist.name == 'Pixies'
    assert artist.genre == 'Rock'

def test_equality():
    artist_1 = Artist(1, 'Pixies', 'Rock')
    artist_2 = Artist(1, 'Pixies', 'Rock')
    assert artist_1 == artist_2

def test_formatting():
    artist_1 = Artist(1, 'Pixies', 'Rock')
    assert str(artist_1) == "Artist(1, Pixies, Rock)"