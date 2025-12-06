+++
title = "Python basics refresher"
outputs = ["Reveal"]
weight = 30 # chapter number
+++

{{< reveal-titlepage figure="/lectures-prog-data-analysis/images/DS_scratch_cover.png" >}}
  
---

### The very basics

{{% figure src="/lectures-prog-data-analysis/images/PDA_cover.png" class=float-left height=400
    caption="Chapter 2.3" %}}

- Python history: version 2 vs 3; now popular for AI & ML
- Whitespace, quotations, language conventions, operators
- Control statements: blocks, if-elif-else, while
- Modules and import

{{% fragment %}}

#### A Quick Practice!

This is a good place to practice what we reviewed so far. Think of a theme and use [Brython](https://brython.info/tests/editor.html?lang=en) to write your program with:

- At least three variables and do some artithmetic
- One list, one function, and one if statement with elif and else
- One for and one while loop, and use continue and break
- Print a lot of things
- Click on the "Share" button to post on forum

{{% /fragment %}}

---

An *ephemeral* Python practice area (wait for it to load)

<iframe src="https://jupyterlite.github.io/demo/repl/index.html?kernel=python&amp;toolbar=1&amp" width="800px" height="600px"></iframe>

---

### How to practice Python

Do one or more of these based on your preferences!
- Use online IDEs ([Brython Editor](https://brython.info/tests/editor.html?lang=en) - no ads, can get share link)
- Download from [Pyton.org](https://www.python.org/downloads/)
- Download IDE [PyCharm](https://www.jetbrains.com/pycharm/) ([student discount](https://www.jetbrains.com/community/education/#students/))
- Download IDE [Visual Studio Code](https://code.visualstudio.com/) with Python plugin
- Download [Jupyter](https://jupyter.org/) (we'll use it in second half of semester)

---

### A crash course into Python

{{% figure src="/lectures-prog-data-analysis/images/DS_scratch_cover.png" class=float-left height=400
    caption="See Chapter 2." %}}

- Zen of Python
- Installing 
- Virtual environments
- Whitespace
- Modules and import
- Functions
- Strings

---

### Practice functions

Work in teams, but only one person should submit. Write Python code
online or in your own IDE to:
- List your teammates' names in a **comment** at the top.
- Print out a salutation message with a function that has **default
  function parameters**. Show its usage for parameters that are
  provided vs. missing.
- Add a **docstring** to your function. Demonstrate how your docstring
  is displayed with the `help()` function.
- Create a **list** and a **for loop** that prints out each element using
  **f-strings**.
- Add an **if-statement** that behaves differently for some elements of
  the list by applying two or more **lambda functions**.

Have a theme of your choice and make it interesting!

<!--iframe height="500px" width="100%" src="https://replit.com/@cengique/Python-functions-sp24?lite=true#main.py" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe-->

---

### Language basics

(Continuing DSS Chapter 2)

- Lists
- Tuples
- Dictionaries (default, Counter)

---

### Practice basics in-class exercise

Work in teams on any IDE. Create a program with a theme of your choice
that uses all of the elements from both of the following lists:

**Dictionaries**: 
- Take input from a user in a loop
- Add to a dictionary items and their associated values
- Then check if items exist in the dictionary
- Delete items from dictionary based on conditions
- Print out the dictionary

**Also include** the following elements:
- A function that returns multiple values using a tuple
- Use list unpacking to assign variables from tuple
- Access a list's elements by using slicing

<!--iframe height="500px" width="100%" src="https://replit.com/@cengique/Python-dict-sp24?lite=true#main.py" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe-->

---

### Misc Python Oddities

(Continuing DSS Chapter 2)

- Sets
- Control flow
- Truthiness
- Sorting
- List comprehensions
- Zip and argument unpacking
- Type annotations (just the basics)

---

### Practice Misc Python Stuff

Work in teams on any IDE. Create a program that includes:
- A set: add elements and check for membership
- An if-elif-else statement
- A loop with use of break and continue
- Use truthiness of data structures in a conditional statement (other than simple binary operators), could be for loop logic
- sort a data structure and print them out
- create a list using the list comprehension syntax, you can use the data from the set
- use zip somewhere
- specify type annotations in at least one place
- make sure it's sufficiently distinct from others' submissions and that your program has a theme

<!--iframe height="500px" width="100%" src="https://replit.com/@cengique/Python-misc-features-sp23?lite=true#main.py" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe-->
