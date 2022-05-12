[![Build](https://github.com/noahgift/pytest-from-ground-zero/actions/workflows/build.yml/badge.svg)](https://github.com/noahgift/pytest-from-ground-zero/actions/workflows/build.yml)
[![Build2](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiZGhyL002azVxblZhdDFUOXM3ZHlYSmdYQ2xobnl2Unh6TTNOOG96bVEzYXN3ZXQ4TFhvSzN3bDcrWVR4b1FVSTJseFltWWhlbk9DTzAycE1VT0Mrbnk4PSIsIml2UGFyYW1ldGVyU3BlYyI6IkJ1VG9FMGJjUGx2K29wSi8iLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)
# pytest-from-ground-zero
This is a new pytest repo that covers the best practices

## Note on Virtualenv
Checkout how if you run `pip freeze | wc -l` there are many package you may not want
Try `which python`

1. `virtualenv ~/.venv`
2. `vim ~/.bashrc` and put in `source ~/.venv/bin/activate`
3.  Verify the right python `which python` and try `pip freeze | wc -l`

## Testing for Multi-Cloud

* AWS Cloud Shell

## Using PyTest

* Use library style:  `python -m pytest -vv --cov=mylib testing/`
* Run tests by keyword expressions: `python -m pytest -vv -k "search"`
* To run a specific test within a module: `python -m pytest -vv testing/test_fruity.py::test_random_fruit`
* Run tests by marker expressions: https://docs.pytest.org/en/7.1.x/how-to/mark.html#mark
* Profile tests: `pytest --durations=10 --durations-min=1.0`
* Skipping `@pytest.mark.skip(reason="no way of currently testing this")`
* [Checkout Fixtures here](https://paiml.com/docs/home/books/testing-in-python/chapter07-pytest-fixtures/)

### Distributed Testing: 

* install: https://pypi.org/project/pytest-xdist/#installation
![Drawing-8 sketchpad](https://user-images.githubusercontent.com/58792/168116462-09d64935-9862-4e3a-9d87-5c160f9f66eb.jpeg)

