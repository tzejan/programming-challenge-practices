def BiggerIsGreater(s):
    w = list(s)
    si = len(w)

    for i in range(len(w)-1, 0, -1):
        if w[i] > w[i-1]:
            si = i-1
            break

    nl = si + 1

    for i in range(si+1, len(w)):
        if w[i] < w[nl] and w[i] > w[si]:
            nl = i

    #swap the next biggest number
    if si < len(w):
        temp = w[si]
        w[si] = w[nl]
        w[nl] = temp

    for i in range(si+1, len(w)):
        smallesti = i
        for j in range(i+1, len(w)):
            if w[j] < w[smallesti]:
                smallesti = j
        if smallesti != i:
            temp = w[i]
            w[i] = w[smallesti]
            w[smallesti] = temp

    if si == len(w):
        print "no answer"
    else:
        print "".join(w)

inputList = ["ab", "bb", "hefg", "gojh"]
for i in inputList:
    BiggerIsGreater(i)