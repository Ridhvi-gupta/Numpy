# Slicing using Numpy
import numpy as np

array = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12],
                 [13, 14, 15, 16]])  # Creating a 2-dimensional array (4x4 matrix)

# For array slicing, we will use subscript operator [start:end:step] where start is the starting index, end is the ending index (exclusive), and step is the step size.
# array[start:end:step]

# print(array[0])  # Output: [1 2 3 4] - Accessing the first row
# print(array[1])  # Output: [5 6 7 8] - Accessing the second row
# print(array[2])  # Output: [9 10 11 12] - Accessing the third row
# print(array[3])  # Output: [13 14 15 16] - Accessing the fourth row
# print(array[4])  # This will raise an IndexError because index 4 is out of bounds for axis 0 with size 4
# print(array[-1])  # Output: [13 14 15 16] - Accessing the last row using negative indexing
# print(array[-2])  # Output: [9 10 11 12] - Accessing the second last row using negative indexing
# print(array[0:2])  # Output: [[1 2 3 4] [5 6 7 8]] - Accessing the first two rows
# print(array[0:3]) # Output: [[ 1  2  3  4] [ 5  6  7  8] [ 9 10 11 12]] - Accessing the first three rows
# print(array[1:4]) # Output: [[ 5  6  7  8] [ 9 10 11 12] [13 14 15 16]] - Accessing rows from index 1 to 3
# print(array[:])  # Output: entire array - Accessing all rows
# print(array[1:])  # Output: [[ 5  6  7  8] [ 9 10 11 12] [13 14 15 16]] - Accessing all rows from index 1 to the end
# print(array[:3])  # Output: [[1 2 3 4] [5 6 7 8] [9 10 11 12]] - Accessing all rows from the start to index 2

# print(array[0:4:2])  # Output: [[ 1  2  3  4] [ 9 10 11 12]] - Accessing every second row from index 0 to 3
# print(array[::2])  # Output: [[ 1  2  3  4] [ 9 10 11 12]] - Accessing every second row from the entire array

# print(array[2]) # Output: [ 9 10 11 12] - Accessing the third row , if we omit colons numpy thinks we are selecting the second index
# print(array[::-1]) # Output: [[13 14 15 16] [ 9 10 11 12] [ 5  6  7  8] [ 1  2  3  4]] - Reversing the rows of the array
# print(array[::-2]) # Output: [[13 14 15 16] [ 9 10 11 12]] - Accessing every second row in reverse order

## Accessing columns with 2 indices
# print(array[0, 0])  # Output: 1 - Accessing the first element of the first row (first column)
# print(array[, 0])  # Output: Inavlid syntax - This will raise a SyntaxError
# print(array[:, 0])  # Output: [ 1  5  9 13] - Accessing the first column
# print(array[:, 1])  # Output: [ 2  6 10 14] - Accessing the second column
# print(array[:, 2])  # Output: [ 3  7 11 15] - Accessing the third column
# print(array[:, 3])  # Output: [ 4  8 12 16] - Accessing the fourth column
# print(array[:, -1])  # Output: [ 4  8 12 16] - Accessing the last column using negative indexing)
# print(array[:, -2])  # Output: [ 3  7 11 15] - Accessing the second last column using negative indexing

print(array[:, 0:3]) # Output: [[ 1  2  3] [ 5  6  7] [ 9 10 11] [13 14 15]] - Accessing the first three columns
print(array[:, 1:4])  # Output: [[ 2  3  4] [ 6  7  8] [10 11 12] [14 15 16]] - Accessing columns from index 1 to 3
print(array[:, 1:]) # Output: [[ 2  3  4] [ 6  7  8] [10 11 12] [14 15 16]] - Accessing columns from index 1 to 3
print(array[:, :])  # Output: entire array - Accessing all columns
print(array[:, ::2])  # Output: [[ 1  3] [ 5  7] [ 9 11] [13 15]] - Accessing every second column
print(array[:, 1::2])  # Output: [[ 2  4] [ 6  8] [10 12] [14 16]] - Accessing every second column starting from index 1
print(array[:, ::-1])  # Output: [[ 4  3  2  1] [ 8  7  6  5] [12 11 10  9] [16 15 14 13]] - Reversing the columns of the array
print(array[:, ::-2])  # Output: [[ 4  2] [ 8  6] [12 10] [16 14]] - Accessing every second column in reverse order

# Both row and column selection
print(array[0:2, 0:2])  # Output: [[1 2] [5 6]] - Accessing a sub-array from the first two rows and first two column
print(array[0:2, 2:])  # Output: [[3 4] [7 8]] - Accessing a sub-array from the first two rows and last two columns
print(array[2:, 0:2])  # Output: [[ 9 10] [13 14]] - Accessing a sub-array from the last two rows and first two columns


 

