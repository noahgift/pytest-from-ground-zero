from mylib.fruity import random_fruit
import pytest


class Fruit:
    def __init__(self, name):
        self.my_fruit = name

# Arrange
@pytest.fixture
def fruit_bowl():
    return [Fruit("strawberry"), Fruit("banana"), Fruit("cherry")]

def test_random_fruit_fixture(fruit_bowl):
    # Act
    fruit_salad = fruit_bowl
    assert fruit_salad[0].my_fruit or\
        fruit_salad[1].my_fruit or\
        fruit_salad[2].my_fruit in random_fruit()

    



def test_random_fruit_no_fixture():
    assert "apple" or "banana" or "cherry" in random_fruit()