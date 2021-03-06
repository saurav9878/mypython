# Multidimentional Arrays
# 1D Array (Lists in Python)

myarray1 = [1, 2, 3, 4]

print myarray1[0]  # prints 1
print myarray1[-1]  # prints last element i.e. 4
print myarray1[-2]  # prints 2nd last element i.e. 3

# 2D Array

myarray2 = [[5, 4, 3, 2, 1], [2, 8, 9, 3, 5]]  # representing an 5*2 matrix

print myarray2[0][1]  # prints 4
print myarray2[1][2]  # prints 9

# 3D Array

myarray3 = [[[3, 2], [0, 8], [2, 5]], [[5, 4], [9, 7], [1, 8]]]
# representing a 3d matrix of dimension (2, 2, 3)
# First dimension represents its a list with 2 elements
# Rest two dimension represents that it is 2*3 Matrix
# Finally It is a list having 2 elements of which both elements are 2*3 Matrix

print myarray3[0][1][0]
