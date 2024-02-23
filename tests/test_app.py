from playwright.sync_api import Page, expect

# Tests for your routes go here
def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store_html.sql")
    page.goto(f"http://{test_web_address}/albums")
    paragraph_tags = page.locator("p")
    h3_tags = page.locator("h3")
    expect(h3_tags).to_have_text([
        "Title: Doolittle",
        "Title: Surfer Rosa"
    ])
    expect(paragraph_tags).to_have_text([
        "Released: 1989",
        "Released: 1988"
    ])

def test_get_single_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store_html.sql")
    page.goto(f"http://{test_web_address}/albums/2")
    title_element = page.locator(".t-title")
    expect(title_element).to_have_text("Surfer Rosa")
    release_year = page.locator(".t-release_year")
    expect(release_year).to_have_text("Release year: 1988")



"""
The page returned by GET /albums should contain a link for 
each album listed. It should link to /albums/<id>, 
where <id> is the corresponding album's id. 
That page should then show information about the specific album.
"""

def test_visit_album_show_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store_html.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text = Title: Surfer Rosa")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Surfer Rosa")
    paragraph_tag = page.locator("p")
    expect(paragraph_tag).to_have_text([
        "Release year: 1988", 
        "Artist: Pixies"
    ])


"""
Add a route GET /artists which returns an HTML 
page with the list of artists. This page should 
contain a link for each artist listed, linking to /artists/<id> 
where <id> needs to be the corresponding artist id.
"""

def test_get_all_artists(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store_html.sql")
    page.goto(f"http://{test_web_address}/artists")
    h3_tags = page.locator("h3")
    paragraph_tags= page.locator("p")
    expect(h3_tags).to_have_text = ([
        "Name: Pixies",
        "Name:ABBA",
        "Name: Taylor Swift",
        "Name: Nina Simone"
    ]) 
    expect(paragraph_tags).to_have_text = ([
        "Rock",
        "Pop",
        "Pop",
        "Jazz"
    ]) 


"""
Add a route GET /artists/<id> which returns
an HTML page showing details for a single artist.
"""

def test_get_single_artist(db_connection, test_web_address, page):
    db_connection.seed("seeds/record_store_html.sql")
    page.goto(f"http://{test_web_address}/artists/1")
    h1_tags = page.locator("ht-name")
    paragraph_tags = page.locator("t-genre")
    expect(h1_tags).to_have_text = ("Pixies")
    expect(paragraph_tags).to_have_text = ("Rock")


"""
The page returned by GET /artists should contain a link for 
each artist listed. It should link to /artists/<id>, 
where <id> is the corresponding artists's id. 
That page should then show information about the specific artist.
"""

def test_visit_single_artist_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store_html.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text = Name: Pixies")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Artist name: Pixies")
    paragraph_tag = page.locator("p")
    expect(paragraph_tag).to_have_text("Genre: Rock")


# """
# When we create a new album 
# we can see it reflected in the list of albums
# """
# def test_create_new_album(page, test_web_address, db_connection):
#     db_connection.seed("seeds/record_store_html.sql")
#     page.goto(f"http://{test_web_address}/artists")
#     page.click("text = 'Add a new album'")
