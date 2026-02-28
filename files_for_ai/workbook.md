# 0. 项目合同（Project Contract）✅

## 文件与职责分工（不可变）

* **唯一代码入口**：`./code/project_stastistic_analyse_and_visualization.ipynb`（所有代码都写这里）
* **原始数据**：`./data/raw/Billionaires Statistics Dataset.csv` 
* **可选清洗输出目录**：`./data/clean/`（需要的话存 cleaned 数据）
* **报告**：`project_report.tex` 编译 PDF；并把 **Notebook 附到报告末尾**（交付要求）
* tips: 更加详细的文件说明见`./files_for_ai/workbook.md`

## 报告结构与评分强制对齐（不可变）(refer to `./delivery_requirements_and_standard/official_requirement.md` for detailed information)

* Introduction 10%：数据概览 + 目标 + **要回答的问题（RQ）** 
* Statistical Analysis 45%：必须包含 **Descriptive + Inferential（相关/检验）+ Regression（简单线性回归至少一条）** 
* Key Insights & Conclusions 15%：≥3 条 takeaway + 现实联系 + limitations 
* Notebook 30%：代码清晰、可复现、支撑报告
* Extra credit（最多 +10）：advanced methods 或独特洞察 (也很重要！！！) 

---

# 1. 最终版 RQ（保留你的认可版本，做“落地强化”）🎯

> 这些 RQ 的设计已经**强制覆盖**课程要求的 3 类统计技术（descriptive / inferential / regression）。

## RQ0（数据可信度地基）

**RQ0：数据质量（缺失/异常/重复）是否会系统性偏向某些国家/行业，从而影响推断？**

* 输出：缺失分布（总体+分组）、异常规则、清洗影响日志
* 目的：为后续所有结论加“可信度底座”（G3 的灵魂）

## RQ1（Descriptive 主线：重尾与集中度）

**RQ1：`finalWorth` 的分布是否重尾？top 1% 对整体统计量（均值/方差/相关/回归）的支配性有多强？**

* 输出：原尺度 vs log 尺度分布、分位数表、top1% 贡献率

## RQ2（Inferential 主线：群体差异）

**RQ2：`selfMade`、`gender`、`industry/category` 与 `finalWorth` 是否存在显著差异？差异的效应量与不确定性（CI）是多少？**

* 输出：Welch/Mann–Whitney、Kruskal–Wallis、bootstrap CI、effect size

## RQ3（Inferential + 机制视角：宏观变量相关结构）

**RQ3：`finalWorth` 与国家宏观变量（如 `gdp_country` 等）是否相关？在 log 变换、分层（按 industry 等）后是否一致？**

* 输出：Pearson + Spearman、分层相关、稳健性对比

## RQ4（Regression 主线：预测/解释）

**RQ4：用 `gdp_country` 预测 `finalWorth` 的简单线性回归表现如何？在 log 版本、多元回归、稳健标准误、敏感性设定下结果是否稳定？**

* 强制覆盖 requirement 示例：`finalWorth ~ gdp_country` 

备选加分（可选，不影响主线）

**RQ5：Quantile regression（GDP 对不同分位富豪的影响是否不同）→ Extra credit 很友好**

**RQ6：Permutation test / Bootstrap-based inference（更少分布假设）**

---

# 2. 三条硬规则（DoD：Definition of Done）✅

从现在起，任何模块不过这三条就算没完成：

1. **每模块 ≥1 张图/表 + 1 句 takeaway**（写在 notebook markdown）
2. **每个推断/回归结论必须有 effect size + CI**（p 值只能辅助）
3. **每条关键结论至少做 1 个稳健性检验**（transform / outlier / missingness / stratification 四选一）

---

# 3. 研究级（G3）Notebook 结构模板（直接照抄为 Markdown cell 标题）🧱

在 `./code/project_stastistic_analyse_and_visualization.ipynb` 里按以下顺序建 Markdown 分节（强烈建议保持一致，保证 notebook 与报告 1:1 对齐）：

