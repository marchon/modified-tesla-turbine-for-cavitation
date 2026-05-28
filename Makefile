.PHONY: diagrams docs docs-pdf latex clean

diagrams:
	python3 python/generate_diagrams.py

docs:
	cd docs && python3 -m sphinx -b html . _build/html

docs-pdf:
	cd docs && python3 build_pdf.py
	@echo ""
	@echo "✅ Professional Sphinx documentation PDF ready:"
	@echo "   docs/_build/sphinx_documentation.pdf"
	@echo "   (titlepage + full TOC + all sections + cross-reference index at back)"

latex:
	cd latex && pdflatex -interaction=nonstopmode main.tex && pdflatex -interaction=nonstopmode main.tex
	@echo "PDF: latex/main.pdf"

clean:
	rm -rf docs/_build latex/*.aux latex/*.log latex/*.out latex/*.toc diagrams/*.png diagrams/*.svg
