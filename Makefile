LATEX=pdflatex
LATEXOPT=--shell-escape

#"nonstopmode" is very verbose. batchmode is not verbose
NONSTOP=--interaction=nonstopmode
#NONSTOP=--interaction=batchmode

LATEXMK=latexmk
LATEXMKOPT=-pdf
CONTINUOUS=-pvc

MAIN=main
SOURCES=source




all: clean-compile

clean-compile: clean compile .showerrors run

compile:
	$(LATEXMK) $(LATEXMKOPT) -pdflatex="$(LATEX) $(NONSTOP) $(LATEXOPT) %O %S" $(MAIN) &> /tmp/errors

run:
	xdg-open $(MAIN).pdf

.showerrors:
	/usr/bin/grep --color=always -A3 "\!.*" /tmp/errors || :

.refresh:
	touch .refresh

continuous: $(MAIN).tex .refresh $(SOURCES)
	$(LATEXMK) $(LATEXMKOPT) $(CONTINUOUS) \
	-pdflatex="$(LATEX) $(LATEXOPT) $(NONSTOP) %O %S" $(MAIN)

force:
	touch .refresh
	rm $(MAIN).pdf
	$(LATEXMK) $(LATEXMKOPT) $(CONTINUOUS) \
	-pdflatex="$(LATEX) $(LATEXOPT) %O %S" $(MAIN)

clean:
	$(LATEXMK) -C $(MAIN)
	rm -f $(MAIN).pdfsync main.pdf  *~ *.tmp *.bbl *.blg *.aux *.end *.fls *.log *.out *.fdb_latexmk

debug:
	$(LATEX) $(LATEXOPT) $(MAIN)
