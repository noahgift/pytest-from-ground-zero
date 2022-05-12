from random import choices


def random_fruit():
    fruits = ["apple", "banana", "cherry"]
    return choices(fruits)[0]
