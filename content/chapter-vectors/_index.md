+++
title = "Working with vector data"
outputs = ["Reveal"]
weight = 10 # chapter number
+++

{{< reveal-titlepage >}}
  
---

{{% section %}}

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

### Numpy practice

- Work in groups
- Create numpy arrays in 1D, 2D, and 3D
- Index slices in 1D, 2D, and 3D
- Do some arithmetic
- Have a meaning?
- Fork [this](https://replit.com/@cengique/numpy-practice) to submit

{{% /section %}}

---

{{% section %}}

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

### Vector math

inner/[dot product](http://mathworld.wolfram.com/DotProduct.html): $$ \vec{x} \cdot \vec{y} = \sum x_i y_i $$

- Calculates "length of projection"
- Multiply corresponding elements and sum to result in scalar
- Useful in calculating weighted sums, scaling data elements, etc.
                  
[outer product](https://en.wikipedia.org/wiki/Outer_product): $$ \vec{x} \times \vec{y} = [x_i y_j]_{ij} $$ 
- element-by-element multiplication, results in $ n \times m $ size matrix
- useful when duplicating rows or columns, or scaling them

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

Useful transforming rows of data, image operations, 3D rotations, machine learning, etc.

{{% /section %}}

---

{{% section %}}

### NumPy: conventional looping versus vector operations

Loop through your data and calculate mean and standard deviation (or regression, min, max, etc.).

```python
vector = [1,2,3]
sum = 0
for element in vector:
    sum += element
mean = sum / len(vector)
```

Use vector operations to do it shorter and more efficiently. 
$$ \mu = \sum_{i=1..N} x_i / N $$
```python
import numpy as np
vector = np.array([1,2,3])
mean = np.sum(vector) / len(vector)
```
---

### Numpy exercise

Calculate standard deviation
$$ \sigma = \sqrt{ \sum_{i=1..N} ( x_i - \mu )^2 / ( N - 1 ) } $$
where $N$ is the number of elements in $ \vec{x} $ and $ \mu $ is its mean.

Submit by forking [this](https://replit.com/@cengique/numpy-beginner-sp22#main.py)

---

### Make a Colab notebook with your solution

- Work in groups as before
- Log into [Google Colab](colab.research.google.com/) with any Google account
- Create a new Python notebook
- Write some text and code blocks to explain your standard deviation code
- Compare your result to the output of `np.std(vector, ddof=1)` in your notebook
- Share your link
