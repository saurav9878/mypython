ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."
# creating a list of words in string using split(' ') function
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    # pop from last as no index passed
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    # len(stuff) returns length of list.
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]  # -1 index gives last element in list
print stuff.pop()  # pop last element
print ' '.join(stuff)  # exactly opposite to that of split function
print '#'.join(stuff[3:5])

# stuff[3:5] extracts a "slice" from the stuff list that is from
# element 3 to element 4, meaning it does not include element 5.
# It's similar to how range(3,5) would work.


# range (1, 7) means 1 to 6 (not 7)
