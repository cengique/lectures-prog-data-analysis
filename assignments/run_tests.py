"""
import unittest
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('tests')
    with open('/autograder/results/results.json', 'w') as f:
        JSONTestRunner(visibility='visible', stream=f, 
	        stdout_visibility='hidden').run(suite)
"""
import unittest
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner

# due to bug in gradescope to codio markdown converter.
def remove_score_post_processor(data):
	# test if all scores of tests total to 0.
	if sum([float(test['score']) for test in data['tests']]) == 0:
		return # don't delete global score attribute

	if "score" in data: 
		del data["score"] # delete global score attribute
		return 

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('tests')
    with open('/autograder/results/results.json', 'w') as f:
        JSONTestRunner(
            visibility='visible', 
            stdout_visibility="visible", 
            stream=f, 
            post_processor=remove_score_post_processor
        ).run(suite)
