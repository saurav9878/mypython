# Composition
class Other(object):

    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit()"

    def altered(self):
        print "OTHER altered()"

        
class Child(object):

    def __init__(self):
        self.other = Other()  # while defining variables inside funcn
        # in class use self always to differentiate it from local
        # variables

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"

        
son = Child()

son.implicit()
son.override()
son.altered()
