.PHONY:	all clean

all: talk.pdf

clean:
	latexmk -C talk.tex

talk.pdf: talk.tex
	latexmk -synctex=1 -halt-on-error -pdfxe $<
