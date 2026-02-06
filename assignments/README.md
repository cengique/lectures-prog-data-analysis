
# ITEC 2120 Introduction to Programming - Python autograder scripts for Gradescope

## Create

To create a new autograder script:

1. Go to the `autograder_framework/tests/` directory.
2. Copy the `test_shell_yellow_fruit.py` file and give the copy a similar name (must start with `test_`)
3. Modify the script following the python3 unittest conventions.
4. Come back to this directory and run the make_autograder.sh script
   with the name of your new script **without the trailing .py**
    Example:
    ```
    ./make_autograder.sh test_shell_yellow_fruit
    ```

## Test locally

To test and run the autograder script locally, create a test environment:

1. cd into the `autograder_framework/tests` directory.
2. create a `.env` folder
3. run `python -m venv .env/` to create a new virtual environment
4. run `.env/bin/pip install gradescope_utils` to install the GradeScope module inside the environment
5. Optional: run `.env/bin/python -m ipython` to have IPython accessible

Once you have the test environment, run solution and test functions by:

1. cd into the `autograder_framework/tests` directory.
1. run `.env/bin/ipython` (if available) or `.env/bin/python` to enter the Python environment
1. import your new test by running `import test_... as xx` where `test_...` is the new file you created and `xx` is an abbreviation to refer to it

## Test with Docker

To run the test suite in a Docker environment similar to that on Gradescope:

1. `cd` into the `autograder_framework` directory.
1. Build your Docker image with `sudo docker build -t gradescope2120 .` (sudo is optional).
1. Create a `tmp` folder and inside it, unzip the autograder zip file you created above.
1. Run your image by mounting three volumes. Make sure to provide the full path. Note that 
   we mount the `tmp` and `tmp/tests` folders separately.
   ```bash
   sudo docker run --rm \
                   -v /path/to/submission/files:/autograder/submission \
	               -v /path/to/tmp:/autograder/results \
				   -v /path/to/tmp/tests:/autograder/source/tests \
				   gradescope2120 /autograder/run_autograder
   ```
1. You will find a `results.json` file under your `tmp` folder

See [Gradescope site](https://gradescope-autograders.readthedocs.io/en/latest/manual_docker/) for details.
