.PHONY: tags exports graph serve build validate-sidebar

tags:
	python3 generate-tags.py

exports:
	python3 generate-exports.py

graph:
	python3 generate-graph.py

validate-sidebar:
	python3 validate-sidebar.py --cap 5 --docs-dir docs

serve:
	cd docs && bundle exec jekyll serve --livereload

build:
	cd docs && bundle exec jekyll build
