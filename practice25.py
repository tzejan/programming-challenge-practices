#https://oj.leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

def findMin(num):
    l = 0
    r = len(num)-1
    i = (l+r)/2
    while r > l:
        if num[i] > num[i+1]:
            return num[i+1]
        if num[i] > num[r]:
            l = i + 1
        else:
            r = i - 1
        i = (l+r)/2
        print i
    return None

numbers = [n for n in range(10)]
numbers = numbers[4:] + numbers[:4]
print numbers
print findMin(numbers)