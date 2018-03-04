#https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/the-normal-type/

#n = int(raw_input())
#a = map(int, raw_input().split())

a = [1, 1, 1, 1, 1 ]

#with open("3e7de26a-7-input-3e7ddd6.txt") as f:
#    n = int(f.readline())
#    a = map(int, f.readline().split()) 

distinct = len(set(a))
#print distinct

i = 0
j = 0
ds = 0
working_dict = dict()
working_dict[a[j]] = 1

while j < len(a):
    if len(working_dict) == distinct:
        ds += len(a) - j 
        #move the front

        working_dict[a[i]] -= 1
        if not working_dict[a[i]]:
            del working_dict[a[i]]
        i += 1
    else:
        # move the back
        j += 1
        if j < len(a):
            if a[j] not in working_dict:
                working_dict[a[j]] = 0
            working_dict[a[j]] += 1
    
print ds
    

'''

working_set = set(a[:distinct])
ds = 0
for i in range(distinct-1, len(a)):
    for j in range(i, len(a)):
        working_set.add(a[j])
        if len(working_set) == distinct:
            ds += len(a) - j
            break

    if a[i-distinct] in working_set:
        working_set.remove(a[i-distinct])
        
print ds
'''