0. **Project Contract & RQ**
1. **Data Ingestion & Variable Register (Schema Freeze)**
2. **Data Quality Audit (Missingness / Outliers / Duplicates)**
3. **Cleaning & Feature Engineering (df_clean)**
4. **Descriptive Analysis (Univariate)**
5. **EDA (Bivariate / Stratified / Multivariate)**
6. **Inferential Statistics (Tests + Effect Size + CI)**
7. **Regression (Simple + Multiple + Diagnostics + Robust SE)**
8. **Robustness & Sensitivity (for every key claim)**
9. **Report Map & Reproducibility (Figure/Table index + Runbook)**

> 这套结构会自动满足 requirement 对报告结构/统计分析类型/可复现性的要求。

---

# 4. 最终版 G3 执行 WorkBook（模块级清单：写什么代码 / 出什么图表 / 做什么自检）

下面每个模块都按统一口径：**Goal / Code blocks / Outputs / Checks / Report mapping**。
（“Code blocks”我会给你建议函数清单与关键调用点——下一个 AI 可以直接按此填充具体实现。）

---

## G3-M0：Project Contract & RQ（冻结口径）
**Notebook section**：`0. Project Contract (RQ + Variables)`
**Goal**：把 RQ 与变量口径冻结，避免后面分析漂移。
**Report mapping**：Introduction（Objectives + Questions）

### Code blocks（建议）

* `print_env()`：打印 Python/库版本（可复现）
* `load_data_preview()`：读入后快速 `shape/head/info/describe`
* `build_variable_register(df)`：自动生成变量注册表（dtype/missing/unique/top levels）

### Outputs（至少）

* `tab_variable_register`：列名、类型、含义（初版可先写“待补充”）
* takeaway：本项目 Y/X/Group 变量、变换策略（log1p 等）

### Checks

* **Checkpoint A（强制）**：完成 register 后冻结列名与转换；之后变更必须写 Change Log。

---

## G3-M1：Data Ingestion & Dictionary（读入与字典）
**notebook section**: `1. Data Ingestion & Dictionary`
**Goal**：读对类型、识别缺失编码，为后续推断打基础。
**Report mapping**：Introduction（dataset overview）

### Code blocks（建议）

```python
# 读入
df_raw = pd.read_csv(PATH, encoding="utf-8", na_values=["", "N/A", "None", "?"])

# 基本检查
df_raw.shape, df_raw.head(), df_raw.info()

# schema summary
schema = make_schema_summary(df_raw)  # dtype, missing%, nunique
```

### Outputs

* `tab_schema_summary`（dtype + missing%）
* figure:`fig_missingness_overall`（缺失率条形图,给出（注释的）代码和操作说明即可）

### Checks

* 核心列（至少 `finalWorth`, `gdp_country`）是否为 numeric；如果不是，先纠正（否则后面 regression 会炸）。
- 每个图表有标题/轴标签/单位
- 输出与Register一致

---

## G3-M2：Data Quality Audit（缺失/异常/重复）
**Notebook section**: `2. Data Quality Audit`
**Goal**：回答 RQ0（数据是否偏），并形成清洗策略证据链。
**Report mapping**：Statistical Analysis（Data Quality 子段）

### Code blocks（建议）

* `missing_profile(df, group_col=None)`：总体缺失；按 country/industry/selfMade 分层缺失
* `range_checks(df)`：`年龄范围`、`finalWorth 非负`等规则
* `duplicate_checks(df, keys=[...])`：若有 name/ID 列，用组合键检查

### Outputs

* `tab_dq_issues`：issue/evidence/action
* `fig_missing_by_group_country`（top-10 country 的缺失对比）
* `fig_outlier_box_finalWorth`（原+log）

### Checks（论敌点）

* 若缺失集中在特定国家/行业：后面推断必须做“complete-case vs alternative”稳健性对照（硬规则 #3）。
* 记录“删/填补”的数量与具体操作。
---

