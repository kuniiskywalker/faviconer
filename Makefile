build:
	python setup.py build
.PHONY: build

link-pypi:
	ln -s pypirc ~/.pypirc
.PHONY: link-pypi

package:
	rm -f -r src/.egg-info/* dist/*
	python setup.py sdist
	python setup.py bdist_wheel
.PHONY: package

test:
	python setup.py test
.PHONY: test

local-install: build
	cd build
	pip install -e .
.PHONY: local-install

test-upload: test build package
	python -m readme_renderer README.rst
	twine upload --repository testpypi dist/*
.PHONY: test-upload

test-install:
	pip --no-cache-dir install --upgrade --index-url https://test.pypi.org/simple/ faviconer
.PHONY: test-install

production-upload: test build package
	python -m readme_renderer README.rst
	twine upload --repository pypi dist/*
.PHONY: production-upload

production-install:
	pip --no-cache-dir install --upgrade faviconer
.PHONY: production-install

uninstall:
	pip uninstall faviconer
.PHONY: uninstall
