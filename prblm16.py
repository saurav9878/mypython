from sys import argv

script, file1 = argv

myfile = open(file1)
target = open("copy.txt", 'w')

print "File selected is: %s" % file1
print "Ready for Copy....."
data = myfile.read()
target.write(data)
target.close()
print "Copy Done..."
target = open("copy.txt")
print target.read()
target.close()
