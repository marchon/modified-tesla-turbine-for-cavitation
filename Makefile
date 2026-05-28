.PHONY: diagrams docs docs-pdf latex clean

diagrams:
	python3 python/generate_diagrams.py

docs:
	cd docs && python3 -m sphinx -b html . _build/html

docs-pdf:
	cd docs && python3 build_pdf.py
	mkdir -p pdfs
	cp docs/_build/sphinx_documentation.pdf "pdfs/Modified_Tesla_Turbine_for_Cavitation_-_Full_Documentation.pdf"
	@echo ""
	@echo "✅ Professional Sphinx documentation PDF ready:"
	@echo "   pdfs/Modified_Tesla_Turbine_for_Cavitation_-_Full_Documentation.pdf"
	@echo "   (titlepage + full TOC + all sections + cross-reference index at back)"

latex:
	cd latex && pdflatex -interaction=nonstopmode main.tex && pdflatex -interaction=nonstopmode main.tex
	mkdir -p pdfs
	cp latex/main.pdf "pdfs/Modified_Tesla_Turbine_for_Cavitation_-_Technical_Report.pdf"
	@echo ""
	@echo "✅ LaTeX Technical Report ready:"
	@echo "   pdfs/Modified_Tesla_Turbine_for_Cavitation_-_Technical_Report.pdf"

clean:
	rm -rf docs/_build latex/*.aux latex/*.log latex/*.out latex/*.toc diagrams/*.png diagrams/*.svg
