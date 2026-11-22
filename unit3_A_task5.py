A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print("Addition:")
for i in range(2):
    print([A[i][j] + B[i][j] for j in range(2)])

print("Subtraction:")
for i in range(2):
    print([A[i][j] - B[i][j] for j in range(2)])

print("Multiplication:")
for i in range(2):
    print([sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)])