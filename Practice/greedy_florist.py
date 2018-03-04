#n, k = map(int, raw_input().split())
#f = map(int, raw_input().split())

line1 = "3 3"
line2 = "2 6 5 "

n, k = map(int, line1.split())
f = map(int, line2.split())


fs = sorted(f)[:n]

count = 0
mul = 1
pur_sum = 0

for p in fs[::-1]:
    count += 1
    pur_sum += p * mul 
    if count % k == 0:
        mul += 1

print pur_sum
