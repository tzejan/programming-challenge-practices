#dota heroes rush

def addItem(A, item):
    A.append(item)
    upheap(A, (len(A)-1)/2, len(A)-1)

def upheap(A, n, m):
    leftChild = 2 * n + 1
    rightChild = 2 * n + 2

    if n < 0:
        #reached the parent of the root
        return

    swapIndex = n
    if leftChild <= m and A[leftChild] > A[n]:
        swapIndex = leftChild
    if rightChild <=m and A[rightChild] > A[n] and A[rightChild] > A[leftChild]:
        swapIndex = rightChild

    if swapIndex != n:
        temp = A[n]
        A[n] = A[swapIndex]
        A[swapIndex] = temp
        upheap(A, (n-1)/2, m) # parent

def downheap(A, n, m):
    leftChild = 2 * n + 1
    rightChild = 2 * n + 2

    if n > m:
        #end of array
        return

    swapIndex = n
    if leftChild <= m and A[leftChild] > A[n]:
        swapIndex = leftChild
    if rightChild <= m and A[rightChild] > A[n] and A[rightChild] > A[leftChild]:
        swapIndex = rightChild

    if swapIndex != n:
        temp = A[n]
        A[n] = A[swapIndex]
        A[swapIndex] = temp
        downheap(A, swapIndex, m)

def modifyHealth(A, damage):
    A[0] -= damage
    if A[0] > 0:
        downheap(A, 0, len(A)-1)
        return True
    else:
        return False


#code to calculate rush

def raidSuccess(towers, damage, heroes):

    heroHealth = []
    for h in heroes:
        addItem(heroHealth, h)

    for t in range(towers):
        if not modifyHealth(heroHealth, damage):
            return False

    return True

def altRaidSuccess(towers, damage, heroes):
    totalHits = 0
    for h in heroes:
        hits = h/damage
        if h % damage == 0:
            hits -= 1
        totalHits += hits

    if totalHits >= towers:
        return True

    return False

heroes = [100, 100, 100]
towers = 3
damage = 75


print raidSuccess(towers, damage, heroes)
print altRaidSuccess(towers, damage, heroes)


