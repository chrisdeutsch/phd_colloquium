.PHONY:	all clean

all: talk.pdf

clean:
	latexmk -C talk.tex

talk.pdf: talk.tex
	latexmk -pdfxe $<
