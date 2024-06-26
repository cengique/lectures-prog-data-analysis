+++
title = "Errors and Exceptions"
outputs = ["Reveal"]
weight = 45 # chapter number
+++

{{< reveal-titlepage >}}
  
---

### What are exceptions?

- A way to break out of the linear execution of a program
- Usually for an _exceptional_ situation (e.g., an error)
- Otherwise, it may cause your program to crash
- Why not instead use if statements to catch errors?

{{% fragment %}}
- Cleaner logic and execution, does not disrupt logic
- Exception may arise from multiple places
{{% /fragment %}}

---

### Examples with if statements vs exceptions

If statement:
```python
value = count_inputs(...)
if value < -1:
  print("Error in counting inputs!")
  exit -1
# now do stuff with value
...
```

{{% fragment %}}
Exception:
```python
try:
  value = count_inputs(...)
  # now do stuff with value
  ...
except:
  print("Error in counting inputs!")
  raise
```

{{% /fragment %}}

---

### Exceptions in Python

- All exceptions should be subclasses of `BaseException`
- Other options and examples below and in [official Python docs](https://docs.python.org/3/tutorial/errors.html)

```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
else:
    print("OMG no errors!")
finally:
    print("Error or not, I say this.")
```

---

### Exercise time

Individually or in teams, implement ONE of these by using exceptions:

1. `defaultdict` functionality by using the regular `dict`
1. Implement input validation (only numbers) with loops
1. Create a file if not already exists 

Attach runtime output screenshots showing valid and exception cases on submission site.
