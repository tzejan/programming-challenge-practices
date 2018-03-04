#https://www.hackerearth.com/practice/data-structures/trees/binary-and-nary-trees/practice-problems/algorithm/the-silly-snail-3/

class Node(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = 0

tree_dict = dict()
root = 0

def addBranch(x, y, z):
    #branch = Node()
    #branch.data = x
    #print x, y, z
    global root

    tree_dict[x]= (y, z)
    if root == 0 or root == y or root == z:
        root = x

def traverseTree(root):
    global tree_dict

    print root,
    if root in tree_dict:
        left, right = tree_dict[root]
        if left:
            traverseTree(left)
        if right:
            traverseTree(right)


with open("practice38Input.txt", "r") as f:
    t = int(f.readline())

    for _ in range(t):
        tree_dict = dict()
        n = int(f.readline())

        for b in range(n):
            x, y, z = map(int, f.readline().split())
            addBranch(x, y, z)

        traverseTree(root)
        print ""

exit(0)

t = int(raw_input())

for _ in range(t):
    tree_dict = dict()
    n = int(raw_input())

    for b in range(n):
        x, y, z = map(int, raw_input().split())
        addBranch(x, y, z)

    traverseTree(root)
    print ""




