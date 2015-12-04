.PHONY: all check test build dist clean

all: clean check test doc dist

check:
	python setup.py check

test:
	python setup.py test

build:
	python setup.py build

dist: build
	python setup.py sdist bdist_wheel

upload:
	twine upload -u flyingcampdesign dist/*

%.html: %.rst
	rst2html.py $< > $@

doc: $(shell find . -name "*.rst" | sed 's/rst/html/')

clean:
	python setup.py clean --all
	find . -name \*.pyc -delete
	rm -rf *.egg-info dist
	rm -f *.html
