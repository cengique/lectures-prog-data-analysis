+++
title = "Object Oriented Programming"
outputs = ["Reveal"]
weight = 40 # chapter number
+++

{{< reveal-titlepage >}}
  
---

### What is object oriented programming?

- Analogy to way we interact with objects in real world
- A component-oriented approach
- Promotes reusability

---

### OOP: encapsulation and data abstraction

- Two of the fundamental pillars of OOP
- Data and functions (methods) go together
- Unimportant details of code are hidden

---

### OOP in Python

Module 3 from [Python Essentials 2](https://skillsforall.com/learningcollections/python?courseLang=en-US) (old resource: [HyperSkill](https://hyperskill.org/knowledge-map/482))
- Constructors
- Class attributes
- Instance attributes
- Calling class methods
- [Magic methods](https://realpython.com/python-magic-methods/)

---

### Class activity: make your own class!

- Teams of 2, pick a marker
- Write code on a board that includes:
{{% fragment %}}
  - A class with a constructor
  - One or more method functions
  - Make sure to have some class attributes that serve a purpose
  - Also have instance attributes
  - Create several instances of the class and call its methods to demonstrate
{{% /fragment %}}

---

### Class activity: now make it individually

No teamwork; change example below (not just the strings!):
- create a new class, add one new method
- have default parameters in constructor to set instance attributes
- make use of class attribute, show usage examples

```python
class Gunay:
  # class attributes
  classname = "python"
  school = "ggc"
  
  # constructor with instance attributes
  def __init__(self, firstname, lastname, pet, sport, vacation):
    self.firstname = firstname
    self.lastname = lastname
    self.pet = pet
    self.sport = sport
    self.vacation = vacation

  # additional method
  def greeting(self):
    print("Hello, I am " + self.firstname + " " + 
          self.lastname + " and I like " + self.sport +
          " while I am vacationing at " + self.vacation)
    print("I'm in the " + self.classname + " course at " + self.school + " like everyone else.")
```

<!--iframe height="500px" width="100%" src="https://repl.it/@cengique/objectoriented-sp22?lite=true#gunay.py" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe-->

---

### Inheritance and Polymorphism

- The last two [fundamental pillars of OOP](https://hyperskill.org/knowledge-map/1212)
- Inheritance: subclasses inherit methods and attributes
- Polymorphism: all subclasses can be used interchangably, regardless of implementation details

---

- Inheritance
- The `super()` method
- Overriding methods
- Decorators
- Abstract classes
- Multiple inheritance
- Polymorphism

---

### Class activity: polymorphism

- Teams of 2, pick a marker
- Write code on a board that includes:
  - A parent class and 2-3 child classes
  - Create parent class method to be *overloaded* in the children
  - Implement different versions of method in child classes
  - Use `super()` at least once
  - Demonstrate calling the method in children object instances to show different outcomes
  - Must have a meaning!

---

### Class activity: inherit!

Work individually, follow instructions:
- Create a subclass of the `PythonClass` below
- Use the `super()` method in your constructor
- Add any additional attributes into your class about yourself
- Modify the `__str__` method to compose a message about yourself
- Finish by creating an instance of your class
- Call the `__str__` method with your instance

```python
class PythonClass:
  school = "GGC"
  degree = "IT"
  classname = "ITEC 3160"
  members = []

  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname
    self.member = "student"
    PythonClass.members.append(self)

  def __str__(self):
    return self.fname + " " + self.lname + " (" + self.member + ")"
```

<!--iframe height="500px" width="100%" src="https://repl.it/@cengique/objectoriented-inheritance-sp22?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe-->
