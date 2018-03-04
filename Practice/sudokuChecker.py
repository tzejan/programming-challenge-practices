def solvedSudoku(puzzle):
    if len(puzzle) != 81:
        return False

    #check rows and cols
    for j in range(9):
        sumRow = 0
        sumCol = 0
        for i in range(9):
            sumRow += puzzle[9 * j + i]
            sumCol += puzzle[9 * i + j]

        if sumRow != 45:
            print "Row ", j
            return False
        if sumCol != 45:
            print "Col ", j
            return False

    # check boxes
    relIndex = [0, 1, 2, 9, 10, 11, 18, 19, 20]
    startingIndex = [0, 3, 6, 27, 30, 33, 54, 57, 60]

    for si in startingIndex:        
        sumBox = 0
        for i in range(9):
            sumBox += puzzle[si + relIndex[i]]

        if sumBox != 45:
            print "Box ", si
            return False

    return True



puzzle = [8, 3, 1, 6, 7, 2, 4, 9, 5, 9, 4, 2, 8, 3, 5, 6, 1, 7, 5, 6, 7, 9, 4, 1, 3, 8, 2, 2, 8, 4, 1, 5, 6, 7, 3, 9, 3, 5, 9, 7, 2, 4, 1, 6, 8, 1, 7, 6, 3, 8, 9, 2, 5, 4, 6, 9, 5, 4, 1, 7, 8, 2, 3, 4, 1, 8, 2, 9, 3, 5, 7, 6, 7, 2, 3, 5, 6, 8, 9, 4, 1,]
puzzle = [3, 2, 8, 6, 9, 4, 7, 5, 1, 7, 6, 4, 8, 5, 1, 2, 3, 9, 9, 1, 5, 3, 2, 7, 6, 8, 4, 1, 4, 9, 2, 8, 6, 3, 7, 5, 2, 8, 3, 7, 4, 5, 9, 1, 6, 5, 7, 6, 1, 3, 9, 8, 4, 2, 8, 5, 1, 9, 7, 2, 4, 6, 3, 6, 9, 7, 4, 1, 3, 5, 2, 8, 4, 3, 2, 5, 6, 8, 1, 9, 7,]

print solvedSudoku(puzzle)