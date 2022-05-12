from mylib.wiki import search_wiki
from time import sleep
import pytest

def test_search_wiki():
    assert "1981–82 Los Angeles Lakers season" in search_wiki()

@pytest.mark.skip(reason="This test is too slow and I added a sleep")
def test_slow_test():
    sleep(3)
    assert "1981–82 Los Angeles Lakers season" in search_wiki()

@pytest.mark.xdist_group(name="groupa")
def test_slow_test_parallel_a1():
    sleep(3)
    assert "1981–82 Los Angeles Lakers season" in search_wiki()
@pytest.mark.xdist_group(name="groupa")
def test_slow_test_parallel_a2():
    sleep(3)
    assert "1981–82 Los Angeles Lakers season" in search_wiki()


@pytest.mark.xdist_group(name="groupb")
def test_slow_test_parallel_b1():
    sleep(3)
    assert "1981–82 Los Angeles Lakers season" in search_wiki()
@pytest.mark.xdist_group(name="groupb")
def test_slow_test_parallel_b2():
    sleep(3)
    assert "1981–82 Los Angeles Lakers season" in search_wiki()
