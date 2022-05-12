install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=mylib testing/

format:
	black *.py

lint:
	pylint --disable=R,C $$(git ls-files '*.py')

all: install lint test format