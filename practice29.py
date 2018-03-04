#https://www.hackerearth.com/practice/data-structures/arrays/multi-dimensional/practice-problems/algorithm/akash-and-the-assignment-1-12/

def k_smallest(il, queries):
    for l, r, k in queries:
        if k > r-l+1:
            print "Out of range"
            continue

        letters = il[r][:]

        for i in range(26):
            letters[i] -= il[l-1][i]

        for i, c in enumerate(letters):
            k -= c
            if k <= 0:
                print chr(i+97)
                break

def create_indexed_list(s):
    indexed_list = [[0] * 26] 
    
    for i, c in enumerate(s):
        indexed_list.append(indexed_list[i][:])
        indexed_list[i+1][ord(c)-97] += 1

    return indexed_list


#il = create_indexed_list("a")
#k_smallest(il, [[1,1,1],[1,1,1]])

#exit(0)
with file("practice29-input-110fb5d.txt", 'r') as f:
    n, q = map(int, f.readline().split())
    s = f.readline().strip()
    queries = []
    for _ in range(q):
        queries.append( map(int, f.readline().split()))

    #k_smallest(s, queries)
    il = create_indexed_list(s)
    k_smallest(il, queries)
    

exit(0)
n, q = map(int, raw_input().split())
s = raw_input().strip()
queries = []
for _ in range(q):
    queries.append( map(int, raw_input().split()))

ans = k_smallest(s, queries)
for a in ans:
    print a