.PHONY: all check test build dist upload apidoc docs clean

all: clean check test docs dist

init:
	pip install -r requirements.txt

init-dev:
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

apidoc:
	sphinx-apidoc -T -f -o docs/apidoc/ aardvark_py/ aardvark_py/aardvark/{darwin,linux,windows}
	# sphinx-apidoc -T -f -o docs/apidoc/ aardvark_py/ aardvark_py/aardvark
	# sphinx-apidoc -T -f -o docs/apidoc/ aardvark_py/

docs: apidoc
	$(MAKE) -C docs html

clean-apidoc:
	rm -rf docs/apidoc/

clean-docs: clean-apidoc
	$(MAKE) -C docs clean

clean: clean-docs
	python setup.py clean --all
	find . -name \*.pyc -delete
	rm -rf *.egg-info dist
	rm -f *.html
