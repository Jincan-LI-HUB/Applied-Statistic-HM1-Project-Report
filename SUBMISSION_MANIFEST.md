# Submission Manifest

## Primary Files

- `report.pdf`: final compiled report with rendered notebook appendix. This is the canonical version to submit.
- `report.tex`: LaTeX source for the final report.
- `code/formal/project_notebook.ipynb`: executable notebook source.
- `code/formal/project_notebook.executed.ipynb`: executed notebook generated in WSL.
- `code/formal/project_notebook.executed.html`: HTML render of the executed notebook.
- `project_notebook.pdf`: PDF render of the executed notebook included in `report.pdf`.
- `RUNBOOK.md`: rebuild and QA instructions.

## Reproducibility Notes

- The notebook and helper scripts locate the project root dynamically.
- The final M6 inferential table is generated from notebook-computed CSV output, then supplemented with computed gender tests; it no longer uses hard-coded Pearson/Spearman/Welch/Kruskal-Wallis rows in helper scripts.
- The official requirement is copied into both `delivery_requirment/` and `delivery_requirments_and_standard/` for compatibility with the earlier folder conventions and notebook root detection.

## Last QA Results

- `report.pdf`: 113 pages.
- `project_notebook.pdf`: 79 pages.
- Executed notebook scan: 71 cells, 106 outputs, 28 image outputs, 0 scanned execution issues.
- LaTeX log scan: no overfull boxes, underfull boxes, undefined references, undefined citations, fatal errors, or content-breaking warnings. The only remaining warning is the package-level `microtype` footnote patch warning.
- HTML export warning: 28 images lack alt text. This is an nbconvert accessibility warning, not a code execution warning.
- Visual spot check retained for the final Table 7 layout: `code/test/qa_report_table7_final.png`.
