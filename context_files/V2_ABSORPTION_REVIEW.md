# V2 Absorption Review

## Correct old baseline

The real earlier completed draft is:

- `E:\canfiles\Common courses study\大学通识\25-26 Spring\UFUG 2104 Applied statistics\HM1_project_report_v2\report.pdf`
- `E:\canfiles\Common courses study\大学通识\25-26 Spring\UFUG 2104 Applied statistics\HM1_project_report_v2\report.tex`
- `E:\canfiles\Common courses study\大学通识\25-26 Spring\UFUG 2104 Applied statistics\HM1_project_report_v2\code\formal\project_notebook.ipynb`

Verified page/cell structure:

- Old `report.pdf`: 169 pages.
- Old `project_notebook.pdf`: 153 pages.
- Old notebook: 170 cells, 74 code cells, 131 outputs.
- Current rebuilt `project_report.pdf`: 110 pages.
- Current `supplemental_code.executed.pdf`: 78 pages.
- Current executed notebook: 71 cells, 42 code cells, 106 outputs.
- Current executed notebook QA scan: 0 unexecuted code cells, 0 error outputs, and 0 occurrences of `FigureCanvasAgg`, `UserWarning`, `FutureWarning`, `RuntimeWarning`, `Traceback`, or `Error` in captured outputs.

## What V2 did better

The V2 notebook was stronger as a full reasoning trail. It did not only show final statistics; it documented how the team thought through the dataset before modeling:

- Raw CSV fingerprint and schema freeze.
- The fact that `personName` is not a stable primary key.
- Snapshot-level surrogate-key logic using `(rank, country, personName)`.
- Exact alias relationship between `category` and `industries`.
- `date` as snapshot metadata, not a time-series variable.
- Variable-layer reasoning: core variables, time variables, geography, macro variables, labels, and metadata.
- Drop/keep policy for columns with weak interpretability or high missingness.
- Macro-variable framing as scale, development, and institution/cost environment.
- Reviewer-defense notes explaining why these choices are not arbitrary.

## What has now been absorbed into the current version

Added to `supplemental_code.ipynb`:

- A `V2 Draft Absorption Layer` explaining what was preserved from the earlier full notebook.
- Raw-data fingerprint and record-identity audit.
- Generated artifacts:
  - `output/tab/tab_M1_raw_fingerprint.csv/.tex`
  - `output/tab/tab_M1_identity_audit.csv/.tex`
  - `output/tab/tab_M1_variable_reasoning_matrix.csv/.tex`
- Variable reasoning matrix covering outcome, time/life-cycle, geography, business category, identity/social labels, scale macro variables, development macro variables, and institution/cost variables.
- Cleaning/drop/keep defense notes.
- Macro-variable interpretation guardrail: scale vs development vs institution.
- RQ/module mini-summaries after each major analysis block, so the appendix reads as a reproducible statistical dossier rather than only a code listing.
- V2-to-current integration matrix documenting exactly which V2 strengths were retained and where they appear.
- V2 topic-reasoning archive documenting which old exploratory ideas were kept, strengthened, caveated, or not carried forward.
- Old V2 research-question coverage table mapping RQ0-RQ7 to the current report and appendix structure.
- Restored geography drill-down that is defensible from the available data: country concentration, country/citizenship mismatch, U.S. state profile, U.S. region profile, and China city profile.
- Notebook rendering fix: the old `FigureCanvasAgg is non-interactive` warning path was removed by displaying figures explicitly in notebook output and closing them after save; stale outputs were cleared and the notebook was re-executed in WSL.

Added to `project_report.tex`:

- A new paragraph in the data-governance section explicitly acknowledging and preserving the V2 pre-analysis audit.
- A new record identity and alias audit table in the main report.
- Expanded feature-engineering discussion to include `log_pop`, `gdp_pc`, and `log_gdp_pc`.
- A clearer macro-variable interpretation paragraph warning against over-interpreting GDP as development or causality.
- Updated notebook module map to mention the V2 absorption layer.
- Added a V2 Integration Audit section with a landscape integration matrix table.
- Added a landscape old-V2-versus-current-RQ coverage table.
- Added a restored geography paragraph and figure for U.S. state and China city profiles, with explicit caveats that these are descriptive record-count views rather than causal geography or policy effects.

## What was intentionally not copied verbatim

The old notebook contained many long exploratory sections and informal bilingual notes. These were not pasted wholesale because the current report already has stronger formal statistical analysis: bootstrap/BCa, Holm-type multiple testing control, VIF, nested F-test, grouped CV, quantile regression, and robustness matrices.

The current direction is therefore:

- Keep V2's comprehensive reasoning and audit trail.
- Keep the current report's stronger statistical framework.
- Avoid turning the appendix into repeated exploratory scratch work unless a section adds a new audit, figure, table, or defense point.

## Items from the earlier "remaining upgrades" list that have now been completed

- Expanded notebook markdown into RQ/module mini-summaries and defense notes.
- Restored selected geography storytelling from V2, especially U.S. state and China city discussion, while adding explicit anti-overclaiming caveats.
- Added a dedicated table comparing old V2 research-question coverage against the current integrated report structure.
- Added more narrative explanations around key notebook outputs so the appendix reads as a reproducible statistical dossier rather than only a code dump.

## Honest remaining boundary

Within the existing dataset, the current version now combines V2's strongest comprehensive reasoning trail with the newer report's stronger statistical framework. The remaining ceiling is not more computation on the same columns; it is external validation. Stronger causal or institutional claims would require outside evidence or a different dataset, because this Forbes snapshot is observational, cross-sectional, and partly label-driven.

Final PDF QA on 2026-05-01:

- `project_report.pdf`: 110 pages, built successfully with `latexmk`.
- `supplemental_code.executed.pdf`: 78 pages, generated from the WSL-executed notebook HTML.
- LaTeX log scan: no `Overfull`, no undefined references, no undefined citations, no fatal errors.
- Visual spot-check: identity audit page, geography page, V2 integration tables, V2 RQ coverage table, and appendix start page stayed within page bounds.
