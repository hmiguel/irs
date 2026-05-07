# Simulador IRS · Portugal

Simulador de IRS português para os anos **2008–2026**. Corre directamente no browser — sem build, sem dependências locais.

## Funcionalidades

- **Simulação anual** — selecciona qualquer ano fiscal de 2008 a 2026 via barra de pills
- **Δ variação interanual** — o take-home, a coleta líquida e a TET mostram o delta face ao ano anterior
- **Benefício municipal** — dedução automática baseada no município seleccionado (dados 2024)
- **Poder de compra ajustado** — para anos históricos, mostra o equivalente em euros do ano mais recente corrigido pela inflação acumulada
- **Escalões** — tabela de escalões do IRS para o ano activo, com destaque no escalão aplicável
- **Dark / Light mode** — tema escuro (carvão quente + laranja Braun) e claro (creme + laranja), com preferência guardada em `localStorage`

## Stack

| | |
|---|---|
| UI | [Alpine.js 3.14](https://alpinejs.dev) — zero build |
| Fonte UI | [Plus Jakarta Sans](https://fonts.google.com/specimen/Plus+Jakarta+Sans) |
| Fonte números | [JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono) |
| Dados fiscais | `index.html` (inline JS) + `metadata.json` |
| Dados inflação | `inflation.json` |

## Utilização

Abre `index.html` directamente no browser. Não é necessário servidor.

```
open index.html
```

## Ficheiros

```
index.html      — aplicação completa (HTML + CSS + JS)
metadata.json   — tabelas de IRS e deduções municipais por ano
inflation.json  — taxas de inflação anuais (2008–2025)
```

## Aviso

Cálculo aproximado. Não substitui a declaração oficial na AT.
Os dados de 2008–2023 são estimativas baseadas na legislação publicada.
