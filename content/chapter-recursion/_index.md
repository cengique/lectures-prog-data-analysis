+++
title = "Recursion"
outputs = ["Reveal"]
weight = 50 # chapter number
+++

<style>
div.goat > svg {
    width: 200px; max-height: 200px; margin-left: auto; margin-right: auto;
}
</style>

{{< reveal-titlepage >}}
  
---

[![](https://www.smbc-comics.com/comics/1562409923-20190706.png)<br>
(click to read more)](http://smbc-comics.com/comic/recursion)

---

### What is recursion

- Reusing a function
- Calling itself
- Similar to a loop
- But not linear, instead it could be exponential

```python
def recursive(x):
    print(x)
    if x < 10:
        recursive(x + 1)
```


---

### Why recursion

What is the advantage over loops?
- Divide-and-conquer type problems
- Tree search
- Sorting
- Elegant solution

Limitations?

{{% fragment %}}

- Less efficient
- Can exhaust program stack

{{% /fragment %}}

---

{{< youtube Qk0zUZW-U_M >}}

---

### Designing a recursive algorithm

1. Do you have a nesting doll situation? Identify the part in your problem that repeats and when that happens. 
1. {{% fragment %}} Identify when the recursion ends. What is the condition that stops it? {{% /fragment %}}

---

### Example: Factorial

$$f(n)=n!$$
$$f(n)=n\times{}(n-1)\times\cdots\times{}2\times{}1$$

What is the **repeating part** versus the **termination condition**?

{{% fragment %}}
1. Repeating pattern: each time multiply with one less number $$f(n)=n\times f(n-1)$$
1. Termination condition: we stop at 1 $$f(1)=1$$
{{% /fragment %}}

---

### Classic example: factorial

For demo purposes only, not today's class activity.
<!-- code on REPL:
def factorial(n):
  if n <= 1:
    return 1
  else:
    return  n * factorial(n - 1)
-->

<iframe
  src="https://jupyterlite.github.io/demo/repl/index.html?kernel=python&toolbar=1&code=def%20factorial(n):%0A%20%20if%20n%20%3C=%201:%0A%20%20%20%20return%201%0A%20%20else:%0A%20%20%20%20return%20%20n%20*%20factorial(n%20-%201)%0A%20%20%20%20"
  width="100%"
  height="400"
></iframe>

```python
num = int(input("Enter a number to factorialize:"))
print("Factorio of", num, "is", factorial(num))
```

<!--iframe height="400px" width="100%" src="https://repl.it/@cengique/Recursion-factorial?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe-->

---

### Trees

A [binary tree](https://en.wikipedia.org/wiki/Binary_tree):

<div style="width: 150px; height: 150px; margin-left: auto; margin-right: auto">

```goat
    o b 
   / \
a o   o c
```
</div>

Always true in [sorted binary tree (or binary search tree - BST)](https://en.wikipedia.org/wiki/Binary_search_tree):
$a<b<c$

Not a linear data structure, `b` is root node, `b.left=a` and `b.right=c`

<div style="width: 500px; margin-left: auto; margin-right: auto">

```python
class Node:
    def __init__(self, info): 
        self.info = info
        self.left = None
        self.right = None 
```

</div>

---

### Traversing trees without recursion

Can we write a non-recursive program to count all the nodes in tree?


```goat
    4 
   / \
   
  3   8 
 /   /
 
2   6
     \
     
      7
```

Start with `root` node object (`root.info=4`), and you can go `root.left` or `root.right` to get to the next node. If there is no node, it will be an empty object (`None`).

{{% fragment %}}
Does it work for any tree?
{{% /fragment %}}

---

### With recursion

```goat
    4 
   / \
   
  3   8 
 /   /
 
2   6
     \
     
      7
```

```python
def node_count(node, count):
    if node.left:
        count = node_count(node.left, count + 1)
    if node.right:
        count = node_count(node.right, count + 1)
    return count

print(node_count(root, 1))
```

{{% fragment %}}
Does it work for any tree?
{{% /fragment %}}

---

### Class activity: Solve ONE of these problems

1. [Inorder Traversal (HackerRank)](https://www.hackerrank.com/challenges/tree-inorder-traversal/problem?isFullScreen=true)
1. [Preorder Traversal (HackerRank)](https://www.hackerrank.com/challenges/tree-preorder-traversal/problem?isFullScreen=true)
1. [Postorder Traversal (HackerRank)](https://www.hackerrank.com/challenges/tree-postorder-traversal/problem?isFullScreen=true)

Advanced:
1. [Height of binary tree (HackerRank)](https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem?isFullScreen=true)
1. [Binary search tree insertion](https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem?isFullScreen=true)

Post your solution link on Piazza.

---

[![](https://imgs.xkcd.com/comics/fixing_problems.png)<br>
(click to read more)](https://xkcd.com/1739/)

