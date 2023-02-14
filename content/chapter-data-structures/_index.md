+++
title = "Data structures and performance"
outputs = ["Reveal"]
weight = 4 # chapter number
+++

{{< reveal-titlepage >}}
  
---

### Time complexity, big-O notation

- General idea: time it takes for an algorithm to run.
- Complexity: the number of steps involved in a process or pieces that make up a system ?

{{% fragment %}}
> Complexity makes a difference in everyday use:
>
> **Fast and high quality** services vs <br> those that **lag, crash, and are unreliable**
{{% /fragment %}}

---

### Big-O is calculated based on input size

- In data analytics, we will often work with large amounts of data
- Performance of algorithms matter more with large data

{{% fragment %}}
> Does this algorithm scale up when it is given a large input?

- Therefore, $O()$ notation indicates _growth_ of time with an input, _n_
{{% /fragment %}}

---

### Definitions: Big-O notation

- $O(1)$: constant time, independent of input size, $n$ <br>(e.g. getting an item from an array with an index)
- $O(\log(n))$: less than linear, exponent of $n$'s growth <br>(e.g., binary tree search; $log_2(4)=2$, $log_2(16)=4$)
- $O(\sqrt{n})$: more than log, less than $n$ (e.g., process one row of matrix data)
- $O(n)$: linear time with size (e.g. summation of every element in list)
- $O(n^k)$: polynomial time ($k$: constant) (e.g., nested loops over whole input)
- $O(2^n)$: exponential time (worst case; e.g., finding best route between two points)

{{% note %}}
TODO: add graph
{{% /note %}}

---

### Common algorithms

- Index lookup: $O(1)$
- Hash lookup: $O(1)$ (in Python: dict and sets)
- Binary search: $O(\log_2 n)$
- Search in array: $O(n)$
- Find prime numbers: $O(\sqrt{n})$
- Nested loops: $O(n^k)$
- Find diFFeRent cAPiTAlizations of words: $O(2^n)$

---

### Fork & practice!

Share REPL to work together with teammates. Submit team fork link once on Piazza.

<iframe height="500px" width="100%" src="https://repl.it/@cengique/Python-big-o#main.py?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

---

### Bitwise operators

Can you solve word capitalizations using binary numbers?

{{% fragment %}}
Take advantage of binary representation of computers!

[Bitwise operators in Python](https://wiki.python.org/moin/BitwiseOperators):

```python
x & 4  # will be non-zero only if x has 3rd bit on
x | 15 # will turn on lower 4 bits
x >> 4 # shift x by 4 bits to the right (faster than dividing by 2)
x & ~x # will always be 0
x ^ x  # will always be 0
```
{{% /fragment %}}

---

### Big-O can also apply memory size

- Same idea: $O(1)$, $O(n)$, etc
- Hashing usually requires additional space
- Do not use complex data structures unnecessarily!

---

### Constant time: The holy grail

Why does indexing an array take constant time, $O(1)$?

{{% fragment %}}
- In homogeneous arrays, each item takes the same memory space!
- You can multiply the index by item size to find offset of item:
$$ \mathsf{Item~at~index~} i = \mathsf{array~starting~address} + i * \mathsf{size~of~one~item}$$
{{% /fragment %}}

{{% fragment %}}
> Hint: In Python, `list` can contain heterogeneous items, but each item is
> an object reference that take up equal space.
{{% /fragment %}}

---

### What's hashing?

- hash is a math function that can calculate a number out anything
- the number would be unique (or close to) for each input
  ```
  hash("hello") -> 46487
  ```
- hash number can be used (with some tricks) as an **index**
- then you can use the index instead of searching with $O(1)$

#### Other uses:

- Comparing complex objects
- Sorting (only for values)
- Checksumming internet download packages

---

### About sets

Pros:
 * faster lookup times
 * ensures uniqueness of items
 * awesome methods (union, intersection, difference)

Cons:
 * uses more memory
 * slower to build and append to than a list

---

### Exercise time! Choose one:

Compare speed of: 

1. the programs you wrote in last exercise
1. list vs set operations:
    1. Searching an item OR
    1. Appending an item
1. finding common elements between two lists by:
    1. writing an $O(n^2)$ algorithm AND
    1. using set operations (hint: `intersection`)

---

### To find speed:

1. Initialize a long list, then create a set from it
1. Start a timer
1. Loop a large number of times (e.g. 100,000)
1. Put only one operation inside the loop to measure (e.g., `"hello" in my_list`)
1. Stop the timer and find elapsed time
1. Report time per operation by dividing with repeat multiplier you selected above

OR use [defbench](https://github.com/shitchell/defbench) that GGC graduate Shaun Mitchell made!

---

### Example program to measure performance

Copy-paste from [Repl](https://repl.it/@cengique/PerfMeasure-sp22#main.py) to local computer because cloud runs are not consistent:

<iframe height="500px" width="100%" src="https://repl.it/@cengique/PerfMeasure-sp22#main.py?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

{{% reveal-prevnext-links %}}
