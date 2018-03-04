#2D spiral


def spiral(n):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    r = 0
    c = 0

    direction = 0
    spiral_array = []
    for _ in xrange(n):
        spiral_array.append([0]*n)

    for i in xrange(1, n*n+1):
        spiral_array[r][c] = i
        r += dr[direction]
        c += dc[direction]
 

        if (r >= n or r < 0 or c >= n or c < 0 or spiral_array[r][c] > 0):
            r -= dr[direction]
            c -= dc[direction]

            direction = (direction + 1) % 4
            r += dr[direction]
            c += dc[direction]


    return spiral_array




















def spiral_old(n):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    #initialize 2D array
    spiral_array = []
    for _ in xrange(n):
        spiral_array.append([0] * n)
    r = 0
    c = 0
    dir = RIGHT
    for i in xrange(1, n*n+1):
        print r, c
        spiral_array[r][c] = i
        if dir == RIGHT:
            if c+1 >= n or spiral_array[r][c+1] > 0:
                dir = DOWN
        elif dir == DOWN:
            if r+1 >= n or spiral_array[r+1][c] > 0:
                dir = LEFT
        elif dir == LEFT:
            if c-1 < 0 or spiral_array[r][c-1] > 0:
                dir = UP
        elif dir == UP:
            if r-1 < 0 or spiral_array[r-1][c] > 0:
                dir = RIGHT

        if dir == LEFT:
            c -= 1
        elif dir == RIGHT:
            c += 1
        elif dir == UP:
            r -= 1
        elif dir == DOWN:
            r += 1

             


    return spiral_array


result = spiral(8)
for row in result:
    for num in row:
        print num,
    print ""