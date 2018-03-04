#https://www.hackerearth.com/practice/data-structures/advanced-data-structures/trie-keyword-tree/practice-problems/algorithm/registration-system/
#
#
# This was implemented with misunderstanding the question.
# This solution increases the numbers at the end of the id, instead of the last character

class Node(object):
    def __init__(self, c):
        self.letter = c
        self.ids = None
        self.children = None
        self.taken = False


def findID(IDList, proposedID):
    left = 0
    right = len(IDList) - 1
    found = False
    while left <= right and not found:
        i = (left + right) / 2
        if IDList[i] == proposedID:
            found = True
            break
        if IDList[i] > proposedID:
            right = i - 1
        else:
            left = i + 1
    return found

def getSmallestID(IDList, proposedID):
    #binary search for proposed ID
    found = findID(IDList, proposedID)

    if found:
        proposedID = 0
        # loop through the list, if the proposedID is not at the index, then this is the smallest number not in the list
        for i in range(len(IDList)):
            if proposedID != IDList[i]:
                break
            proposedID += 1

    #add this id to the list
    IDList.append(proposedID)
    #sort this new IDList
    for i in range(len(IDList)-1, 0, -1):
        if IDList[i] < IDList[i-1]:
            temp = IDList[i]
            IDList[i] = IDList[i-1]
            IDList[i-1] = temp
        else:
            break

    return proposedID



def getLoginID(trie, name):
    loginID = ""
    parent = trie
    for i, c in enumerate(name):
        #numbers
        if c.isdigit():
            proposedID = int(name[i:])
            if not parent.ids:
                parent.ids = []

            found = findID(parent.ids, proposedID)
            if found and not parent.taken:
                parent.taken = True
                return loginID
            newID = getSmallestID(parent.ids, proposedID)
            return loginID + str(newID)

        #letters
        n = Node(c)
        loginID += c
        if not parent.children:
            parent.children = dict()
        if c not in parent.children:
            parent.children[c] = n

    # id with no numbers
    
    if not parent.taken:
        parent.taken = True
        return loginID

    if not parent.ids:
        parent.ids = []
    newID = getSmallestID(parent.ids, 0)
    return loginID + str(newID)

trie = Node("")

n = int(raw_input())

for _ in range(n):
    name = raw_input()
    newLoginID = getLoginID(trie, name)
    print newLoginID


