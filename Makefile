.PHONY: install test

install:
	pip3 install -r requirements-dev

test:
	flake8 --ignore=E402,W503 *.py
	pytest tests/

build:
	rm -r dist
	python setup.py sdist

release-test:
	twine upload -r testpypi dist/*

release:
	twine upload -r pypi dist/*
