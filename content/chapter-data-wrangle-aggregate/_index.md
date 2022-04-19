+++
title = "Data wrangling and aggregation"
outputs = ["Reveal"]
weight = 12 # chapter number
+++

{{< reveal-titlepage >}}

---

{{% section %}}

### Data wrangling

- See Python for Data Analysis, Chapter 8

---

#### Hierarchical indexing:

- partial indexing
- `unstack()` method converts to `DataFrame`
- `stack()` is the reverse
- `swaplevel()` for reordering hierarchical indices
- `sort_index()` for sorting by one index
- Summary statistics with vector operators, such as `sum(level=, axis=)`

---

#### Combining and merging

- `merge()` by using keys (indices) like the SQL *join* operator
  - inner, left, right, and outer joins possible
- `concat()` for stacking objects

---

#### Reshape and pivot

- `stack/unstack`
- `reshape`
- `pivot`

{{% /section %}}

---

### Data cleaning

- Missing data with N/A, NaN, and NULL values
- Filtering missing data out
- Filling in missing data values
- Eliminating duplicates
- Replacing values
- Adding new calculated columns
- Cosmetics (axis labels, etc)
- Discretization
- Outliers
- Random sampling and shuffling
- String manipulation and regular expressions
