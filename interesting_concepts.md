##Classes in Python
What happened is Python's original rendition of class was broken in many serious ways.
By the time they admitted the fault it was too late, and they had to support it.
In order to fix the problem, they needed some "new class" style so that the "old classes"
would keep working but you could use the new more correct version.

This is where "class is-a object" comes in. They decided that they would use
the word "object," lowercased, to be the "class" that you inherit from to make a class.
Confusing, right? A class inherits from the class named object to make a class but it's
not an object really it's a class, but do not forget to inherit from object.

Exactly. The choice of one single word meant that I couldn't teach you about this until
now. Now you can try to understand the concept of a class that is an object if you like.

However, I would suggest you do not. Just completely ignore the idea of old style versus
new style classes and assume that Python always requires (object) when you make a class.
Save your brain power for something important.

For the meaning of "is-a" look over <a href= "Word drills.png">Word Drills </a> picture.

## Using super() inside class
'''python
class Mammal(object):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    
class Dog(Mammal):
  def __init__(self):
    print('Dog has four legs.')
    super().__init__('Dog')
    
d1 = Dog()
'''
'''
output: Dog has four legs.
        Dog is a warm-blooded animal.
'''
### No need the remember the name of base class to run methods
### That's how you can run the __init__ method of a parent(base) class reliably.
### Very useful in Multiple Inheritance:
'''python
class Animal:
  def __init__(self, animalName):
    print(animalName, 'is an animal.');

class Mammal(Animal):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    super().__init__(mammalName)
    
class NonWingedMammal(Mammal):
  def __init__(self, NonWingedMammalName):
    print(NonWingedMammalName, "can't fly.")
    super().__init__(NonWingedMammalName)

class NonMarineMammal(Mammal):
  def __init__(self, NonMarineMammalName):
    print(NonMarineMammalName, "can't swim.")
    super().__init__(NonMarineMammalName)

class Dog(NonMarineMammal, NonWingedMammal):
  def __init__(self):
    print('Dog has 4 legs.');
    super().__init__('Dog')
    
d = Dog()
print('')
bat = NonMarineMammal('Bat') 
'''
### When you run the program, the output will be:
'''
Dog has 4 legs.
Dog can't swim.
Dog can't fly.
Dog is a warm-blooded animal.
Dog is an animal.

Bat can't swim.
Bat is a warm-blooded animal.
Bat is an animal.
'''

## When to Use Inheritance or Composition

The question of "inheritance versus composition" comes down to an attempt to solve
the problem of reusable code. You don't want to have duplicated code all over your
software, since that's not clean and efficient. Inheritance solves this problem by
creating a mechanism for you to have implied features in base classes. 
Composition solves this by giving you modules and the ability to call functions in
other classes.

### Use composition to package code into modules that are used in many different
### unrelated places and situations.

### Use inheritance only when there are clearly related reusable pieces of code that
### fit under a single common concept or if you have to because of something you're using.other classes.
