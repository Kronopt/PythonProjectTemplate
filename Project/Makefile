.PHONY: help clean lint test coverage docs sdist sdist-test release

help:
	@echo "clean            <description of 'clean'>"
	@echo "lint             <description of 'lint'>"
	@echo "test             <description of 'test'>"
	@echo "coverage         <description of 'coverage'>"
	@echo "docs             <description of 'docs'>"
	@echo "sdist            <description of 'sdist'>"
	@echo "sdist-test       <description of 'sdist-test'>"
	@echo "release          <description of 'release'>"

clean:
	rm -rf build/
	rm -rf dist/
	find . -name '*.pyc' -exec rm -f {} +

lint:
	# lint code

test:
	python -m unittest <tests folder>

coverage:
	# coverage code

docs:
	# build/release docs

sdist:
	python setup.py sdist bdist_wheel

sdist-test:
	twine check dist/*
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

release: sdist
	twine upload dist/*
