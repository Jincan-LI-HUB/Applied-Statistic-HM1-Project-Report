# Variable Register + Schema Freeze (Billionaires Statistics Dataset, 2023) 📌

> **Purpose / 目的**
> - **EN:** Lock down variable meanings, types, and transformations **before** analysis, so results stay comparable across EDA / tests / regression.
> - **ZH:** 在分析开始前冻结变量口径（含义/类型/变换），避免“分析到一半改口径”导致结论不可比。

---

## A. Schema Freeze (Freeze A) 🧊

**EN:** “Schema” = column list + order + data types + missing-value rules at the moment we ingest `df_raw`.  
**ZH:** “Schema”= 读入 `df_raw` 当下的列名/顺序/类型/缺失识别规则。

- **Freeze ID**: `SF-2026-02-26-A`
- **Frozen artifact**: raw CSV schema at ingest (before cleaning).
- **Raw file path (project)**: `./data/raw/Billionaires Statistics Dataset.csv`
- **Row × Col**: 2640 × 35
- **File fingerprint**: sha256 `af398e929329cc44166e04ab763243de50d0bf049974a0b8c2544ba2db21760e`, md5 `af5e42a6886edca9e0f83330e49ad294`
- **Ingest read settings** (recommended): `pd.read_csv(..., encoding='utf-8', na_values=['', 'N/A', 'None', '?'])`
- **Column order** (frozen): `rank`, `finalWorth`, `category`, `personName`, `age`, `country`, `city`, `source`, `industries`, `countryOfCitizenship`, `organization`, `selfMade`, `status`, `gender`, `birthDate`, `lastName`, `firstName`, `title`, `date`, `state`, `residenceStateRegion`, `birthYear`, `birthMonth`, `birthDay`, `cpi_country`, `cpi_change_country`, `gdp_country`, `gross_tertiary_education_enrollment`, `gross_primary_education_enrollment_country`, `life_expectancy_country`, `tax_revenue_country_country`, `total_tax_rate_country`, `population_country`, `latitude_country`, `longitude_country`

### A1. Frozen decisions (must follow) ✅
- **EN:** Do **not** rename/drop raw columns in-place. If you need a cleaner name, create a **derived** column (see Section C) and record it in Change Log.
- **ZH:** 不要直接对原始列做重命名/删除；需要更友好的名称就新建“派生列”，并写入变更日志。

- **EN:** Treat missing values as pandas `NaN` after ingest. (Currently no explicit tokens like `"N/A"` were observed, but we keep `na_values` for safety.)
- **ZH:** 缺失统一用 `NaN`；（目前未观察到显式 `"N/A"` 等 token，但仍保留 `na_values` 以防数据源更新。）

### A2. Uniqueness / Keys 🔑
- **EN:** There is **no single reliable primary key** (e.g., `personName` is not fully unique). Use a **surrogate key** when needed:
  - `uid_raw = (personName, rank, country, finalWorth)` (observed unique in this CSV snapshot).
- **ZH:** 数据中没有稳定的单列主键（例如 `personName` 有重复）。需要唯一标识时可用组合键：
  - `uid_raw = (personName, rank, country, finalWorth)`（在当前 CSV 快照中观察为唯一）。

---

## B. Variable Register (Data Dictionary) 🧾

### B0. Role map for this project (quick) 🎯
- **P0 (core variables / 核心变量)**: `finalWorth`, `gdp_country`, `selfMade`, `gender`, `industries`( = `category`), `category`, `country`, `age`
- **Meta/ID (identifiers / 标识类)**: `rank`, `personName`, `firstName`, `lastName`, `date`
- **P1 (supporting variables / 支撑变量)**: all others (location, macro indicators, etc.)

### B1. Full register table (frozen list) 📋

