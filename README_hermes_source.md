# Hermes-Assisted Report — Quality Summary

## What was produced

`project_report.tex` — A complete, high-quality LaTeX research report for the UFUG 2104 Applied Statistics Assignment 1 (Billionaires Statistics Dataset).

## Report structure (100 pts + up to 10 pts extra credit)

| Section | Weight | Content |
|---|---|---|
| Introduction | 10% | Dataset overview, objectives, RQ table |
| Statistical Analysis | 45% | Data quality, descriptive, inferential, regression, robustness |
| Key Insights & Conclusions | 15% | 4 takeaways + real-world connection + limitations |
| References | — | Dataset, Python stack |
| Jupyter Notebook | 30% | Executable notebook submitted with the report |

## Statistical methods covered

**Descriptive**
- Histograms (raw + log scale), CCDF log-log, box plots
- Quantile tables, concentration summary (top 1% wealth share)
- Composition charts (top-10 countries, categories)

**Inferential**
- Pearson + Spearman correlation with 95% bootstrap CI
- Welch t-test, Cohen's d, Cliff's δ (selfMade group)
- Kruskal–Wallis + post-hoc with Benjamini–Hochberg FDR
- Permutation test (robustness)

**Regression**
- Model A: raw scale OLS (baseline, not significant)
- Model B: log-log OLS with HC3 robust SE (primary, p=0.019)
- Model C: multivariate log-log + demographic/industry controls
- Breusch–Pagan heteroskedasticity test
- Top-1% exclusion robustness

**Advanced / Extra Credit**
- Bootstrap CI throughout (10,000 replicates)
- HC3 robust standard errors
- Permutation test for group comparison
- FDR-corrected post-hoc pairwise comparisons
- Robustness matrix consolidating 3 core claims × 4 settings

## Key findings

1. **Heavy tail**: top 1% hold ~18% of total wealth; arithmetic mean is 5× median → log scale required
2. **Wealth–GDP association**: positive but weak (ρ≈0.10), elasticity ≈0.023, becomes imprecise after top-1% exclusion → association only, NOT causation
3. **Self-made paradox**: self-made billionaires have lower median wealth than non-self-made in this dataset (d=−0.12)
4. **Industry heterogeneity**: Real Estate (ρ=0.29), Manufacturing (−0.15), Healthcare (−0.07) — wide dispersion across categories

## Robustness discipline

Every major claim is stress-tested:
- Log vs. raw scale
- All data vs. drop top 1%
- Overall vs. stratified by selfMade/category
- Complete-case vs. full sample

## Files in this folder

- `project_report.tex` — the main report (compile with `pdflatex` twice)
- `project_report.pdf` — compiled report
- `supplemental_code.ipynb` — executable WSL-tested notebook
- `supplemental_code.executed.ipynb` — executed notebook output from WSL validation
- `output/fig/` and `output/tab/` — local report artifacts
- `COMPILE_INSTRUCTIONS.txt` — how to build the PDF
- This README

## Required artifacts

All figures and tables referenced by the report are local:
```
output/fig/   ← all .pdf/.png figures
output/tab/   ← all .tex/.csv tables
```

The notebook that generates these artifacts:
```
supplemental_code.ipynb
```

## Compilation

```
cd E:\hermes_assisted
pdflatex project_report.tex   # first pass
pdflatex project_report.tex   # second pass (cross-references, TOC)
```

Requires: pdflatex (MiKTeX, TeX Live, or MacTeX). No additional packages beyond the standard ones already declared in the .tex preamble.
