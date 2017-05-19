# We put a , (comma) at the end of each print
# line. This is so print doesn't end the
# line with a newline character and go to the next line.
# comma is used to do the next task in same line
print "How old are you?",
# raw_input() is used to get input
# int(raw_input()) to get number input
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
   age, height, weight)
# inside raw_input we can pass string to display and get input from same
feeling = raw_input("WOW!!!!")
print feeling

# input() will try to get input as if they were Python code. -> avoid using it
