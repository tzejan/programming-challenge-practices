"""
Board of 19 x 19
No seed = 0
Black = 1
White = 2

"""

def IsAlive(x, y, board):
    #breath first search
    index = y * 19 + x
    frontier = [index]
    next = []
    visited = set()

    def query(index, nextIndexes, visited):
        if index in visited:
            return False
        visited.add(index)
        
        if board[index] == 0:
            return True
        if board[index] == 1:
            nextIndexes.append(index)
        
        return False

    if board[index] != 1:
        return False

    while frontier:
        nextIndexes = []
        for index in frontier:
            x = index % 19
            y = index / 19           

            #check  left
            if x > 0:
                if query(index-1, nextIndexes, visited):
                    return True

            #check right
            if x < 18:
                if query(index+1, nextIndexes, visited):
                    return True

            #check up
            if y > 0:
                if query(index-19, nextIndexes, visited):
                    return True

            #check down
            if y < 18:
                if query(index+19, nextIndexes, visited):
                    return True

        frontier = nextIndexes
    return False


board = [0] * 19 * 19

board[20] = 1
board[1] = 2
board[19] = 2
board[21] = 2
board[39] = 1

print board

print IsAlive(1, 1, board)