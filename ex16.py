# Methods/Functions for data file handling:
# close() -> save & close the file
# read() -> read the file
# readline() -> read just one line of text file
# truncate() -> Empties the file.
# write('stuff') -> write 'stuff' to the file.

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit Ctrl-C (^C)."
print "If you do want that, hit RETURN."
# Its similar to getch() to hold the console
raw_input("?")

print "Opening the file..."
# open file in write mode by passing 'w' as 2nd parameter
# 'w' is file mode. Similarly other file modes are 'r' (read) by default
# then 'a' to append
# modifiers like + can be used with file modes
target = open(filename, 'w')

print "Truncating the file. GoodBye!"
# file truncating(emptying)
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to a file."
# write data to file.
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
