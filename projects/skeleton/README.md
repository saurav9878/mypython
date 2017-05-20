## Install the following Python packages:

1. pip from http://pypi.python.org/pypi/pip
2. distribute from http://pypi.python.org/pypi/distribute
3. nose from http://pypi.python.org/pypi/nose/
4. virtualenv from http://pypi.python.org/pypi/virtualenv

## Final Directory Structure

When you are done setting all of this up, your directory should look like mine here:
```
skeleton/
     NAME/
         __init__.py
     bin/
     docs/
     setup.py
     tests/
         NAME_tests.py
         __init__.py
```
And from now on, you should run your commands from that work with this directory 
from this point. If you can't do ls -R and see the same structure, then you are 
in the wrong place. For example, people commonly go into the tests/ directory to
try to run files there, which won't work. To run your application's tests, you
would need to be above tests/ and this location I have above. So, if you try this:
```
$ cd tests/   # WRONG! WRONG! WRONG!
$ nosetests

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
```
### Then that is wrong! You have to be above tests, so assuming you made this mistake, you would fix it by doing this:
```
$ cd ..   # get out of tests/
$ ls      # CORRECT! you are now in the right spot
NAME                bin             docs            setup.py        tests
$ nosetests
.
----------------------------------------------------------------------
Ran 1 test in 0.004s

OK
```

## Using the Skeleton


1. Make a copy of your skeleton directory. Name it after your new project.
2. Rename (move) the NAME directory to be the name of your project or 
   whatever you want to call your root module.
3. Edit your setup.py to have all the information for your project.
4. Rename tests/NAME_tests.py to also have your module name.
5. Double check it's all working by using nosetests again.
6. Start coding.

Q. Why do we need a bin/ folder at all?
	This is just a standard place to put scripts that are run on the
	command line, not a place to put modules.
