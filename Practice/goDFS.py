def IsAlive(x, y, board):

    index = y* 19 + x
    frontier = [index]
    visited = set()

    def checkAlive(index):
        if index in visited:
            return False

        visited.add(index)

        x = index % 19
        y = index / 19

        print x, y, index

        if board[index] == 2:
            return False

        if board[index] == 0:
            return True

        print "connect"


        if x > 0:
            if checkAlive(index - 1):
                return True
        if x < 18:
            if checkAlive(index + 1):
                return True
        if y > 0:
            if checkAlive(index - 19):
                return True
        if y < 18:
            if checkAlive(index + 19):
                return True

        return False
        
    return checkAlive(index)

board = [0] * 19 * 19

board[20] = 1
board[1] = 2
board[19] = 2
board[21] = 2
board[39] = 1
board[58] = 1

print board

print IsAlive(1, 1, board)


def IsAliveStack(x, y, board):
    index = y * 19 + x

    visited = set()    
    visited.add(index)

    unvisited = [index]

    while unvisited:
        index = unvisited.pop()
        
        x = index % 19
        y = index / 19

        if x > 0:            
            nb = index - 1
            visited.add(index)
            if nb in visited:
                continue
            if board[nb] == 0:
                return True
            if board[nb] == 1:
                unvisited.append(nb)

        if x < 18:
            nb = index + 1
            visited.add(index)
            if nb in visited:
                continue
            if board[nb] == 0:
                return True
            if board[nb] == 1:
                unvisited.append(nb)

        if y > 0:
            nb = index - 19
            visited.add(index)
            if nb in visited:
                continue
            if board[nb] == 0:
                return True
            if board[nb] == 1:
                unvisited.append(nb)

        if y < 18:
            nb = index + 19
            visited.add(index)
            if nb in visited:
                continue
            if board[nb] == 0:
                return True
            if board[nb] == 1:
                unvisited.append(nb)

    return False

print IsAliveStack(1,1,board)