## G3-M3：Cleaning & Feature Engineering（产出 df_clean）
**Notebook section**: 3. Cleaning & Feature Engineering
**Goal**：形成可复现的 `df_clean` 与清洗日志。
**Report mapping**：Statistical Analysis（Cleaning 说明）

### Code blocks（建议）

* `clean_numeric_columns(df, cols)`：强转数值
* `clean_category_columns(df, cols)`：strip/lower/replace
* `add_features(df)`：`log_finalWorth = log1p(finalWorth)`, `log_gdp = log1p(gdp_country)` 等

### Outputs (以代码形式给出，我们来跑)

* `df_clean`（可选保存到 `./data/clean/`）
* `tab_cleaning_log`（删了多少行、改了哪些列、缺失处理策略）
* `fig_raw_vs_clean_dist_finalWorth`（对比图）

### Checks

* 清洗前后 p50/p90/p99 是否发生“不可解释的大变化”；若变化大，记录原因并在 limitations 说明（这反而更研究级）。

---

## G3-M4：Descriptive Analysis（单变量：重尾与集中度）
**Notebook section**: `4.Descriptive Analysis`
**Goal**：完成 RQ1 的 descriptive 主证据。
**Report mapping**：Statistical Analysis（Descriptive）

### Code blocks（建议）

* `quantile_table(df, col, qs=[.5,.75,.9,.95,.99])`
* `plot_hist_and_kde(df, col, log=False)`
* `plot_ccdf(df, col)`（重尾更清晰，Bonus）
* `topk_bar(df, col, k=10)`

### Outputs（至少，鼓励更多有价值的产出）
记得要带上对这个的takeaways, 尽善尽美。
* `fig_dist_finalWorth_raw`
* `fig_dist_finalWorth_log`
* `tab_quantiles_finalWorth`
* `fig_topk_country`, `fig_topk_industry`

### Checks

* 重尾数据：**所有关键关系（相关/回归）都必须至少给一个 log 版本**（论敌#1）。
* 标注单位（finalWorth 单位若不明确，至少写“dataset unit”并避免绝对解释）

---

## G3-M5：EDA（双变量/分层/多变量）

**Goal**：为 inferential 与 regression “选战场”，并提前识别 Simpson 风险。
**Report mapping**：Statistical Analysis（承上启下）

### Code blocks（建议）

* `plot_scatter(df, x, y, logx=False, logy=False, hue=None)`
* `plot_group_box(df, y, group)`
* `corr_heatmap(df, cols, method="spearman")`

### Outputs

* `fig_scatter_finalWorth_vs_gdp_raw`
* `fig_scatter_logWorth_vs_logGDP`
* `fig_box_logWorth_by_selfMade`, `fig_box_logWorth_by_gender`
* `fig_corr_heatmap_spearman`

### Checks

* 必做一次分层：例如按 `selfMade` 或 `industry` 上色/分面，看总体相关与分组相关是否一致（论敌#3/Simpson）。

---

## G3-M6：Inferential（检验 + 效应量 + CI）
**Notebook section**: `6. Inferential Statistics`
**Goal**：满足 requirement 的 inferential（相关 + 假设检验），并做到研究级。
**Report mapping**：Statistical Analysis（Inferential）

### 必做内容（P0）

1. **Correlation**

* Pearson（线性）+ Spearman（重尾稳健）
* 至少对：`(log_)finalWorth` vs `gdp_country`（requirement 示例）
* Bootstrap CI for correlation（G3 强化）

2. **Hypothesis testing（至少 2 个）**

* 两组：selfMade vs not（log_finalWorth）

  * Welch t-test（方差不齐更稳）+ effect size（Cohen’s d 或 Cliff’s delta）+ bootstrap CI
* 多组：industry/category（Kruskal–Wallis）+（可选）post-hoc（控制多重比较）

3. **Multiple testing control（当你做很多行业比较时）**

* FDR（Benjamini–Hochberg）

### Outputs（硬规则 #2）

