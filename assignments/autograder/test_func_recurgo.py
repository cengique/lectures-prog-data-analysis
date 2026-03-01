import shell 
import unittest
import os
import sys
from gradescope_utils.autograder_utils.decorators import weight, number
from gradescope_utils.autograder_utils.files import check_submitted_files
from random import randint, shuffle

class TestFuncRecurgo(shell.TestShell):
        """
Assg 5: Exceptions and recursion (due midnight Fri Feb 27)
        
Do all of the following in a Python file named “**recurgo.py**” and submit your code file via the Gradescope link on D2L under assignment 5. **Do not leave any of your testing code!** Only submit the function itself.

1.  Write a recursive function “go” that takes no parameters.
2.  Inside the function, ask for a user input with the prompt **"Enter direction (1 for left, 2 for straight, 3 for right, and done to stop): "** (note space at the end)
3.  For each of the number answers, the function should first indicate the direction by printing **“Went !”**, call itself recursively, and then print the opposite direction (right, back, left).
4.  If the user enters “done”, it should cause an error in converting the input to a number and cause an exception. The exception should be handled and the function should print **“Arrived, returning!”** and then **return**.

The resulting program should be able to take a list of directions and then return through the same path with inverse instructions. Exception handling is used as the termination condition of recursion.

**Examples:**

Running the function with one input of “1” should result in going left and then going right to return to where you started:

```

>> go()
Enter direction (1 for left, 2 for straight, 3 for right, and done to stop): 1
Went left!
Enter direction (1 for left, 2 for straight, 3 for right, and done to stop): done
Arrived, returning!
Went right!
```

Running the function with two inputs of “1” and “2” should result in:

```

>> go()
Enter direction (1 for left, 2 for straight, 3 for right, and done to stop): 1
Went left!
Enter direction (1 for left, 2 for straight, 3 for right, and done to stop): 2
Went straight!
Enter direction (1 for left, 2 for straight, 3 for right, and done to stop): done
Arrived, returning!
Went back!
Went right!
```
        """

	def setUp(self):
		self.py_asg_file = 'recurgo.py'
		super().setUp()

	def rungo(self, same_input):
		"""Test given input"""
		try:
			from recurgo import go as stud_go
			local_go = locals()
			local_go["go"] = go # Add local function
			stud = self.get_eval_output("stud_go()", locals(), input_str=same_input)
			sol  = self.get_eval_output("go()", local_go, input_str=same_input)
			self.assertEqualShellOutput(stud, sol,
                                                    msg="Output mismatch.")
		except:
			raise

	@weight(5)
	@number("1")
	def test_0step(self):
		"""Test 0 inputs"""
		self.rungo("done\n")
		
	@weight(5)
	@number("2")
	def test_1step(self):
		"""Test 1 inputs"""
		self.rungo("1\ndone\n")

	@weight(5)
	@number("3")
	def test_2step(self):
		"""Test 2 inputs"""
		self.rungo("3\n2\ndone\n")
		
	@weight(5)
	@number("4")
	def test_nstep(self):
		"""Test 10 inputs"""
		inputs = "\n".join([ str(randint(1, 3)) for i in range(10) ]) + "done\n"		
		self.rungo(inputs)

#SOLUTION BELOW 
def go():
        try:
                user = input("Enter direction (1 for left, 2 for straight, 3 for right, and done to stop): ")
                num = int(user)
                if num == 1:
                        print("Went left!")
                        go()
                        print("Went right!")
                elif num == 2:
                        print("Went straight!")
                        go()
                        print("Went back!")
                elif num == 3:
                        print("Went right!")
                        go()
                        print("Went left!")
        except ValueError:
                print("Arrived, returning!")
                return
        
