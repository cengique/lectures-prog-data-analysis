import shell 
import unittest
import os
from gradescope_utils.autograder_utils.decorators import weight, number
from gradescope_utils.autograder_utils.files import check_submitted_files
from random import randint, shuffle

class TestPetYoshi(shell.TestShell):

	def setUp(self):
		self.py_asg_file = 'petYoshi.py'
		super().setUp()


	@weight(3)
	@number("1")
	def test_func(self):
		"""Test Func"""
		try:
			from petYoshi import petYoshi
			a, b = (True, True)
			stud = petYoshi(a, b)
			sol = sol_petYoshi(a, b)
			self.assertFuncsEqual(stud, sol, "petYoshi(%s, %s)" % (repr(a), repr(b)))
		except ImportError:
			self.fail("Missing Function petYoshi")

	@weight(3)
	@number("2")
	def test_func2(self):
		"""Test Func"""
		try:
			from petYoshi import petYoshi
			a, b = (True, False)
			stud = petYoshi(a, b)
			sol = sol_petYoshi(a, b)
			self.assertFuncsEqual(stud, sol, "petYoshi(%s, %s)" % (repr(a), repr(b)))
		except ImportError:
			self.fail("Missing Function petYoshi")

	@weight(3)
	@number("3")
	def test_func3(self):
		"""Test Func"""
		try:
			from petYoshi import petYoshi
			a, b = (False, True)
			stud = petYoshi(a, b)
			sol = sol_petYoshi(a, b)
			self.assertFuncsEqual(stud, sol, "petYoshi(%s, %s)" % (repr(a), repr(b)))
		except ImportError:
			self.fail("Missing Function petYoshi")

	@weight(4)
	@number("4")
	def test_func4(self):
		"""Test Func"""
		try:
			from petYoshi import petYoshi
			a, b = (False, False)
			stud = petYoshi(a, b)
			sol = sol_petYoshi(a, b)
			self.assertFuncsEqual(stud, sol, "petYoshi(%s, %s)" % (repr(a), repr(b)))
		except ImportError:
			self.fail("Missing Function petYoshi")

#SOLUTION BELOW
def sol_petYoshi(a, b):
	return a and not b