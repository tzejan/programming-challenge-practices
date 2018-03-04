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
            #([1,2,5,3,4,5], 9),
            ([1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000], 18252025766940),
            #([1,2,3,4,5],4),
            #([7,7,8,9,10,11,1,2,2,3,4,5,6],607),
            #([123,217,661,678,796,964,54,111,417,526,917,923],0),

]




def howMany(values):
    memo = set()

    def getKey(bobVal, frankVal, bobMax, frankMin, bIndex, fIndex, index):
        return (bobVal, frankVal, bobMax, frankMin, bIndex, fIndex, index)

    def dp(bobVal, frankVal, bobMax, frankMin, bIndex, fIndex, index):
        #print bobVal, frankVal, bobMax, frankMin, bIndex, fIndex, index
        #print len(values)
        #key = getKey(bobVal, frankVal, bobMax, frankMin, bIndex, fIndex, index)

        #if key in memo:
        #    return 0

        if len(values) == index:
            if bobVal == frankVal and bobMax <= frankMin and bobVal > 0:
                #memo.add(key)
                #print bobCache, '-' ,frankCache
                #print bobVal, frankVal, bobMax, frankMin, bIndex, fIndex, index

                return 1
            else:
                return 0



        nextJewelry = values[index]
        #print nextJewelry, leftover, leftoverJewelry
        newBobMax = bobMax
        if newBobMax < nextJewelry:
            newBobMax = nextJewelry
        tryBob = dp(bobVal+nextJewelry, frankVal, newBobMax, frankMin, index, fIndex, index+1)

        newFrankMin = frankMin
        if newFrankMin > nextJewelry:
            newFrankMin = nextJewelry
        tryFrank = dp(bobVal, frankVal+nextJewelry, bobMax, newFrankMin, bIndex, index, index+1)

        trySkip = dp(bobVal, frankVal, bobMax, frankMin, bIndex, fIndex, index+1)

        return tryBob + tryFrank + trySkip


    return dp(0, 0, 0, 1000, 0, 0, 0)


import time

t0 = time.time()

for data in dataList:
    result = howMany(data[0])
    print result

t1 = time.time()
print "done in %fs" % (t1-t0)




