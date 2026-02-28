# Context for AI

This is an explanation of our project to make AI better understand what we are doing.

## File content tree (update by the task going)

```output
📁 HW1_project_report
├── 📁 code
│   ├── 🔧 color_setting.json
│   │   - Purpose: Global plot palette & style tokens for all figures (consistency + “fancy”).
│   │   - Used in: notebook (loaded in M0 / plotting helpers). Not included in report, but ensures consistent visuals.
│   └── 📓 project_stastistic_analyse_and_visualization.ipynb
│       - Purpose: The ONE canonical executable notebook (M0→M9). Produces all tables/figures + cleaned dataset.
│       - Used in: Appendix “Notebook appended” (deliverable requirement). Also the source of all report figures/tables.
│
├── 📁 data
│   ├── 📁 clean
│   │   ├── 📋 billionaires_clean.csv
│   │   │   - Purpose: Clean dataset exported by M3 (audit-friendly, portable).
│   │   │   - Used in: Not directly pasted in report; referenced in “Data Processing” as the cleaned artifact.
│   │   └── 📄 billionaires_clean.parquet
│   │       - Purpose: Same as CSV but faster for code; optional.
│   │       - Used in: Notebook reruns; not pasted in report.
│   └── 📁 raw
│       └── 📋 Billionaires Statistics Dataset.csv
│           - Purpose: Professor-provided raw data (must not be modified).
│           - Used in: Notebook M1 ingestion; referenced in report “Dataset” subsection.
│
├── 📁 delivery_requirments_and_standard
│   └── 📖 official_requirement.md
│       - Purpose: Official rubric + required report structure.
│       - Used in: Writing the report outline (Introduction/Statistical Analysis/Key Insights/References/Notebook).
│
├── 📁 files_for_ai
│   ├── 🐍 content_tree.py
│   │   - Purpose: Utility script to print the folder tree (maintenance only).
│   │   - Used in: Not used in report; for project housekeeping.
│   ├── 📖 context_for_ai.md
│   │   - Purpose: Alignment doc for AI (what files mean, where artifacts live).
│   │   - Used in: Not part of submission; internal coordination.
│   ├── 📖 variable_registery.md
│   │   - Purpose: Human-written variable dictionary + schema freeze notes (semantics, units, caveats).
│   │   - Used in report: “Data & Variables” (cite key variable definitions: finalWorth, gdp_country, status, country fields).
│   └── 📖 workbook.md
│       - Purpose: Workflow spec (M0→M9 standards, artifact expectations, takeaways rules).
│       - Used in: Internal execution; not submitted.
│
├── 📁 output
│   ├── 📁 fig
│   │   - Purpose: All figures saved as both PDF (report) and PNG (quick preview).
│   │   - Used in report: Include PDFs via \includegraphics{output/fig/<name>.pdf}.
│   │
│   │   ├── fig_M0_variable_role_counts.{pdf,png}
│   │   │   - What: Variable role counts (P0/P1/Meta) to justify analysis scope.
│   │   │   - Place: Introduction / Data Overview (optional but good for transparency).
│   │   ├── fig_M1_dtype_distribution.{pdf,png}
│   │   │   - What: Data type distribution (schema sanity check).
│   │   │   - Place: Data Processing (short).
│   │   ├── fig_M2_missingness_top15.{pdf,png}
│   │   │   - What: Top missingness columns.
│   │   │   - Place: Data Processing & EDA (DQ audit subsection).
│   │   ├── fig_M2_missingness_heatmap_country_top12.{pdf,png}
│   │   │   - What: Missingness structure by country (top 12).
│   │   │   - Place: Data Processing & EDA (DQ audit; supports “missing not at random” discussion).
│   │   ├── fig_M2_us_only_state_coverage.{pdf,png}
│   │   │   - What: Structural missingness: state/region only for US records.
│   │   │   - Place: Data Processing & EDA (important governance insight).
│   │   ├── fig_M2_outliers_raw_vs_log_box.{pdf,png}
│   │   │   - What: Heavy-tail evidence; motivates log transform and robust methods.
│   │   │   - Place: Descriptive stats / Method notes (before regression).
│   │   ├── fig_M3_validation_log_distributions.{pdf,png}
│   │   │   - What: Post-cleaning validation (log distributions sanity check).
│   │   │   - Place: Data Processing (end, 1 figure enough).
│   │   ├── fig_M4_finalWorth_distribution_raw_and_log.{pdf,png}
│   │   │   - What: Univariate distribution (raw vs log).
│   │   │   - Place: Statistical Analysis → Descriptive.
│   │   ├── fig_M4_finalWorth_ccdf_loglog.{pdf,png}
│   │   │   - What: CCDF log-log showing heavy tail / concentration.
│   │   │   - Place: Descriptive + Key Insight (wealth concentration).
│   │   ├── fig_M4_top10_country_count.{pdf,png}
│   │   │   - What: Top countries by billionaire count.
│   │   │   - Place: Descriptive (geo pattern).
│   │   ├── fig_M4_top10_category_count.{pdf,png}
│   │   │   - What: Top categories by count.
│   │   │   - Place: Descriptive (industry pattern).
│   │   ├── fig_M4_top1pct_wealth_share.{pdf,png}
│   │   │   - What: Wealth share of top 1%.
│   │   │   - Place: Key Insights #1 (concentration) + limitation notes.
│   │   ├── fig_M4_correlation_heatmap.{pdf,png}
│   │   │   - What: Numeric correlation overview (screening).
│   │   │   - Place: EDA / transition into inferential/regression (optional).
│   │   ├── fig_M5_scatter_finalWorth_vs_gdp_raw.{pdf,png}
│   │   │   - What: Raw scale relationship (often dominated by outliers).
│   │   │   - Place: EDA (to motivate log model).
│   │   ├── fig_M5_scatter_logWorth_vs_logGDP.{pdf,png}
│   │   │   - What: Main EDA plot for the core relationship (log-log).
│   │   │   - Place: Inferential/Regression lead-in.
│   │   ├── fig_M5_scatter_logWorth_vs_logGDP_by_selfMade.{pdf,png}
│   │   │   - What: Stratified EDA to address Simpson’s paradox risk.
│   │   │   - Place: Robustness/limitations (great for “not just one scatter”).
│   │   ├── fig_M5_box_logWorth_by_selfMade.{pdf,png}
│   │   │   - What: Group comparison (self-made vs inherited proxy).
│   │   │   - Place: Inferential analysis.
│   │   ├── fig_M5_box_logWorth_by_gender.{pdf,png}
│   │   │   - What: Gender comparison (descriptive/inferential).
│   │   │   - Place: Descriptive or inferential (pick one; don’t overstuff).
│   │   ├── fig_M5_corr_heatmap_spearman.{pdf,png}
│   │   │   - What: Spearman correlation matrix (robust to outliers).
│   │   │   - Place: Inferential/robustness notes.
│   │   ├── fig_M6_effectsize_forest.{pdf,png}
│   │   │   - What: Headline effect sizes + CI (correlation + group diffs).
│   │   │   - Place: Inferential (the “effect size + CI” scoring point).
│   │   ├── fig_M7_regression_fit_loglog.{pdf,png}
│   │   │   - What: Regression fitted line on log-log scale.
│   │   │   - Place: Regression section (main model).
│   │   ├── fig_M7_regression_diagnostics.{pdf,png}
│   │   │   - What: Residual vs fitted + QQ plot (model checking).
│   │   │   - Place: Regression → Diagnostics (1 figure is enough).
│   │   └── fig_M7_robust_coef_compare_top1pct.{pdf,png}
│   │       - What: Robustness—coefficient stability after dropping top 1%.
│   │       - Place: Regression → Robustness (required by your rule).
│   │
│   └── 📁 tab
│       - Purpose: All tables saved as CSV (audit) + TEX (directly \input into report).
│       - Used in report: \input{output/tab/<name>.tex} (with caption/label wrapper).
│
│       ├── schema_freeze_A.json
│       │   - What: Schema freeze artifact (hash, columns, NA policy).
│       │   - Place: Not pasted in report; referenced in Data Processing (1 sentence).
│       ├── tab_M0_environment_snapshot.{csv,tex}
│       │   - What: Reproducibility snapshot (python/pandas versions).
│       │   - Place: Appendix or Data Processing footnote (optional).
│       ├── tab_M0_research_questions.{csv,tex}
│       │   - What: Final English RQs table.
│       │   - Place: Introduction (must-have).
│       ├── tab_M0_research_questions_source.{csv,tex}
│       │   - What: Source RQs extracted from workbook (audit trail).
│       │   - Place: Not in report (internal).
│       ├── tab_M0_schema_freeze_A_summary.{csv,tex}
│       │   - What: Human-readable freeze summary table.
│       │   - Place: Data Processing (short).
│       ├── tab_M0_variable_roles.{csv,tex}
│       │   - What: Role assignment (P0/P1/Meta).
│       │   - Place: Data & Variables (optional).
│       ├── tab_M1_dictionary_verification_checks.{csv,tex}
│       │   - What: Verified facts (e.g., category==industries, US-only state).
│       │   - Place: Data Processing (supports “governance insight”).
│       ├── tab_M1_gdp_parse_summary.{csv,tex}
│       │   - What: GDP string→numeric parse coverage.
│       │   - Place: Data Processing (1 table ok).
│       ├── tab_M1_schema_summary.{csv,tex}
│       │   - What: Column dtype/missing summary.
│       │   - Place: Data Processing appendix (optional).
│       ├── tab_M2_artifact_index.{csv,tex}
│       │   - What: Artifact registry (auto index).
│       │   - Place: Not in report; internal.
│       ├── tab_M2_dq_issues_summary.{csv,tex}
│       │   - What: DQ issues list (missingness/outliers flags).
│       │   - Place: Data Processing (optional; cite 2–3 key issues only).
│       ├── tab_M2_missingness_by_country_top12.{csv,tex}
│       │   - What: Missingness rates per country (top 12).
│       │   - Place: Data Processing (supporting table; optional if heatmap shown).
│       ├── tab_M2_missingness_top15.{csv,tex}
│       │   - What: Missingness ranking table (top 15).
│       │   - Place: Data Processing (optional if you include fig_top15).
│       ├── tab_M2_us_only_state_coverage.{csv,tex}
│       │   - What: US-only structural coverage table.
│       │   - Place: Data Processing (recommended—short and strong).
│       ├── tab_M3_clean_dataset_manifest.{csv,tex}
│       │   - What: Clean dataset manifest (rows/cols/hash).
│       │   - Place: Data Processing (optional).
│       ├── tab_M3_cleaning_log.{csv,tex}
│       │   - What: Cleaning decisions log (audit).
│       │   - Place: Data Processing appendix (optional).
│       ├── tab_M4_finalWorth_describe.{csv,tex}
│       │   - What: Descriptive summary stats.
│       │   - Place: Descriptive section (must-have).
│       ├── tab_M4_top10_country_by_count.{csv,tex}
│       │   - What: Top countries by count (table form).
│       │   - Place: Descriptive (optional if bar chart used).
│       ├── tab_M4_top10_category_by_count.{csv,tex}
│       │   - What: Top categories by count.
│       │   - Place: Descriptive (optional if bar chart used).
│       ├── tab_M4_top1pct_wealth_share.{csv,tex}
│       │   - What: Top 1% share numeric values.
│       │   - Place: Key Insights (supports the claim).
│       ├── tab_M4_correlation_matrix.{csv,tex}
│       │   - What: Numeric correlation matrix.
│       │   - Place: EDA appendix (optional).
│       ├── tab_M5_corr_matrix_spearman.{csv,tex}
│       │   - What: Spearman matrix (robust).
│       │   - Place: Inferential/robustness appendix (optional).
│       ├── tab_M5_groupwise_correlations.{csv,tex}
│       │   - What: Stratified correlations (e.g., by selfMade).
│       │   - Place: Robustness (recommended—supports “not Simpson”).
│       ├── tab_M6_inferential_results.{csv,tex}
│       │   - What: All inferential results (effect sizes + CI + p).
│       │   - Place: Inferential section (use as primary table; summarize key rows in text).
│       ├── tab_M6_posthoc_category_pairwise.{csv,tex}
│       │   - What: Post-hoc comparisons (BH-FDR).
│       │   - Place: Optional appendix (too long for main).
│       ├── tab_M7_regression_main.{csv,tex}
│       │   - What: Regression coefficients with HC3 SE + CI.
│       │   - Place: Regression section (must-have).
│       ├── tab_M7_bp_test_modelB.{csv,tex}
│       │   - What: BP heteroskedasticity test.
│       │   - Place: Regression diagnostics (optional if you already discuss HC3).
│       ├── tab_M7_robust_drop_top1pct_logmodel.{csv,tex}
│       │   - What: Robustness coefficients table (top-1% exclusion).
│       │   - Place: Regression robustness (recommended).
│       ├── tab_M8_robustness_matrix.{csv,tex}
│       │   - What: Robustness matrix for key claims.
│       │   - Place: Key Insights or Appendix (nice “extra credit” feel).
│       ├── tab_M9_report_map.{csv,tex}
│       │   - What: Mapping report section ↔ figures/tables ↔ notebook module.
│       │   - Place: Not in report; internal (but great for writing).
│       └── tab_M9_runbook.{csv,tex}
│           - What: Reproducibility steps checklist.
│           - Place: Appendix (optional) or internal.
│
├── 📄 project_report.tex
│   - Purpose: The final written report (LaTeX source).
│   - Must include: Introduction (RQs) / Statistical Analysis (Desc+Infer+Reg) / Key Insights / References / Notebook appended.
│
├── 📄 project_report.pdf
│   - Purpose: The submission file (compiled from .tex).
│
├── 📄 project_report.{aux,log,out,synctex.gz}
│   - Purpose: LaTeX build artifacts (not needed for submission; keep for debugging only).
```

