
mat = [[1,2,3], [4,5,6], [7,8,9]]
mat = [[1,2], [3, 4]]

def get_anti(arr, N):
    result = []
    for i in range(1, N+N):
        if i <= N:
            cnt = i 
        else:
            cnt = N+N - i
        #print cnt

        if i < N:
            r = 0
        else:
            r = i - N

        if i < N:
            c = i - 1
        else:
            c = N - 1
        
        diag = []

        for a in range(cnt):
            diag.append(mat[r+a][c-a])
        result.append(diag)

    return result

print get_anti(mat, 2)