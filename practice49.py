#small hexxeh

hexDict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
hexArr = '0123456789abcdef'


def hexStrToDecimal(hexStr):
    decimal = 0
    power = 1
    s = hexStr[::-1]
    for c in s:
        decimal += hexDict[c] * power
        power *= 16
    return decimal

def decimalToHexStr(decimal):
    hexVal = ""
    while decimal:
        rem = decimal % 16
        hexVal += hexArr[rem]
        decimal /= 16
    if hexVal:
        return hexVal[::-1]
    return "0"


def increaseHex(hexStr):
    decVal = hexStrToDecimal(hexStr)
    decVal += 1

    return decimalToHexStr(decVal)

def isSameReversed(s):
    for i in range(len(s)/2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

k = "d3e01e"
k = increaseHex(k)
while not isSameReversed(k):
    k = increaseHex(k)
print k
exit(0)

t = int(raw_input())
for _ in range(t):
    k = raw_input().strip()
    k = increaseHex(k)
    while not isSameReversed(k):
        k = increaseHex(k)
    print k


