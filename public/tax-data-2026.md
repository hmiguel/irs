# Portuguese IRS Tax Data — 2026

## Context

- **IRS** is the Portuguese personal income tax (*Imposto sobre o Rendimento das Pessoas Singulares*).
- This data applies to **mainland Portugal only**. The autonomous regions of Madeira and the Azores have their own regional assemblies and set different (usually lower) IRS rates — this dataset does not cover them.
- Tax is calculated on **annual gross income** minus deductions. The standard deduction for employment income is the *deducção específica* (whichever is higher: the fixed amount or actual Social Security contributions).
- Brackets use a **marginal + abatement parcel** formula: `tax = income × bracket_rate − parcel`. This avoids cliff edges between brackets.
- The **county tax** (*taxa municipal*) is a surcharge on top of the national IRS, set by each municipality. It ranges from 0% to 5% and is applied to the same taxable income. See the full municipality list in the JSON dataset.
- Workers earning up to the **minimum monthly income threshold** (×14 months) pay zero IRS — this is the *mínimo de existência* rule.
- **IAS** (*Indexante dos Apoios Sociais*) is a reference index used to calculate several social thresholds.

---

## 2026 Rates and Parameters

| Parameter | Value |
|---|---|
| Specific deduction (employment) | €4,462.15 |
| Social Security rate (employee) | 11% |
| IAS (2026) | €537.13 |
| Minimum monthly income (mínimo de existência) | €920/month × 14 = €12,880/year |

---

## 2026 Tax Brackets

| Bracket | Taxable income up to | Marginal rate | Abatement parcel |
|---|---|---|---|
| 1 | €8,342 | 12.5% | €0.00 |
| 2 | €12,587 | 15.7% | €266.94 |
| 3 | €17,838 | 21.2% | €959.26 |
| 4 | €23,089 | 24.1% | €1,476.45 |
| 5 | €29,397 | 31.1% | €3,092.77 |
| 6 | €43,090 | 34.9% | €4,209.94 |
| 7 | €46,566 | 43.1% | €7,743.27 |
| 8 | €86,634 | 44.6% | €8,441.48 |
| 9 | Above €86,634 | 48.0% | €11,387.17 |

**Formula:** `annual_tax = taxable_income × rate − parcel`

Where `taxable_income = gross_annual − specific_deduction` (minimum of Social Security contributions paid, floor at €4,462.15).

---

## County Tax (Municipal Surcharge)

Each of Portugal's 278 mainland municipalities sets its own surcharge rate (0%–5%) applied on top of the national IRS liability. The full table of all municipalities and their 2026 rates is available in the JSON dataset.

---

## Disclaimer

This data was compiled through independent research and is provided for informational purposes only. It may contain errors or omissions. Always verify against official publications from AT (Autoridade Tributária e Aduaneira) or the Portuguese tax authority before making any financial or tax decisions.

---

## Full Dataset

Historical data for all years (2002–2026), including all tax brackets, deductions, Social Security rates, and county tax rates per municipality, is available at:

- **JSON (all years):** https://irs.lixo.dev/tax-data.json
- **Interactive simulator:** https://irs.lixo.dev
