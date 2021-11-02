import numpy as np

matrix_A = np.matrix('3 -4 1; -4 8 -4; 1 -4 3')
matrix_B = np.matrix('1; 0; 0')

print (matrix_A)
print (matrix_B)
A = matrix_A**10
print (A)
total = (A) * matrix_B

print (total)
