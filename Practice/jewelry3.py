#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      simtj
#
# Created:     24/10/2013
# Copyright:   (c) simtj 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

dataList = [
            ([1,2,5,3,4,5], 9),
            #([1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000], 18252025766940),
            #([1,2,3,4,5],4),
            #([7,7,8,9,10,11,1,2,2,3,4,5,6],607),
            #([123,217,661,678,796,964,54,111,417,526,917,923],0),

]




MAXN = 30;
MAX = 30000;

#LL B[MAXN+1][MAX+1]; // [n pocz][sum]
#LL F[MAXN+1][MAX+1];

#LL nk[MAXN+1][MAXN+1];



def cnk(nk):
    nk[0][0]=1
    for k in range(1, MAXN+1):
        nk[0][k]=0

    for n in range(1,MAXN+1):
        nk[n][0]=1;
        for k in range(1,MAXN+1):
            nk[n][k] = nk[n-1][k-1]+nk[n-1][k]



def calc(T, listofJewelry, n):
    T[0][0] = 1
    for x in range(1,MAX+1):
        T[0][x]=0
    for ile in range(1,n):
        a = listofJewelry[ile-1]
        for x in range(0,MAX+1):
            T[ile][x] = T[ile-1][x]
            if(x>=a):
                T[ile][x] +=T[ile-1][x-a];


def howMany(listofJewelry):
    B = [[0 for x in xrange(MAX+1)] for x in xrange(MAXN+1)]
    F = [[0 for x in xrange(MAX+1)] for x in xrange(MAXN+1)]
    nk = [[0 for x in xrange(MAXN+1)] for x in xrange(MAXN+1)]

    n = len(listofJewelry)
    cnk(nk)
    listofJewelry.sort(reverse=True)
    calc(F, listofJewelry, n)
    #print F[-1]
    listofJewelry.sort()
    calc(B, listofJewelry, n)
    res = 0
    done=0
    while(done<n):
        p=done
        while(p<n and listofJewelry[p]==listofJewelry[done]):
            p = p + 1
        print ">",p
        c=p-done
        for u in range(1,c):
            uu = u * listofJewelry[done]

            for x in range(uu,MAX):
              res += B[done][x-uu] * F[n-done-u][x] * nk[c][u]

        done=p

    return res;




import time

t0 = time.time()

for data in dataList:
    result = howMany(data[0])
    print result

t1 = time.time()
print "done in %fs" % (t1-t0)




