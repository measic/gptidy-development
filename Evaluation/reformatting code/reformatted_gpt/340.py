## Example
A = np.array([[1, 0, 0],
              [4, 5, 0],
              [7, 8, 9]])

b = np.array([1, 2, 3])

## solve system
x = forward_sub(A, b)
print(x)