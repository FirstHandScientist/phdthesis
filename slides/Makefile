LATEX=pdflatex
LATEXOPT=--shell-escape

#"nonstopmode" is very verbose. batchmode is not verbose
NONSTOP=--interaction=nonstopmode
#NONSTOP=--interaction=batchmode

LATEXMK=latexmk
LATEXMKOPT=-pdf
CONTINUOUS=-pvc
SLIDES=ppgm_slide

all: slide

slide: $(SLIDES).tex
	$(LATEXMK) $(LATEXMKOPT) $(CONTINUOUS) \
	-pdflatex="$(LATEX) $(LATEXOPT) $(NONSTOP) %O %S" $(SLIDES)

# run: slide
# 	xdg-open $(SLIDES).pdf
