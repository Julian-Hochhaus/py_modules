all: build/main.pdf


TeXOptions = -lualatex \
			 -interaction=nonstopmode \
			 -halt-on-error \
			 -output-directory=build
build/example.tex: example.py| build
			 						python example.py

build/main.pdf: build/example.tex
build/main.pdf: FORCE | build
	latexmk $(TeXOptions) main.tex

FORCE:
build:
	mkdir -p build/

clean:
	rm -rf build
