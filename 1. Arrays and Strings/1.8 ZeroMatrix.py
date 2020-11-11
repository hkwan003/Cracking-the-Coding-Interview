

def ZeroMatrix(matrix):
    rows = set()
    column = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.add(i)
                column.add(j)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in rows or j in column:
                matrix[i][j] = 0


    print(matrix)



a = [[1,2,3],
     [4,0,6],
     [7,8,9]]

ZeroMatrix(a)