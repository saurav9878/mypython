# Suppose we want to swap elements of a list then, we can use the
# following way of swap in python instead of using a conventional
# temp variable of C/C++

# Swap 3rd and 5th element
L = [1, 2, 3, 5, 7]
L[2], L[4] = L[4], L[2]

print L
