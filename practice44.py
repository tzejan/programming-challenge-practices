#https://www.hackerearth.com/practice/data-structures/advanced-data-structures/trie-keyword-tree/practice-problems/algorithm/registration-system/

class Node(object):
    def __init__(self, letter):
        self.char = letter
        self.children = dict()
        self.occupied = False
        self.lastOpen = 0


def getID(trie, proposedID):
    generatedID = proposedID
    parent = trie
    for c in proposedID:
        if c not in parent.children:
            n = Node(c)
            parent.children[c] = n
        parent = parent.children[c]

    if not parent.occupied:
        parent.occupied = True
        return generatedID

    emptySlot = False
    i = parent.lastOpen
    numID = ""
    while not emptySlot:
        numParent = parent
        numID = str(i)
        for c in numID:
            if c not in numParent.children:
                n = Node(c)
                numParent.children[c] = n
            if not numParent.children[c].occupied:
                numParent.children[c].occupied = True
                generatedID += numID
                parent.lastOpen = i
                emptySlot = True
                break
            numParent = numParent.children[c]
        i += 1

    return generatedID
    
trie = Node("")
'''
print getID(trie, "lebron")
print getID(trie, "lebron0")
print getID(trie, "lebron1")
print getID(trie, "lebron")

exit(0)
'''
with open("4fe134f4-a-input-4fe12ca.txt.clean.txt", "r") as f:
    n = int(f.readline())
    n = 790 #629 790

    for _ in range(n):
        proposedID = f.readline().strip()
        newID = getID(trie, proposedID)
        print proposedID, newID

exit(0)

n = int(raw_input())

for _ in range(n):
    proposedID = raw_input().strip()
    newID = getID(trie, proposedID)
    print newID