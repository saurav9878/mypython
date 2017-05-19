# Classes Are Like Modules


class MyStuff(object):  # object is keyword here and use assuch always
    # self is a pseudo object to work around inside class to keep its
    # variables look different from local variables.
    def __init__(self):  # __init__ function is constructor always
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print "I AM CLASSY APPLES!"


# Here's why classes are used instead of modules: You can take this
# MyStuff class and use it to craft many of them, millions at a
# time if you want, and each one won't interfere with each other.
# When you import a module there is only one for the entire program
# unless you do some monster hacks.


# Objects are Like Import

# If a class is like a "mini-module," then there has to be a
# similar concept to import but for classes. That concept is called
# "instantiate", which is just a fancy, obnoxious, overly smart way
# to say "create." When you instantiate a class what you get is
# called an object.

# You instantiate (create) a class by calling the class like it's
# a function, like this:

thing = MyStuff()
thing.apple()
print thing.tangerine


# Classes are like blueprints or definitions for creating new
# mini-modules.
# Instantiation is how you make one of these mini-modules and import
# it at the same time. "Instantiate" just means to create an object
# from the class.
# The resulting created mini-module is called an object and you then
# assign it to a variable to work with it.


# Getting Things from Things

# ***dict style***
# mystuff['apples']

# ***module style***
# mystuff.apples()
# print mystuff.tangerine

# ***class style***
# thing = MyStuff()
# thing.apples()
# print thing.tangerine
