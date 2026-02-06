#!/usr/bin/env bash

if [ -z "$1" ]; then
	echo "Usage: $0 autograder/test.py"
	exit -1
fi

# Ex: ./make_autograder.sh test_shell_yellow_fruit
# or make all with> for i in autograder_framework/tests/test_*.py; do f=$(basename $i .py); ./make_autograder.sh $f; done

# or redo all with> for i in *zip; do x=`echo $i | sed 's/_autograder.zip//'`; ./make_autograder.sh $x; done

test_name=$(basename $1 .py)

zip -r ${test_name}_autograder.zip setup.sh run_autograder run_tests.py requirements.txt autograder/__init__.py autograder/shell.py $1

