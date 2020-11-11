def RotateMatrix(matrix):
    length = len(matrix)
    matrix.reverse()
    for i in range(length):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    print(matrix)






a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

RotateMatrix(a)