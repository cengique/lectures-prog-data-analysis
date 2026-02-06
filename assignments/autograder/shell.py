import unittest
import os
from gradescope_utils.autograder_utils.decorators import weight, number
from gradescope_utils.autograder_utils.files import check_submitted_files

class TestShell(unittest.TestCase):
	def setUp(self):
		# by default on assert failures, only show the specified msg string
		self.longMessage = False
	
	def has_correct_file(self):
		missing_files = check_submitted_files([self.py_asg_file], base=".")
		return (len(missing_files) == 0)

	def get_shell_output(self, py_file, input_str):
		if not self.has_correct_file():
			self.skipTest("File Not Found")
		with open("input.txt", "w") as f: f.write(input_str)
		os.system("python3 %s < input.txt > output.txt" % py_file)
		with open("output.txt") as f: return f.read()

	def get_shell_output_from_stuff(self, py_file, input_str):
		if not self.has_correct_file():
			self.skipTest("File Not Found")
		with open("stuff.txt", "w") as f: f.write(input_str)
		os.system("python3 %s > output.txt" % py_file)
		with open("output.txt") as f: return f.read()

	#NOTE: There are no newlines in stud, sol so better parsing comparison is VERY difficult.
	def assertEqualShellOutput(self, stud, sol, msg=None):
		emsg = ("Output Mismatch\n"
			"Correct Output: %s"
			"   Your Output: %s\n\n" % (sol, stud))
		if msg != None:
			emsg += msg
		else:
			emsg += "NOTE: User Input is hidden." 

		self.assertEqual(stud.strip(), sol.strip(), emsg)

	def assertInShellOutput(self, stud, input_str, check_str):
		self.assertIn(str(check_str), stud, 
			"\nGiven input:\n%s\n"
			"Correct Output Must Contain: %s\n"			
			"Your Output\n###########\n%s\n\n" % (
			input_str, check_str, stud))

	def assertFuncsEqual(self, stud, sol, func_str):
		self.assertEqual(stud, sol, 
			"\nGiven Function Call: %s\n"
			"Correct Return Value: %s\n"			
			"   Your Return Value: %s\n\n" % (			
			func_str, repr(sol), repr(stud)))

	def assertClassEqual(self, stud, sol, obj_str, expr_str):
		self.assertEqual(stud, sol, 
			"\nGiven Object: %s\n"
			"    Expression: %s\n"
			" Correct Value: %s\n"			
			"    Your Value: %s\n\n" % (			
			obj_str, expr_str, repr(sol), repr(stud)))
			
	@weight(0)
	@number("0")
	def test_submitted_files(self):
		"""Check Correct File Name"""
		self.assertTrue(self.has_correct_file(), 
			'Missing %s! Must match the filename exactlty.' % self.py_asg_file)


