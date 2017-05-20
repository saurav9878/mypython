# Implicit Inheritance
class Parent(object):

    def implicit(self):
        print "PARENT implicit()"

        
class Child(Parent):
    pass  # pass keyword is used to pass the flow of control


dad = Parent()
son = Child()

dad.implicit()
son.implicit()
