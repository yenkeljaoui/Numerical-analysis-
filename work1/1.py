import numpy as np





def reversematrix(revers_matrix):
    i = rows - 1
    j = 0
    elementary = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    count = 0
    while True:
        if i != j:
            identity_matrix = np.eye(3)
            element = (-revers_matrix[i, j] / revers_matrix[j, j])
            identity_matrix[i, j] = element

            revers_matrix = np.dot(identity_matrix, revers_matrix)
            if count == 0:
                elementary = np.dot(revers_matrix, elementary)
                count += 1
            else:
                elementary = np.dot(elementary, revers_matrix)
            i -= 1

        if i == j:
            if j == columns - 1:
                break
            i = rows - 1
            j += 1

    i = 0
    j = columns - 1
    while True:
        if i != j:
            identity_matrix = np.eye(3)
            element = (-revers_matrix[i, j] / revers_matrix[j, j])
            identity_matrix[i, j] = element
            revers_matrix = np.dot(identity_matrix, revers_matrix)
            elementary = np.dot(elementary, revers_matrix)

            i += 1
        if i == j:
            if j == 0:
                break
            i = 0
            j -= 1


def func_norma(matrix):
    arr = []
    sum = 0
    for i in range(rows):
        for j in range(columns):
            x = abs(matrix[i, j])
            sum = sum + x
        arr.append(sum)
        sum = 0

    print(arr)
    return max(arr)


matrix = np.array([[1, -1, -2], [2, -3, -5], [-1, 3, 5]])
rows, columns = matrix.shape
print(matrix)
if np.linalg.det(matrix) != 0:
    reversematrix(matrix)

norma = func_norma(matrix)
