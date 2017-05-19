formatter = "%r %r %r %r"
# never use %r for displaying strings as printing with
# %r will lead to printing with single/double quotes
# so, instead of %r , always use %s for displaying
# strings
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type right.",
    "But it didn't sing.",
    "So I said goodnight."
    )
