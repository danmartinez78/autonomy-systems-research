.PHONY: tags exports serve build

tags:
	python3 generate-tags.py

exports:
	python3 generate-exports.py

serve:
	cd docs && bundle exec jekyll serve --livereload

build:
	cd docs && bundle exec jekyll build
