from mylib.wiki import search_wiki
from time import sleep

def test_search_wiki():
    assert "1981–82 Los Angeles Lakers season" in search_wiki()

def test_slow_test():
    sleep(3)
    assert "1981–82 Los Angeles Lakers season" in search_wiki()