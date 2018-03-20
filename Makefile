.PHONY: all install dev-install check test build dist upload test-upload docs view clean-docs tidy clean

all: check test docs dist

install:
	pip install -r requirements.txt

dev-install:
	pip install -r dev-requirements.txt

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

test-upload:
	twine upload -u flyingcampdesign --repository-url https://test.pypi.org/legacy/ dist/*

docs:
	$(MAKE) -C docs html

view:
	open docs/_build/html/index.html

clean-docs:
	rm -rf docs/apidoc/
	$(MAKE) -C docs clean

tidy:
	find . -name \*.pyc -delete
	find . -name __pycache__ -delete

clean: clean-docs tidy
	python setup.py clean --all
	rm -rf *.egg-info dist
	rm -f *.html
