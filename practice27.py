#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/little-shino-and-coins-3/

#k = int(raw_input())
#s = raw_input()
k = 3
s = "abcaa"
count = 0

for l in range(len(s)):
    letter_set = set(s[l:l+k-1])

    for r in range(l+k-1, len(s)):
        letter_set.add( s[r] )

        unique = len(letter_set)
        print l, r, unique, letter_set
        if unique == k:
            count += 1
        elif unique > k:
            break
            #print l, r, s[l:r]
        #queue.popleft()
print count 