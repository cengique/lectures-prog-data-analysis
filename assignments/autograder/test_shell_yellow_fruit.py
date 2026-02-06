import shell 
import unittest
import os
from gradescope_utils.autograder_utils.decorators import weight, number
from gradescope_utils.autograder_utils.files import check_submitted_files
from random import randint, shuffle

class TestYellowFruit(shell.TestShell):

	def setUp(self):
		self.py_asg_file = 'fruit.py'
		super().setUp()

	@weight(5)
	@number("1")
	def test_lemon(self):
		"""Test lemon"""

		fruit = 'lemon'
		
		input_str = "%s\n" % (fruit)
		stud = self.get_shell_output(self.py_asg_file, input_str)
		sol = self.get_shell_output(__file__, input_str)
		
		self.assertEqualShellOutput(stud, sol)		
	
	@weight(5)
	@number("2")
	def test_banana(self):
		"""Test banana"""

		fruit = 'banana'
		
		input_str = "%s\n" % (fruit)
		stud = self.get_shell_output(self.py_asg_file, input_str)
		sol = self.get_shell_output(__file__, input_str)
		
		self.assertEqualShellOutput(stud, sol)		

	@weight(5)
	@number("3")
	def test_orange(self):
		"""Test orange"""

		fruit = 'orange'
		
		input_str = "%s\n" % (fruit)
		stud = self.get_shell_output(self.py_asg_file, input_str)
		sol = self.get_shell_output(__file__, input_str)
		
		self.assertEqualShellOutput(stud, sol)		

	@weight(5)
	@number("4")
	def test_random(self):
		"""Test random"""

		fruits = ["apple", "apricot", "avocado", "banana", "boysenberry", 
		"blueberry", "cherry", "cantaloupe", "clementine", "cucumber", "plum", 
		"date", "dewberry", "elderberry", "huckleberry", "fig", "lemon"]
		
		input_str = "%s\n" % (fruits[randint(0, len(fruits) - 1)])
		stud = self.get_shell_output(self.py_asg_file, input_str)
		sol = self.get_shell_output(__file__, input_str)
		
		self.assertEqualShellOutput(stud, sol)		


#SOLUTION BELOW (note students do not need if main statement)
if __name__ == "__main__":
	f = input("What is your favorite fruit? ")
	if f == 'lemon' or f == 'banana':
		print("Indeed, yellow fruit are the best!")
	print("Fruit is good for you.")
		
