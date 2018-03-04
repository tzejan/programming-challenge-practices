#https://www.hackerearth.com/practice/algorithms/searching/ternary-search/tutorial/



def UniModalfunc(x):
    return 2 * x * x - 12 * x + 7 

def mino(l, r):
    luf = l
    ruf = r
    #while abs(ruf - luf) > 0.005:
    for i in range(50):
        int_1 = (r - l) / 3.0 + l
        int_2 = r - (r - l) / 3.0

        luf = UniModalfunc(int_1)
        ruf = UniModalfunc(int_2)
        if luf < ruf:
            r = int_2
        else:
            l = int_1

    return int(round(ruf))

with open("86a65e1e-7-input-86a6593.txt", "r") as f:
    n = int(f.readline())

    for _ in range(n):
        l, r = map(int, f.readline().split())

        if _ == 228:
            print _, mino(l, r)


n = int(raw_input())

for _ in range(n):
    l, r = map(int, raw_input().split())

    print mino(l, r)
    


