#

#n = int(raw_input())
#k = map(int, raw_input().split())
#q = int(raw_input())
n = 4
k = [2, 1, 3, 4]
q = 3 


root = None
class Node(object):
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
        
for i in k:
    n = Node()
    n.data = i
    
    if not root:
        root = n
        continue

    temp = root
    parent = None
    while temp:
        parent = temp
        if temp.data >= i:
            temp = temp.left
        else:
            temp = temp.right
            
    if parent.data >= i:
        parent.left = n
    else:
        parent.right = n
        


temp = root
while temp and temp.data != q:
    if temp.data > q:
        temp = temp.left
    else:
        temp = temp.right

def inOrder(node):
    if not node:
        return
    print node.data
    inOrder(node.left)
    inOrder(node.right)
    
inOrder(temp)
        

    
