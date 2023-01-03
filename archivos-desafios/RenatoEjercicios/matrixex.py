def getSpiralMatrix(InputMatrix):
    result = []
    if len(InputMatrix)==0:
        return result
    row_begin = 0
    row_end = len(InputMatrix) -1
    col_begin =0
    col_end= len(InputMatrix[0])-1

    while row_begin <= row_end and col_begin <= col_end:
        for i in range (col_begin,col_end+1):
            result.append(InputMatrix[row_begin][i])
        row_begin +=1

        for i in range (row_begin,row_end+1):
            result.append(InputMatrix[i][col_end])
        col_end -=1

        if row_begin <= row_end:
            for i in range (col_end,col_begin-1,-1):
                result.append(InputMatrix[row_end][i])
        row_end -=1

        if col_begin <= col_end:
            for i in range (row_end,row_begin-1,-1):
                result.append(InputMatrix[i][col_begin])
        col_begin +=1
    return result

    #matrix

matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]

print ("La Matrix: ",matrix)
print(getSpiralMatrix(matrix))
#1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 