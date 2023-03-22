+++
title = "Working with vector data"
outputs = ["Reveal"]
weight = 10 # chapter number
+++

<style>
.reveal pre {
    width: 70%
}
</style>

{{< reveal-titlepage >}}
  
---

<section>

### Python's Numpy module

From *Python for Data Analysis, 2nd Ed*, chapter 4:
- enables working with $n$-dimensional arrays
- math functions without needing to loop over arrays
- reading/writing to files
- advanced math: linear algebra, random numbers, etc

---

### Numpy overview

- Creating and manipulating `ndarray` objects and doing math on them
- Data types for efficient storage and use
- Indexing and slicing; with boolean expressions and *fancy* indexing
- Unary and binary math functions

---

### How do dimensions work?

1 dimension: 1 bracket, 1 index
```python
arr1d = np.array([1, 2, 3])
arr1d[x]
```

{{% fragment %}}

2 dimensions: 2 brackets, 2 indices
```python
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])
arr2d[x, y]
```

{{% /fragment %}}

{{% fragment %}}

3 dimensions: ... 
```python
arr3d = np.array([[[ 1,  2,  3],
                   [ 4,  5,  6]],
                  [[ 7,  8,  9],
                   [10, 11, 12]]])
arr3d[x, y, z]
```

{{% /fragment %}}


---

### Numpy practice

