# Makefile for LaTeX document (Precision Flow Conditioner project)
# Usage:
#   make pdf          - Build the PDF (runs pdflatex + biber as needed)
#   make clean        - Remove auxiliary files
#   make cleanall     - Remove auxiliary files and the PDF

PDF = main.pdf
TEX = main.tex

# Use pdflatex + biber for bibliography
LATEX = pdflatex -interaction=nonstopmode
BIBER = biber

.PHONY: all pdf clean cleanall

all: pdf

pdf: $(PDF)

$(PDF): $(TEX) references.bib
	@echo "=== First LaTeX pass ==="
	$(LATEX) $(TEX)
	@echo "=== Running BibTeX for bibliography ==="
	bibtex main || true
	@echo "=== Second LaTeX pass ==="
	$(LATEX) $(TEX)
	@echo "=== Third LaTeX pass (for references) ==="
	$(LATEX) $(TEX)
	@echo "=== Done: $(PDF) ==="

clean:
	rm -f *.aux *.log *.out *.toc *.bbl *.blg *.bcf *.run.xml *.fdb_latexmk *.fls

cleanall: clean
	rm -f $(PDF)

# Quick one-pass build (useful during heavy editing)
quick:
	$(LATEX) $(TEX)