* `tab_inferential_results`（test / effect size / CI / p / interpretation）
* `fig_effectsize_forest`（误差条图，非常加分）
* takeaway：每个检验 “统计结论 + 实质意义”（不要只说显著）

### Checks（硬规则 #3）

* 至少对一个关键差异做 **permutation test** 作为稳健对照（Bonus，Extra credit 友好）
* 去掉 tpop 1% 后重复一次关键检验
* 注意尺度是否一致（原/log）

---

## G3-M7：Regression（简单回归 + 诊断 + 稳健）
**Notebook section**: `7. Regression Modeling`
**Goal**：满足 regression 要求，并把“研究级诊断”做全。
**Report mapping**：Statistical Analysis（Regression）

### 必做模型（P0）

* OLS：`finalWorth ~ gdp_country`（完全对齐 requirement 示例）
* 同时做更合理版本：`log_finalWorth ~ log_gdp`（重尾常规处理）

### 建议加分项（Bonus）

* Multiple regression：加入 `age` / `selfMade` / `gender` / industry dummies（避免遗漏变量偏误的显著性夸大）
* Robust SE（HC3）
* 诊断：残差 vs 拟合、QQ plot、异方差检验（BP test）
* （可选, 建议）Quantile regression（RQ5，Extra credit 强）

### Outputs（硬规则 #2）

* `tab_regression_main`（coef/CI/p/R²）
* `fig_regression_fit`（scatter + line；建议用 log 版本）
* `fig_regression_diagnostics`（至少 1 张）

### Checks（论敌#4）

* 解释口径固定一句：**association ≠ causation**
* 稳健性：剔除 top 1% 后重跑，比较系数与 CI（硬规则 #3）

---

## G3-M8：Robustness & Sensitivity（每条关键结论必须闭环）

**Goal**：把硬规则 #3 落到纸面。
**Report mapping**：Key Insights & Conclusions（limitations + robustness）

### 稳健性菜单（每条 takeaway 至少选 1 个）

* **Notebook section**: `8. Roubostness & Sensitivity`
* **Transform robustness**：raw vs log
* **Outlier robustness**：all vs drop top 1% finalWorth
* **Missingness robustness**：complete-case vs alternative（如仅对某些分析用完整样本）
* **Stratification robustness**：按 industry/selfMade 分层重复关键结论

### Outputs

* `tab_robustness_matrix`：结论 × 稳健性设定（保持/改变 + 数值差异）
* takeaway：哪些结论非常稳，哪些依赖假设（这很“研究级”）

---

## G3-M9：Packaging（Report Map + Reproducibility）
**Notebook section**: `9. Report Map & Reproducibility`
**Goal**：拿满 Notebook 30%，并让报告写作“复制粘贴式顺滑”。
**Report mapping**：全篇 + Notebook append

### Code blocks（建议）

* `savefig("fig_xxx.pdf")`：统一保存（建议 pdf 便于 LaTeX）
* 自动生成 `report_map` 表：

  * Report section → Notebook section → Figure/Table IDs → 文件名
* notebook 末尾 Runbook：`Restart kernel → Run all` 的说明

### Outputs

* `tab_report_map`
* “How to reproduce” Markdown 段落

---

# 5. 统一命名规范（让下一个 AI 不会乱）

建议所有产出都带编号与模块前缀（便于报告引用）：

* Figures：`./output/fig/fig_M4_dist_finalWorth_log.pdf`
* Tables：`./output/tab/tab_M6_inferential_results.csv` `./output/tab/tab_M6_inferential_results.tex`(生成两种格式的，.csv版本适合于进行下一步的分析.tex版本便于在report中引用)
* 清洗数据（在数据分析的具体情境需要时可选）：`data/clean/billionaires_clean.parquet`

---

# 6. 两个冻结点（最终执行纪律）🧷

* **Freeze A（读入后）**：Variable Register + 缺失编码 + 变换策略（log1p）冻结
* **Freeze B（完成 M5 EDA 后）**：RQ 冻结；之后只做稳健性/诊断，不再改研究问题