SHELL=/bin/bash

.PHONY: all clean

all: higgs_massterm.pdf higgs_hhh.pdf higgs_hhhh.pdf

cleanall: clean
	rm -f *.pdf

clean:
	rm -f *.aux
	rm -f *.log
	rm -f *.1
	rm -f *.mp
	rm -f *.t1

%.pdf: %.tex
	pdflatex $<
	mpost $*_fmf.mp
	pdflatex $<
	pdfcrop --margin 3 $*.pdf $*.pdf
