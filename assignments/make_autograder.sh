#!/usr/bin/env bash

# Ex: ./make_autograder.sh test_shell_yellow_fruit
# or make all with> for i in autograder_framework/tests/test_*.py; do f=$(basename $i .py); ./make_autograder.sh $f; done

# or redo all with> for i in *zip; do x=`echo $i | sed 's/_autograder.zip//'`; ./make_autograder.sh $x; done

cd autograder_framework

zip -r $1_autograder.zip setup.sh run_autograder run_tests.py requirements.txt tests/__init__.py tests/shell.py tests/$1.py

mv $1_autograder.zip ../

cd ../
