# Dictionaries
# it is like an unordered list
# syntax -> dict_name = { key: value, key:value, key: value}
# key can be used to access value but otherway round not possible
# e.g. dict_name[key] = value_stored_in_that_key
# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
    }

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
    }

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'PortLand'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
# items() function with dict_name will return tuples of
# keys and values
for state, abbrev in states.items():  # way to loop around dictionary
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by state that might not be there
# get("key") will return "value of that key" if it
# exists in dict else return None(False)
state = states.get('Texas')
if not state:
    print "Sorry, no Texas."

# get a city with a default value
# the second parameter of get() function is default value
# in case that key is not found in dictionary
city = cities.get('TX', 'Does not Exist')
print "The city for the state 'TX' is: %s" % city


# we can use del keyword to delete values along with keys in dict
# syntax -> del dict_name['key_name']
