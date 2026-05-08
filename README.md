# Simulador IRS · Portugal

Interactive Portuguese income tax (IRS) simulator covering fiscal years **2008–2026**. Runs entirely in the browser — calculations are client-side only, no data leaves your device.

**Live demo → [irs.lixo.dev](https://irs.lixo.dev)**

---

## Features

| Feature | Details |
|---|---|
| **Year selector** | All fiscal years 2008–2026 via pill bar |
| **Year-over-year Δ** | Take-home, net tax, and effective rate show the delta vs the previous year |
| **Municipal benefit** | Automatic deduction based on the selected municipality (~300 municipalities) |
| **Inflation-adjusted take-home** | For historical years, shows the real purchasing-power equivalent in today's euros |
| **Bracket viewer** | IRS bracket table for the active year, with the applicable bracket highlighted |
| **Dark / Light mode** | Dark (warm charcoal + Braun orange) and light (cream + orange) themes, preference saved in `localStorage` |
| **Accessible** | ARIA labels, `aria-live` regions, focus indicators, reduced-motion support |

---

## Tax Calculation

The simulator applies the standard Portuguese IRS formula for employment income (Categoria A):

```
specific_deduction  = max(legal_minimum_for_year, gross × 0.11)
collectable_income  = max(0, gross − specific_deduction)

bracket             = first bracket where collectable_income < upper_limit
base_tax            = collectable_income × marginal_rate − deduction_from_bracket

municipal_benefit   = (base_tax − collection_deductions) × (0.05 − municipal_rate)
net_tax             = base_tax − collection_deductions − max(0, municipal_benefit)

take_home           = gross − specific_deduction − net_tax
effective_rate      = net_tax / gross × 100
```

> **Note:** The 5% in the municipal benefit formula is the maximum allowed municipal surcharge; each municipality sets its own rate from 0% to 5%, and the benefit is the difference from the maximum.

---

## Stack

| Layer | Technology |
|---|---|
| Framework | [Astro 5](https://astro.build) — static output, no JS sent by default |
| Reactivity | [Alpine.js 3.14](https://alpinejs.dev) via CDN |
| Styling | Plain CSS with CSS custom properties (dark/light themes) |
| Data | JSON files (`src/data/`) imported at build time |
| Fonts | [Plus Jakarta Sans](https://fonts.google.com/specimen/Plus+Jakarta+Sans) + [JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono) |

---

## Project Structure

```
src/
├── data/
│   ├── tax-data.json       ← tax brackets, specific deductions, county rates — all years
│   └── inflation.json      ← annual inflation rates (2008–2025)
├── styles/
│   └── main.css            ← all CSS (dark/light themes, responsive layout)
└── pages/
    └── index.astro         ← the page: imports JSON, injects data for Alpine.js
public/
├── robots.txt
├── sitemap.xml
└── llms.txt                ← AI-readable site description
astro.config.mjs
package.json
```

---

## Getting Started

```bash
npm install
npm run dev      # dev server at http://localhost:4321
npm run build    # static output → dist/
npm run preview  # preview the build locally
```

---

## Adding or Updating a Tax Year

All fiscal data lives in **`src/data/tax-data.json`**. To add a new year, append a new key following the existing pattern:

```jsonc
{
  "2027": {
    "specific_deduction": 4600.00,   // minimum specific deduction (€)
    "social_security_tax": 0.11,     // SS rate for specific deduction calculation
    "table": {
      "1": { "to": 8500,        "parcel": 0,        "tax": 0.125  },
      "2": { "to": 12800,       "parcel": 275.00,   "tax": 0.157  },
      // ...remaining brackets...
      "9": { "to": 10000000000, "parcel": 11500.00, "tax": 0.48   }
    },
    "county_tax": {
      "lisboa": 0.005,
      "porto":  0.025,
      // ...all municipalities...
    }
  }
}
```

Then add `"2027"` to the `availableYears` array in `src/pages/index.astro`.

To update inflation data, add an entry to **`src/data/inflation.json`**:

```json
{ "year": 2026, "inflation": 2.10 }
```

---

## Data Sources

| Data | Source |
|---|---|
| IRS brackets & deductions | [Código do IRS](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/irs_rep/) and annual Orçamentos do Estado |
| Municipal surcharge rates | Annual deliberations of Municipal Assemblies, published by AT |
| Inflation (IHPC) | [Banco de Portugal](https://www.bportugal.pt) / [INE](https://www.ine.pt) |

> Data for 2008–2021 are approximations based on published legislation. Always verify with the official AT simulator for decisions with legal or financial consequences.

---

## SEO & AI

The site is instrumented for discoverability:

- **`/robots.txt`** — explicitly allows all major AI crawlers (GPTBot, Claude-Web, PerplexityBot, Google-Extended, …)
- **`/sitemap.xml`** — single-URL sitemap
- **`/llms.txt`** — plain-text description of the tool, formula, and data coverage for LLM agents
- **JSON-LD** (`WebApplication` + `FinanceApplication`) in the `<head>`
- Full Open Graph and Twitter Card tags

---

## Disclaimer

This simulator is an approximation for **Categoria A** (employment) income only. It does not account for:

- Family/dependant deductions
- Health, education, or housing deductions
- Extraordinary surcharges or regional autonomous region rates
- Non-resident or special tax regime rules

**It does not replace the official AT declaration or a qualified tax advisor.**

---

## License

MIT
