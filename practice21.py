# shuffle a list of integers

import random


random.seed("Google")

def shuffle(a):
    acopy = list(a)
    for i in range(len(acopy)):
        newIndex = random.randrange(len(acopy))
        temp = acopy[i]
        acopy[i] = acopy[newIndex]
        acopy[newIndex] = temp
    return acopy

def equalLists(lista, listb):
    same = True

    def generateFreqCounts(numbers):
        freqCount = dict()

        for n in numbers:
            if n not in freqCount:
                freqCount[n] = 0
            freqCount[n] += 1

        return freqCount


    listACounts = generateFreqCounts(lista)
    listBCounts = generateFreqCounts(listb)

    listAKeys = listACounts.keys()
    listBKeys = listBCounts.keys()

    if listAKeys.sort() == listBKeys.sort():
        print "Same Keys"
    else:
        print "Not same Keys"
        same = False

    for k in listAKeys:
        if listACounts[k] == listBCounts[k]:
            print "Same count ", k, listACounts[k]
        else:
            print "Not same count ", k, listACounts[k]
            same = False

    return same


test1 = [random.randrange(10) for n in range(10)]
stest1 = shuffle(test1)
print test1
print stest1
print equalLists(test1, stest1)

def shuffleSameSeed(arr):
    random.seed("Google")
    arrcpy = list(arr)

    for i in range(len(arrcpy)):
        newIndex = random.randrange(len(arrcpy))
        temp = arrcpy[i]
        arrcpy[i] = arrcpy[newIndex]
        arrcpy[newIndex] = temp

    return arrcpy

test2 = [n for n in range(10)]
test2Result = shuffleSameSeed(test2)
print test2
print test2Result
print ""

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return abs(a*b)/gcd(a,b)

def determineShuffleCycle(arr):
    keyInput = [n for n in range(len(arr))]

    shuffleResults = shuffleSameSeed(keyInput)
    shuffleKey = dict()
    for i in range(len(shuffleResults)):
        shuffleKey[shuffleResults[i]] = i

    print keyInput
    print shuffleResults
    print shuffleKey

    cycleLengths = [0] * len(arr)

    for i in range(len(cycleLengths)):
        count = 1
        sindex = i
        while shuffleKey[sindex] != i:
            count += 1
            sindex = shuffleKey[sindex]
            #print i, sindex
        cycleLengths[i] = count

    #find the lowest common multiple for all the cycle lengths
    print cycleLengths

    cyclelength = 1
    for n in cycleLengths:
        cyclelength = lcm(n, cyclelength)

    return cyclelength



test3 = [n for n in range(60)]
test3Result = list(test3)
shuffleCycle = determineShuffleCycle(test3)
for n in range(shuffleCycle):
    test3Result = shuffleSameSeed(test3Result)

print test3
print test3Result
print shuffleCycle

