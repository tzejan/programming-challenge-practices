l = [1, [2, 3], [4, 5, [6, 7, [8, 9, [10], [11], [12, 13, 14, [15]]], [16], [17, 18]]]]

def printList(l):

    for e in l:
        if type(e) is list:
            printList(e)
        else:
            print e

printList(l)

# uppercase, lowercase, numbers
# limi 6 char
