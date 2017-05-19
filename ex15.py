from sys import argv

script, filename = argv
# open() function is used to open file and assign
# file to an object
txt = open(filename)

print "Here's your file %r:" % filename
# variable_name.read() reads the data stored in file.
print txt.read()
# Python allows you to open same file multiple times
print "Type the filename again :"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
# close() function closes the file
txt_again.close()
