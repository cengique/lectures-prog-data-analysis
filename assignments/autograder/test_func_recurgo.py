import shell 
import unittest
import os
import sys
from gradescope_utils.autograder_utils.decorators import weight, number
from gradescope_utils.autograder_utils.files import check_submitted_files
from random import randint, shuffle

def test():
	print("test")

class TestFuncRecurgo(shell.TestShell):

	def setUp(self):
		self.py_asg_file = 'recurgo.py'
		super().setUp()

	def run(self, same_input):
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

	@weight(3)
	@number("1")
	def test_0step(self):
		"""Test 0 inputs"""
		self.run("done\n")
		
	@weight(3)
	@number("2")
	def test_1step(self):
		"""Test 1 inputs"""
		self.run("1\ndone\n")

	@weight(3)
	@number("3")
	def test_2step(self):
		"""Test 2 inputs"""
		self.run("3\n2\ndone\n")
		
	@weight(3)
	@number("4")
	def test_nstep(self):
		"""Test 10 inputs"""
		inputs = "\n".join([ str(randint(1, 3)) for i in range(10) ]) + "done\n"		
		self.run(inputs)

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
        
