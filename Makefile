SHELL := /bin/bash

test:
	python ./tests/run.py

release:
	python setup.py register sdist upload