### File usage explanation

1. `./code/project_stastistic_analyse_and_visualization.ipynb`: we need to write all our codes in this file. You need to make every cell of code clear, powerful, interperable(reader-friendly), reusable, and executable. （有解释更好！）

2. `./data/raw/Billionaires Statistics Dataset.csv`: This file is the raw data provided by our professor.
`./data/clean`: if needed, this dir is used to contain the cleaned data, if not necessary, we can just leave it here to make the dir `./data` complete
3. `./delivery_requirments_and_standard/official_requirement.md`: This is the official guiding file from our professor telling us the requirement of this task overall.
4. `./files_for_ai/content_tree.py`: This is just a file used for myself to update the file tree with every option, you don't need to care too much about it.
`./files_for_ai/context_for_ai.md`: This is a file to achieve an alignment with the AI tool to let him know what I am doing and what does my file structure takes on the contents, so on and so forth.
`./files_for_ai/workbook.md`: This file is a workbook for us to maximize and optimize the quality of the workflow provided by AI and the final outcome of our report.
`./files_for_ai/variable_registery.md`: This records the initail variables we set according to the raw data `./data/raw/Billionaires Statistics Dataset.csv`.
5. `./project_report.*`: This is the files for me to write the report and with its derived files makes the report in the format of PDF.
6. `./output/fig/`, `./output/tab/`: If we have generated any figure or tabular, please put them in these 2 dir respectively.

## Overall Settings to AI

```Markdown
## Your role:
Now please act as a patient scholar and professor excel in the Applied Statistics helping me with the project and report with optimized operation and overall and high-level view of Applied statistic and its project. 

## My role:
A student running a project about the study of the Billionare data set from scratch,  based on the `official_requirement.md` as the overall object of our project and the `workbook.md`, `workbook.md` and `variable_registery.md` as instructions, `Billionaires Statistics Dataset.csv` is the raw data. We want to optimize the outcome

## File declaration (uploaded in this conversation):

### File set 1
- `official_requirment.md`
- `Billionaires Statistics Dataset.csv`

### File set 2
- `variable_registery.md`
- `context_for_ai.md`
- `workbook.md`
- `project_stastistic_analyse_and_visualization.ipynb` (Just a frame)


You can refer to the `context_for_ai.md` to get to know the usage of each files we have already have.

## Core task
Follow the `workbook.md` to finish the work step by step.
```
