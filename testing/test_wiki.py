from mylib.wiki import search_wiki

def test_search_wiki():
    assert "1981–82 Los Angeles Lakers season" in search_wiki()