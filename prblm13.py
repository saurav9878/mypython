from sys import argv

myscript, first, second = argv
second = int(second)
print "Hey! there"
print "What's your name: "
name = raw_input()
age = int(raw_input("Age:"))

print "Hello!! I'm %s age %d welcome %s age %d" % (first, second, name, age)
print "Script :- ", myscript
