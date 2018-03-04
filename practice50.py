#big hexxeh

hexDict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
hexArr = '0123456789abcdef'

def diffHexxeh(sArr):
    halfSLen = len(sArr) / 2
    sLastIndex = len(sArr) - 1
    diffIndex = []
    for i in range(0, halfSLen):
        if sArr[i] != sArr[sLastIndex-i]:
            diffIndex.append(i)

    return diffIndex

def nextHexxeh(sArr):

    sArr = nextBiggerHex(sArr)
    diffIndex = diffHexxeh(sArr)

    # if there is no difference, and it is already a hexxeh
    if not diffIndex:
        return sArr

    isAlreadyBigger = False
    sLastIndex = len(sArr) - 1
    
    incrementFirstHalf = True
    #see if we need to increment the first half of the array
    for i in diffIndex:
        if sArr[sLastIndex-i] < sArr[i]:
            incrementFirstHalf = False
        else:
            incrementFirstHalf = True

    if incrementFirstHalf:
        halfMid = len(sArr)/2 + len(sArr) % 2
        firstHalf = sArr[:halfMid]
        firstHalf = nextBiggerHex(firstHalf)
        firstHalf.extend(sArr[halfMid:])
        sArr = firstHalf
        diffIndex = diffHexxeh(sArr) #find the difference again
        sLastIndex = len(sArr) - 1 #length might change

    for i in diffIndex:
        sArr[sLastIndex-i] = sArr[i]
                
    return sArr


def nextBiggerHex(sArr):
    carry = 1
    i = len(sArr) - 1
    while carry and i >= 0:
        v = hexDict[sArr[i]] + carry
        carry = v / 16
        sArr[i] = hexArr[v % 16]
        i -= 1

    if carry:
        sArr.append('0')
        #move the hex back one space
        for i in range(len(sArr)-1, 0, -1):
            sArr[i] = sArr[i-1]
        #if you need one more space, most likely it is all F, so 1st char is 1, and 2nd char is 0
        sArr[1] = hexArr[0]
        sArr[0] = hexArr[carry]
    return sArr
'''
sArr = list("f")
firstHalf = nextBiggerHex(sArr)

print "".join(sArr), "".join(firstHalf), ">>>>"
'''
def decimalToHexStr(decimal):
    hexVal = ""
    while decimal:
        rem = decimal % 16
        hexVal += hexArr[rem]
        decimal /= 16
    if hexVal:
        return hexVal[::-1]
    return "0"

k = ['11', '1c0', '1c3', 'd35a', '12345', '123456', '12300', 'fe', 'ff', '0', '10f0f', '3444', '987654']
#for s in k:
for i in range(0,1000000):
    #s = decimalToHexStr(i)
    s = hexArr
    #print s,
    sArr = list(s)
    #print nextBiggerHex(sArr)
    sArr = nextHexxeh(sArr)
    "".join(sArr)
    #print ""

exit(0)
t = int(raw_input())
for _ in range(t):
    k = raw_input().strip()
    kArr = list(k)
    kArr = nextHexxeh(kArr)
    print "".join(kArr)