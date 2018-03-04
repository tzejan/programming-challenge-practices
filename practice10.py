#rotate matrix

def rotate(M, N):

    def cti(x, y):
        return x + y * N

    halfN = N / 2 
    for x in range(halfN+1): 
        for y in range(1, halfN+1): #overlapping segment
            br = cti(halfN + x, halfN + y)
            bl = cti(halfN - y, halfN + x)
            tl = cti(halfN - x, halfN - y)
            tr = cti(halfN + y, halfN - x)

            temp = M[br]
            M[br] = M[tr]
            M[tr] = M[tl]
            M[tl] = M[bl]
            M[bl] = temp


def printMatrix(M, N):
    for i in range(N):
        print M[i*N:(i+1)*N]

width = 5
mat = [n for n in range(width*width)]

printMatrix(mat, width)
rotate(mat, width)
print ""
printMatrix(mat, width)