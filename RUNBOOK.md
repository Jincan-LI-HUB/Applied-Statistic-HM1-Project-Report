# Final Project V3 Runbook

This folder is the final submission package for the UFUG 2104 Applied Statistics billionaire dataset project.

## Folder Roles

- `report.tex` / `report.pdf`: main written report source and compiled PDF.
- `code/formal/project_notebook.ipynb`: executable notebook and audit trail.
- `project_notebook.pdf`: rendered executed notebook appended to the report.
- `code/remedy_run.py` and `code/remedy_run_part2.py`: supplemental diagnostics called by the notebook. These scripts locate the project root dynamically and do not rely on the original `E:\hermes_assisted` path.
- `data/raw/`: immutable raw CSV.
- `data/clean/`: generated clean dataset.
- `output/fig/` and `output/tab/`: notebook-generated figures and tables consumed by the report.
- `delivery_requirment/`: official coursework requirement reference.
- `context_files/`: integration notes and prior-version absorption review.

## Rebuild Order

Run the notebook in WSL/Linux from the project root:

```bash
cd "/mnt/e/canfiles/Common courses study/大学通识/25-26 Spring/UFUG 2104 Applied statistics/final_project_v3"
source /tmp/hermes_report_venv/bin/activate
python -m nbconvert --to notebook --execute code/formal/project_notebook.ipynb \
  --output project_notebook.executed.ipynb \
  --output-dir code/formal \
  --ExecutePreprocessor.timeout=1200 \
  --ExecutePreprocessor.kernel_name=python3
python -m nbconvert --to html code/formal/project_notebook.executed.ipynb \
  --output project_notebook.executed.html \
  --output-dir code/formal
```

Render the executed notebook HTML to PDF:

```bash
python code/test/render_notebook_pdf.py
```

Compile the report on Windows from this folder:

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error report.tex
```

## QA Checks

Before submission, check:

- `report.pdf` exists and includes the rendered notebook appendix.
- `project_notebook.pdf` exists.
- LaTeX log has no overfull boxes, undefined references, undefined citations, or fatal errors.
- Executed notebook has no `Traceback`, `Error`, `FigureCanvasAgg`, `UserWarning`, `FutureWarning`, or `RuntimeWarning` outputs.
- `output/tab/tab_M6_inferential_results.tex` reports the Kruskal-Wallis row as `H = 39.16` in the main text and `epsilon-squared = 0.0089` in the effect-size table, with `n = 2615`.
