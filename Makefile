.PHONY: all check test build dist clean

all: check test dist

check:
	python setup.py check

test:
	python setup.py test

build:
	python setup.py build

dist: clean build
	python setup.py sdist bdist_wheel

clean:
	python setup.py clean --all
	find . -name \*.pyc -delete
	rm -rf *.egg-info dist
