
x = 3
y = 0
for _ in range(32):
    y = (y << 1) | (x & 1)
    x >>= 1


print "{0:b}".format(y)

# depth first search

    def sumNumbers(self, A):
        sum_of_num = 0
        nodes = [A]
        visited = set()
        while nodes:
            n = nodes[-1]
            if n.left or n.right:
                visited.add(n)
            if n.left and n.left not in visited:
                nodes.append(n.left)
                continue
            if n.right and n.right not in visited:
                nodes.append(n.right)
                continue
            if n.left == None and n.right == None:
                num = 0
                for node in nodes:
                    num = (num * 10) + node.val
                sum_of_num += num
                visited.add(n)
                nodes.pop()
                continue
            if n in visited:
                nodes.pop()
        
        return sum_of_num % 1003

