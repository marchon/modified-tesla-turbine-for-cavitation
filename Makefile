.PHONY: diagrams docs latex clean

diagrams:
	python3 python/generate_diagrams.py

docs:
	cd docs && python3 -m sphinx -b html . _build/html

latex:
	cd latex && pdflatex -interaction=nonstopmode main.tex && pdflatex -interaction=nonstopmode main.tex
	@echo "PDF: latex/main.pdf"

clean:
	rm -rf docs/_build latex/*.aux latex/*.log latex/*.out latex/*.toc diagrams/*.png diagrams/*.svg
