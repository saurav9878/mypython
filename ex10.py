# Escape Sequences: \\,\n,\t

# An important escape sequence is to escape
# a single-quote ' or double-quote ". Imagine
# you have a string that uses double-quotes and
# you want to put a double-quote inside the string.
# If you write "I "understand" joe." then Python
# will get confused because it will think
# the " around "understand" actually ends
# the string. You need a way to tell Python that
# the " inside the string isn't a real double-quote.

tabby_cat = "\tI'm tabbed in."
# \t for horizontal tabbing
persian_cat = "I'm split\non a line."
# \\ is actually a single backslash(\) rather than double backslash
backslash_cat = "I'm \\ a \\ cat."
# """(triple double quotes) can always be replaced by '''
# It doesn't matter whatever you use
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


# %r -> used for Debugging
# %s -> used for Displaying
