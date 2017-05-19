def break_words(stuff):
    """This function will break up words for us."""
# split function split string into a list and
# parameter is always a space character
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sorts the words."""
# sorted() function sorts the letters in a string
# and returns the list of sorted letters(letters can be repeated in list)
    return sorted(words)


def print_first_word(words):
    """Prints the first word after popping it off."""
# pop is a function used with list to return element at passed index
# pop bydefault returns element at last index
    word = words.pop(0)
    print word

    
def print_last_word(words):
    """Prints the last word after popping it off."""
# pop() same as pop(-1)
    word = words.pop(-1)
    print word


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and the last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print break_words("Hey dude")
# it will break a sentence of strings into a list of words of that sentence
print sort_words("I am happy")
print_last_word(["appy", 'mango'])
print sort_sentence("I am happy")
