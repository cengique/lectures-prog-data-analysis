+++
title = "Python data structures"
outputs = ["Reveal"]
weight = 2 # chapter number
+++

{{< reveal-titlepage >}}
  
---

### Time complexity, big-O notation

- General idea: time it takes for an algorithm to run.
- complexity: the number of steps involved in a process or pieces that make up a system ?

{{% fragment %}}
> It makes a difference in everyday use:
>
> **Fast and high quality** services vs <br> those that **lag, crash, and are unreliable**
{{% /fragment %}}

---

### Big-O calculated based on size

- We are more concerned about performance of algorithms when they work large amounts of data
- Does this algorithm scale up when it is given a large input?
- Therefore, O() notation indicates _growth_ of time with an input, _n_

---

### Definitions: Big-O notation

- $O(1)$: constant time 
    (e.g. getting an item from an array with an index)
- $O(\log(n))$: less than linear, exponent of n's growth (e.g., binary tree search; $log_2(4)=2$, $log_2(16)=4$)
- $O(\sqrt{n})$: more than log, less than n (e.g., ...?)
- $O(n)$: linear time with size (e.g. summation of every element in list)
- $O(n^2)$: polynomial time, in this case squared (e.g., two nested for loops, going through the whole list)

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

Compare speed of two functions:
1. One that searches a string in a list
1. One that finds a string in a set

To find speed:
1. Start a timer
1. Run the test a large number of times (e.g. 1000)
1. Stop the timer and find elapsed time
1. Report time per operation by dividing with repear multiplier (e.g., 1000)
