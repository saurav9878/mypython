### Tuples

A tuple is nothing more than a list that you can't modify. It's
created by putting data inside two () with a comma, like a list:

first_word = ('verb', 'go')
second_word = ('direction', 'north')
third_word = ('direction', 'west')
sentence = [first_word, second_word, third_word]

This creates a pair (TYPE, WORD) that lets you look at the word and do things with it.

This is just an example, but that's basically the end result. You want to take
raw input from the user, carve it into words with split, analyze those words
to identify their type, and finally make a sentence out of them.
