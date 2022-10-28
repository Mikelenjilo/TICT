def createMatrix(n, dataList):
    matrix = []
    for i in range(n):
        Listrow = []
        for j in range(n):
            Listrow.append(dataList[n * i + j])
        matrix.append(Listrow)

    return matrix

let = [
        '0.25', '0.25', '0.25', '0.25', 
        '0.4', '0.2', '0.2', '0.2', 
        '0.1', '0.3', '0.5', '0.1', 
        '0.4', '0.4', '0.1', '0.1', 
        ]

matrix = createMatrix(4, let)

print(let)
print(matrix)

for i in range(len(matrix)):#Loop for access the row
    for j in range(len(matrix[i])):#Loop for accessing the column
        print("i = {}, j = {} => {}".format(i, j ,matrix[i][j])) #printing the each element
print()