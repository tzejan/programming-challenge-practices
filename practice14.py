def makepalindrome(s):
    changes = 0
    for i in range(len(s)/2):
        changes += abs(ord(s[i]) - ord(s[i-1]))
        print s[i], s[i-1]
    return changes


print makepalindrome("abcba")