def commonChild(s1, s2):
    sets1 = set()
    sets2 = set()

    for c in s1:
        sets1.add(c)
    for c in s2:
        sets2.add(c)

    commonLetters = sets1 & sets2

    ts1 = []
    ts2 = []
    for c in s1:
        if c in commonLetters:
            ts1.append(c)
    for c in s2:
        if c in commonLetters:
            ts2.append(c)

    print commonLetters, ts1, ts2

    #wrong loop here, does not skip over letters
    longestChild = 0
    for i in range(len(ts1)):
        for li in range(i+1, len(ts1)+1):
            for j in range(len(ts2)):
                for lj in range(j+1, len(ts2)+1):
                    print i, li, j, lj, ts1[i:li], ts2[j:lj]
                    if ts1[i:li] == ts2[j:lj] and longestChild < li - i:
                        longestChild = li - i
    print longestChild

def preProcess(s1, s2):
    sets1 = set()
    sets2 = set()

    for c in s1:
        sets1.add(c)
    for c in s2:
        sets2.add(c)

    commonLetters = sets1 & sets2

    ts1 = []
    ts2 = []
    for c in s1:
        if c in commonLetters:
            ts1.append(c)
    for c in s2:
        if c in commonLetters:
            ts2.append(c)

    #print commonLetters, ts1, ts2
    return "".join(ts1), "".join(ts2)

memo = dict()

def sKey(s1, s2):
    return s1+':'+s2

def DPCommonChild(s1, s2):
    if sKey(s1,s2) in memo:
        return memo[sKey(s1,s2)]

    if len(s1) == 0 or len(s2) == 0:
        return 0

    
    if s1 == s2:
        #print s1, s2
        return len(s1)

    longest = 0
    for i in range(len(s1)):
        subS1 = s1[:i]+s1[i+1:]
        commonss = DPCommonChild(subS1, s2)
        memo[sKey(subS1,s2)] = commonss
        longest = max(commonss, longest)
        
    for i in range(len(s2)):
        subS2 = s2[:i]+s2[i+1:]
        commonss = DPCommonChild(s1, subS2)
        memo[sKey(s1,subS2)] = commonss
        longest = max(commonss, longest)

    memo[sKey(s1,s2)] = longest    
    return longest



def DPCommonChild2(s1, s2):
    c = [[0 for x in range(len(s1)+1)] for x in range(len(s2)+1)] 
    for i in range(len(s2)+1):
        c[i][0] = 0
    for j in range(len(s1)+1):
        c[0][j] = 0
    for i in range(len(s2)):
        for j in range(len(s1)):
            if s1[j] == s2[i]:
                c[i+1][j+1] = c[i][j] + 1
            else:
                c[i+1][j+1] = max(c[i][j+1], c[i+1][j])
    return c[len(s2)][len(s1)]
    

def DPCommonChild3(s1, s2):
    c = [0 for x in range((len(s1)+1)*(len(s2)+1))] 
    w = len(s2)+1
    for i in range(len(s2)+1):
        c[i] = 0
    for j in range(len(s1)+1):
        c[j*w] = 0
    for j in range(len(s1)):
        for i in range(len(s2)):        
            if s1[j] == s2[i]:
                c[i+1+(j+1)*w] = c[i+(j*w)] + 1
            else:
                c[i+1+(j+1)*w] = max(c[i+(j+1)*w], c[i+1+j*w])
    return c[len(s2)+len(s1)*w]

def DPCommonChild4(s1, s2):
    c = [[0 for x in xrange(len(s1)+1)] for x in xrange(len(s2)+1)] 
    for i in xrange(len(s2)+1):
        c[i][0] = 0
    for j in xrange(len(s1)+1):
        c[0][j] = 0
    for i in xrange(len(s2)):
        for j in xrange(len(s1)):
            if s1[j] == s2[i]:
                c[i+1][j+1] = c[i][j] + 1
            else:
                c[i+1][j+1] = max(c[i][j+1], c[i+1][j])
    return c[len(s2)][len(s1)]
    


inputList = [("HARRY", "SALLY"), ("AA", "BB"),  ("ABCDEF", "FBDAMN"), ("ABCDEF", "DBACFE"),("SHINCHAN", "NOHARAAA"), ]
allA = 'A' * 5000
allB = 'A' * 5000

for i in range(1):
    print DPCommonChild4(allA, allB)
#import sys
#print sys.getsizeof(memo)

for i in inputList:
    print i
    #commonChild(i[0], i[1])
    #print DPCommonChild2(i[0], i[1])
    #pps = preProcess(i[0], i[1])
    #print DPCommonChild(pps[0], pps[1])
    