Work in groups and choose one of these problems (thanks math people!):
1. [Largest product in a grid](https://projecteuler.net/problem=11)
1. [Maximum path sum II](https://projecteuler.net/problem=67)
1. [Non-abundant sums](https://projecteuler.net/problem=23)
1. [Lexicographic permutations](https://projecteuler.net/problem=24)

Make sure to:
- Create numpy arrays in 1D, 2D, and 3D
- Index slices in 1D, 2D, and 3D
- Do some arithmetic
- Use Boolean indexing
- Fork [this](https://replit.com/@cengique/numpy-practice) to submit **individually**

</section>

---

<section>

### Linear algebra basics:
### Vectors and matrices

---

### Basics: Vectors

Vectors: $\vec{x} = [ 1, 2, 3 ]$
- Why? Most data comes in vectors

Can do bulk operations using math magic:
- Adding or subtracting a scalar: $$ \vec{x} + 1 = [ 2, 3, 4 ] $$
- Multiplying or dividing by a scalar: $$ \vec{x} \times 2 = [ 2, 4, 6 ] $$
- Adding two vectors (of same size): $$ \vec{x} + \vec{x} = [ 2, 4, 6 ] $$

---

### Vector math: dot product

inner/[dot product](http://mathworld.wolfram.com/DotProduct.html): $$ \vec{x} \cdot \vec{y} = \sum x_i y_i $$

- Calculates "length of projection" in geometric sense
- Multiply corresponding elements and sum to result in scalar
- Useful in calculating weighted sums, scaling data elements, etc.

{{% fragment %}}

Example: sum of products to find total price

```python
quantity = np.array([1, 1, 5, 2])
prices = np.array([10, 15, 1.25, 20])
total = np.dot(prices, quantity)
``` 

Result: `71.25`

{{% /fragment %}}

---

### Vector math: outer product

[(definition)](https://en.wikipedia.org/wiki/Outer_product)

$$ \vec{x} \times \vec{y} = [x_i y_j]_{ij} $$ 

- element-by-element multiplication, results in $ n \times m $ size matrix
- useful when duplicating rows or columns, or scaling them

{{% fragment %}}

Example:

```python
item_prices = np.full((1,5), 50) # all $50
inflation_per_month = np.array([1.1, 1.3, 1.3, 1.4]) # monthly inflation
new_prices_per_month = np.outer(inflation_per_month, item_prices)
``` 

Result:
```python
array([[55., 55., 55., 55., 55.],
       [65., 65., 65., 65., 65.],
       [65., 65., 65., 65., 65.],
       [70., 70., 70., 70., 70.]])
```

{{% /fragment %}}

---
### Basics: Matrices

$$ A=\left[ \begin{array}{ccc}
a_{11} & \cdots & a_{1n} \newline
\vdots & \ddots & \vdots \newline
a_{m1} & \cdots & a_{mn} \newline
\end{array} \right] $$

Uses:
- Aggregation of many vectors
- Bases for transformation spaces
- Image data and manipulation
                  
---
#### Matrix multiplication
                  
Must have matching inner dimensions, results in a matrix:
$$ A_{m\times n} \times B_{n\times o} = C_{m\times o} $$

Each element of output matrix is the result of one _inner product_:
$$ c_{ij} = \sum_k a_{ik} b_{kj} $$

Rows of $A$ matched to columns of $B$ to create single elements of $C$:
$$ \left[ \begin{array}{c}
\bbox[5px,yellow,border:2px solid red]{\begin{array}{ccc} 
a_{11} & \cdots & a_{1n} 
\end{array}} \newline
\begin{array}{ccc} 
\vdots & \ddots & \vdots \newline
a_{m1} & \cdots & a_{mn} \newline
\end{array}
\end{array} \right] \times
\left[ \begin{array}{cc}
\bbox[5px,yellow,border:2px solid red]{\begin{array}{c}
b_{11} \newline
\vdots \newline
b_{n1}
\end{array}} &
\begin{array}{cc}
\cdots & b_{1o} \newline
\ddots & \vdots \newline
\cdots & b_{no} \newline
\end{array}
\end{array} \right] =
\left[ \begin{array}{ccc}
\bbox[5px,yellow,border:2px solid red]{c_{11}} & \cdots & c_{1o} \newline
\vdots & \ddots & \vdots \newline
c_{m1} & \cdots & c_{mo} \newline
\end{array} \right]
$$


---

### Uses of matrix algebra

- Useful transforming rows of data, image operations, 3D rotations, machine learning, etc.
- [Google's PageRank algorithm](https://en.wikipedia.org/wiki/PageRank) is:
    > [...] calculated using a simple iterative algorithm, and corresponds to the
principal eigenvector of the normalized link matrix of the web.
    (from [original paper](http://infolab.stanford.edu/pub/papers/google.pdf))
- Inverse of a matrix can be calculated to satisfy:
    $$ A\times A^{-1} = I$$
- Solving linear sets of equations: $$Ax+b=y$$


</section>

---

<section>

### NumPy: conventional looping versus vector operations

Loop through your data and calculate mean and standard deviation (or regression, min, max, etc.).

```python
vector = [1,2,3]
sum = 0
for element in vector:
    sum += element
mean = sum / len(vector)
```

{{% fragment %}}

Use vector operations to do it shorter and more efficiently. 
$$ \mu = \sum_{i=1..N} x_i / N $$
```python
import numpy as np
vector = np.array([1,2,3])
mean = np.sum(vector) / len(vector)
```

{{% /fragment %}}

---

### Numpy exercise

Calculate standard deviation
$$ \sigma = \sqrt{ \sum_{i=1..N} ( x_i - \mu )^2 / ( N - 1 ) } $$
where $N$ is the number of elements in $ \vec{x} $ and $ \mu $ is its mean.

Submit by following instructions on the page below.

---

### Make a Colab notebook with your solution

- Work in groups as before
- Log into [Google Colab](https://colab.research.google.com/) with any Google account
- Create a new Python notebook
- Write some text and code blocks to explain your standard deviation code
- Compare your result to the output of `np.std(vector, ddof=1)` in your notebook
- Share your link on Piazza

</section>

---

<section>

### Pandas supports tabular data

<img src="/lectures-prog-data-analysis/images/pandas_logo.svg" style="background: gray; width: 50%">

- https://pandas.pydata.org/
- Akin to spreadseets and SQL tables
- Based on Numpy, but builds on it
- Primary components: `Series` and `DataFrame`
- Continue with Python for Data Analysis, chapter 5

---

### Pandas objects:

- Series for 1-D data
- DataFrame for 2-D data
- Indexing
- Filtering

---

### Hands on activity

- Work in groups as before
- Log into [Google Colab](https://colab.research.google.com/) with any Google account
- Create a new Python notebook
- Create a Dataframe object from any data
- Extract a Series object from your DataFrame
- Use slicing and fancy indexing to get subsets of your DataFrame
- Apply one comparison operator to get a boolean matrix and use it for indexing your DataFrame
- Share your link on Piazza


</section>
