#    hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh
s = "hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh"
s = "aaab"

print s
print s[::-1]

def isPalin(s):
    for i in range(len(s)/2):
        ri = len(s)-i-1
        if s[i] != s[ri]:
            return False
    return True

pi = -1
for i in range(len(s)/2):
    ri = len(s)-i-1
    if s[i] != s[ri]:        
        if s[i+1] == s[ri]:
            if isPalin(s[i+1:ri+1]):
                pi = i
                break
        if s[i] == s[ri-1]:
            if isPalin(s[i:ri]):
                pi = ri
                break
        
print pi, len(s)-pi-1

print s[pi], s[len(s)-pi-1]
print len(s)