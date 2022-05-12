from mylib.fruity import random_fruit
import pytest

def test_random_fruit_no_fixture():
    assert "apple" or "banana" or "cherry" in random_fruit()