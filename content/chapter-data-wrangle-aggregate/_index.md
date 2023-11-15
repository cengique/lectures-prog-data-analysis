+++
title = "Data plotting, wrangling, and aggregation"
outputs = ["Reveal"]
weight = 12 # chapter number
+++

{{< reveal-titlepage >}}

---
<section>

### Data plotting

- See Python for Data Analysis, Chapter 9

{{% fragment %}}

Main library is `matplotlib`:
- Controls how figures are laid out and decorated (axes, labels, colors, line styles, etc)
- Can be used directly
- Pandas uses it indirectly, but allows using `matplotlib` commands

{{% /fragment %}}

---

### Anatomy of a plot in matplotlib

<img style="width: 50%;" src="/lectures-prog-data-analysis/images/plot-simple.png" />

1. **figure**: The graphical area for one figure
1. **axis**: Labeled axis for XY, can be superimposed or tiled
1. **plot**: Individual shapes (lines, rectangles, etc) drawn on an axis

---

### Types of Plots

- line and scatter graphs
- bar graphs and distributions (histogram vs density)
- other statistics (boxplots)
- image plots ([matplotlib commands](https://matplotlib.org/stable/tutorials/introductory/sample_plots.html#contouring-and-pseudocolor))
- surface plots ([matplotlib commands](https://matplotlib.org/stable/tutorials/introductory/sample_plots.html#three-dimensional-plotting))

(see [plotting in pandas using
matplotlib](https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html))

</section>

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

- `stack/` vs `unstack`
- `reshape`
- "long" vs "wide" format
  - `pivot` vs `melt`

{{% /section %}}

---

{{% section %}}

### Data aggregation

- See Python for Data Analysis, Chapter 10

---

#### Groupby: split-apply-combine

- selecting column(s) and index levels
- aggregation functions
- `apply()` arbitrary functions

---

#### Pivot tables and cross-tabulation

- `pivot_table`
- `crosstab`

{{% /section %}}
