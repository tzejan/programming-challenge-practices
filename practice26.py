#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/chess-tournament-4/

n = 3
mat = [[], [0], [1, 0], [0, 1, 1], [1, 0, 0, 1], [1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1]]
#n = int(raw_input())
#mat = []
#for i in range(n):
#    mat.append(map(int, raw_input().split))
numParticipants = 2 ** n
print numParticipants, len(mat)
    
contestants = [i for i in range(1, numParticipants+1)]

winners = []
while len(contestants) > 1:
    for idx in range(0, len(contestants), 2):
        j = contestants[idx]
        i = contestants[idx+1]
        print i, j

        if (mat[i-1][j-1]):
            winners.append(i)
        else:
            winners.append(j)
    contestants = winners
    winners = []
    print contestants
    
print contestants[0]