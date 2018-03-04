
hexDict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
hexArr = '0123456789abcdef'

def incrementHex(s):
    carry = 1
    result = ""
    for c in s[::-1]:
        carry = hexDict[c] + carry 
        result += hexArr[carry % 16]
        carry /= 16
    if carry:
        result += hexArr[carry]

    return result[::-1]

def isHexxeh(s):
    for i in range(len(s)/2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

def getNextHexxeh(s):
    s = incrementHex(s)
    if isHexxeh(s):
        return s

    fstPt = (len(s) / 2) - 1
    secPt = (len(s) + 1) / 2
    midPt = (len(s) - 1) / 2

    if s[secPt:] > s[fstPt::-1]:
        fstHalfResult = incrementHex(s[:midPt+1])
    else:
        fstHalfResult = s[:midPt+1] 

    return fstHalfResult + fstHalfResult[fstPt::-1]

'''
t = int(raw_input())
for _ in range(t):
    k = raw_input().strip()
    print getNextHexxeh(k)
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

#print "a" < "e3d"
#print getNextHexxeh('3441')
#exit(0)
k = ['11', '1c0', '1c3', 'd35a', '12345', '123456', '12300', 'fe', 'ff', '0', '10f0f', '3444', '987654', 'd3e01e', "987654321", "fffff"]
#for s in k:
for i in range(0,1000000):
    #s = decimalToHexStr(i)
    s = hexArr
    getNextHexxeh(s)
    #print s, getNextHexxeh(s)
   