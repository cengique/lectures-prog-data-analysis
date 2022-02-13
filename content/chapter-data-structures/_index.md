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

- $O(1)$: constant time 
    (e.g. getting an item from an array with an index)
- $O(\log(n))$: less than linear, exponent of n's growth (e.g., binary tree search; $log_2(4)=2$, $log_2(16)=4$)
- $O(\sqrt{n})$: more than log, less than n (e.g., process one row of matrix data)
- $O(n)$: linear time with size (e.g. summation of every element in list)
- $O(n^k)$: polynomial time ($k$: constant) (e.g., nested loops over whole input)
- $O(2^n)$: exponential time (worst case; e.g., finding best route between two points)

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

### Popular algorithms

- Index lookup: $O(1)$
- Search in array: $O(n)$
- Hash lookup: $O(1)$ (in Python: dict and sets)

---

### About sets

Pros:
 * faster lookup times
 * ensures uniqueness of items
 * awesome methods for determining what elements two sets do and do not share

Cons:
 * uses more memory
 * slower to build and append to than a list

---

### Big-O can also apply memory size

- Same idea: $O(1)$, $O(n)$, etc
- Hashing usually requires additional space
- Do not use complex data structures unnecessarily!

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

### Exercise time!

Compare speed of two operations:
1. Searching an item in list versus a set
1. Appending an item in list versus a set

{{% fragment %}}
#### To find speed:
1. Initialize a long list, then create a set from it
1. Start a timer
1. Loop a large number of times (e.g. 100,000)
1. Put only one operation inside the loop to measure (e.g., `"hello" in my_list`)
1. Stop the timer and find elapsed time
1. Report time per operation by dividing with repeat multiplier you selected above

OR use [defbench](https://github.com/shitchell/defbench) that GGC graduate Shaun Mitchell made!
{{% /fragment %}}

---

### Example program to measure performance

Copy-paste locally because cloud runs are not consistent:
<iframe height="500px" width="100%" src="https://repl.it/@cengique/PerfMeasure-sp22?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