| Variable | Role(P0/P1/Meta) | Raw dtype | Target dtype | Missing% | Example(s) | Definition (EN) | 定义（ZH） |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rank | Meta/ID | int64 | int64 | 0.0% | 1, 2 | Rank of billionaire in the list (not unique; ties exist). | 富豪榜单排名（非唯一，存在并列）。 |
| finalWorth | P0 | int64 | int64 | 0.0% | 211000, 180000 | Net worth value: USD millions (not provided in this dataset, but we can check the sources online and it's USD millions，This includes the value of their assets, investments, and other holdings.) | 净资产数值: “百万美元”（本文档未给出，但经由资料获知，它包括的是这个人的总资产+投资+其他的所有物） |
| category | P0 | object | category / string | 0.0% | Fashion & Retail, Automotive | Business sector/category label (text). | 行业/商业类别标签（文本）。 |
| personName | Meta/ID | object | category / string | 0.0% | Bernard Arnault & family, Elon Musk | Displayed full name (may include “& family”; not a unique ID). | 展示用姓名（可能含“& family”；不一定唯一）。 |
| age | P0 | float64 | float64 | 2.5% | 74.0, 51.0 | Age in years (some missing). | 年龄（年；有少量缺失）。 |
| country | P0 | object | category / string | 1.4% | France, United States | Country label (business country). | 国家标签（业务国家）。 |
| city | P1 | object | category / string | 6.4% | Paris, Austin | City label (string). | 城市（字符串）。 |
| source | P1 | object | category / string | 0.0% | LVMH, Tesla, SpaceX | Wealth source description (text). | 财富来源描述（文本）。 |
| industries | P0 | object | category / string | 0.0% | Fashion & Retail, Automotive | Industry label; =  `category`. | 行业标签；与category等价，本项目以 category 为 canonical（但 raw 不删除）。 |
| countryOfCitizenship | P1 | object | category / string | 0.0% | France, United States | Country of citizenship (string). | 国籍国家（字符串）。 |
| organization | P1 | object | category / string | 87.7% | LVMH Moët Hennessy Louis Vuitton, Tesla | Organization/company name (string; often missing). | 组织/公司名称（字符串；缺失较多）。 |
| selfMade | P0 | bool | bool | 0.0% | True, False | Whether the person is self-made (boolean). | 是否白手起家（布尔）。 |
| status | P1 | object | category / string | 0.0% |   'D': 1223 (46.33%)'U': 855 (32.39%) 'E': 268 (10.15%) 'N': 150 (5.68%) 'Split Family Fortune': 79 (2.99%) 'R': 65 (2.46%) | refer to the right side | **D**\_**Established Self-made**\_**成熟自创财富**\_高财富、高自创比例、年长$\quad$ **E**\_**Emerging Entrepreneur**\_**新兴企业家**\_中等财富、略低自创比例、年长 $\quad$ **N**\_**Newcomer/Novice**\_**新晋富豪**\_低财富、年轻、排名靠后 $\quad$ **U**\_**Ultra-Inherited**\_**巨大家族财富**\_极高财富、低自创比例、年长 $\quad$ **R**\_**Replenished**\_**复苏财富**\_中等财富、混合来源、较年轻$\quad$ **Split Family Fortune**\_**Divided Inheritance**\_**分割继承**\_高财富、低自创比例  |
| gender | P0 | object | category / string | 0.0% | M, F | Gender label (string). | 性别标签（字符串）。 |
| birthDate | P1 | object | datetime64[ns] (parsed) | 0.0% | 3/5/1949 0:00, 6/28/1971 0:00 | Birth date string (parseable to datetime). | 出生日期字符串（可解析为日期）。 |
| lastName | P1 | object | category / string | 0.0% | Arnault, Musk | Last name (string). | 姓（字符串）。 |
| firstName | Meta/ID | object | category / string | 0.0% | Bernard, Elon | First name (string). | 名（字符串）。 |
| title | P1 | object | category / string | 87.2% | Chairman, CEO | Business title/role (string; often missing). | 职位/头衔（字符串；缺失较多）。 |
| date | Meta/ID | object | datetime64[ns] (parsed) | 0.0% | 4/4/2023 5:01, 4/4/2023 9:01 | Record timestamp in dataset (string; parseable). | 数据记录时间戳（字符串；可解析）。 |
| state | P1 | object | category / string | 71.5% | Texas, Washington | State/province (string; often missing). | 州/省（字符串；缺失较多，但是仅对国籍为美国者有统计，同时极少部分部分美国国籍者未计入，处于合理范畴）。 |
| residenceStateRegion | P1 | object | category / string | 71.7% | `South` `West` `Midwest` `Northeast` `U.S. Territories` | Residence state/region label (string; often missing). | 居住州/地区标签（字符串；缺失较多，但是仅对国籍为美国者有统计，同时极少部分部分美国国籍者未计入，处于合理范畴）。 |
| birthYear | P1 | float64 | Int64 (nullable int) or keep float64 | 2.5% | 1949.0, 1971.0 | Birth year (numeric; derived from birthDate). | 出生年份（数值；由 birthDate 派生）。 |
| birthMonth | P1 | float64 | Int64 (nullable int) or keep float64 | 2.5% | 3.0, 6.0 | Birth month (1–12) (numeric; derived). | 出生月份（1–12；数值；派生）。 |
| birthDay | P1 | float64 | Int64 (nullable int) or keep float64 | 2.5% | 5.0, 28.0 | Birth day of month (1–31) (numeric； derived). | 出生日期（1–31；数值；派生）。 |
| cpi_country | P1 | float64 | float64 | 7.0% | 117.24, 156.46 | Consumer Price Index (CPI) for the billionaire's country. | 消费者价格指数 |
| cpi_change_country | P1 | float64 | float64 | 7.0% | 5.2, 8.0 | CPI change/inflation indicator for the country (numeric, %). | 国家 CPI 变化/通胀指标（数值，百分比）。 |
| gdp_country | P0 | object | float64 (after stripping $ and commas) | 6.2% | $2,715,518,274,227 , $21,427,700,000,000  | GDP for the country as a currency-formatted string; will be cleaned to numeric. | 国家 GDP（带 $ 和逗号的字符串；后续清洗为数值）。 |
| gross_tertiary_education_enrollment | P1 | float64 | float64 | 6.9% | 67.2, 88.2 | Gross tertiary education enrollment ratio (numeric, %). | 高等教育毛入学率（数值，百分比）。 |
| gross_primary_education_enrollment_country | P1 | float64 | float64 | 6.9% | 102.6, 101.8 | Gross primary education enrollment ratio (numeric, %). | 小学教育毛入学率（数值，百分比）。 |
| life_expectancy_country | P1 | float64 | float64 | 6.9% | 82.5, 76.3 | Life expectancy at birth (years). | 预期寿命（年）。 |
| tax_revenue_country_country | P1 | float64 | float64 | 6.9% | 9.6, 12.8 | Tax Revenue as % of GDP | 税收收入占GDP的百分比: 该国政府所有税收收入占其国内生产总值（GDP） 的比例 |
| total_tax_rate_country | P1 | float64 | float64 | 6.9% | 36.6, 59.1 | Total tax rate indicator (numeric; %). | 总税率指标（数值；是百分比）。 |
| population_country | P1 | float64 | float64 | 6.2% | 66834405.0, 331002651.0 | Country population (numeric). | 国家人口（数值）。 |
| latitude_country | P1 | float64 | float64 | 6.2% | 46.227638, 37.09024 | Country latitude (numeric). | 国家纬度（数值）。 |
| longitude_country | P1 | float64 | float64 | 6.2% | 2.213749, -95.712891 | Country longitude (numeric). | 国家经度（数值）。 |

> **Note / 注：** Definitions marked “verify / 需核对” are inferred from column names + sample values; confirm if your course/material provides an official data dictionary.

---

## C. Approved Derived Variables (allowed transformations) 🧪

**EN:** Derived variables are how we make analysis-friendly fields **without mutating raw schema**.  
**ZH:** 用派生变量来做“分析友好字段”，避免直接改动 raw schema。

### C1. Mandatory for heavy-tail robustness (recommended) 💪
- `log_finalWorth = log1p(finalWorth)`
- `gdp_country_num = parse_numeric(gdp_country)`  *(strip `$`, commas, whitespace)*
- `log_gdp = log1p(gdp_country_num)`

### C2. Datetime parsing (recommended)
- `birthDate_dt = to_datetime(birthDate)`
- `record_dt = to_datetime(date)`

### C3. Optional convenience
- `age_int = age.round().astype('Int64')` (nullable int)  
- `is_female = (gender == 'F')` *(only if gender coding is confirmed)*

---

## D. Change Log (Change Control) 🧷

### D1. Rule (non-negotiable) 🚫
- **EN:** Any change that affects interpretation or comparability **must** be logged (rename, recode, type conversion, filtering rules, new derived variables used in claims).
- **ZH:** 任何会影响“解释口径/结果可比性”的变更都必须记入日志（重命名、重新编码、类型转换、过滤规则、用于结论的新派生变量等）。

### D2. Change log template (copy-paste)
| Date | Change ID | Type (rename/recode/type/filter/derive) | Field(s) | Old | New | Reason | Expected impact | Validation (checks) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-02-26 | CL-001 | type | gdp_country | object with `$` and commas | float64 numeric | needed for correlation/regression | enables regression; may drop rows with unparsable GDP | compare missing% before/after; spot-check 10 rows |

---

## E. “How to write / 怎么写” (SOP for beginners) 🧭

### Step 1 — Auto-draft schema (5 min)
- **EN:** Load CSV → record `(rows, cols)`, column order, dtypes, missing%.
- **ZH:** 读入 CSV → 记录行列数、列顺序、类型、缺失率。

### Step 2 — Fill meanings for P0 vars (10–20 min)
- **EN:** For each P0 variable, write: *definition + unit + intended use + allowed transform*.
- **ZH:** 对每个核心变量写清：*定义 + 单位 + 用途 + 允许的变换*。

### Step 3 — Freeze (1 min)
- **EN:** Write Freeze ID + file hash + “no silent changes” rule.
- **ZH:** 写 Freeze ID + 文件 hash + “禁止静默改口径”。

### Step 4 — Change discipline (ongoing)
- **EN:** If you change anything later, add a Change Log row **before** re-running analysis.
- **ZH:** 之后任何变更，必须先写一条 Change Log 再重新跑分析。

---

## F. Completion checklist (DoD) ✅

- [ ] Variable Register table exists for **all 35 columns** (Section B1).
- [ ] P0 variables have clear unit/transform notes (Sections B0 + C).
- [ ] Schema Freeze includes file fingerprint + column order + ingest settings (Section A).
- [ ] Change Log template exists and rule is stated (Section D).