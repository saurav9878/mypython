# use % to put values of formatted character inside string
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# paranthesis is used to display more than one variables.
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y
# %r is used to display whatever raw data to be printed as such.
# Use %r for debugging since it displays raw data
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."
# concatenation of sting by using + operator
print w + e
