.PHONY: tags serve build

tags:
	python3 generate-tags.py

serve:
	cd docs && bundle exec jekyll serve --livereload

build:
	cd docs && bundle exec jekyll build
