.PHONY: tags serve build validate-sidebar

tags:
	python3 generate-tags.py

validate-sidebar:
	python3 validate-sidebar.py --cap 5 --docs-dir docs

serve:
	cd docs && bundle exec jekyll serve --livereload

build:
	cd docs && bundle exec jekyll build
