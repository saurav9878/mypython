# Modules give us various features to use in our script
# sys is a module here
# argv is argument variable(passed while running script)
# values are assigned in sequencial way

# python ex13.py "Hello" 'India' 13 is the way to run this script
# parameters passed from terminal are strings even if you type numbers
# use int() to typecast them to integer
# user input is always string we have to always typecast them to integer
# for calulations. e.g. int(raw_input())

from sys import argv
# first parameter is always script name
script, first, second, third = argv

print "The first script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
