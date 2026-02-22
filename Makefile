.PHONY: tags graph serve build

tags:
	python3 generate-tags.py

graph:
	python3 generate-graph.py

serve:
	cd docs && bundle exec jekyll serve --livereload

build:
	cd docs && bundle exec jekyll build
