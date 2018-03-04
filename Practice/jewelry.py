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
            ([1,2,3,4,5],4),
            #([7,7,8,9,10,11,1,2,2,3,4,5,6],607),
            ([123,217,661,678,796,964,54,111,417,526,917,923],0),

]

memo = set()


def howMany(values):

    def getKey(bobCache, frankCache, leftover, bIndex, fIndex):
        return (tuple(bobCache), tuple(frankCache), tuple(leftover), bIndex, fIndex)

    def dp(bobCache, frankCache, leftover, bIndex, fIndex, index):
        if frankCache and bobCache:
            if min(frankCache) < max(bobCache):
                return 0

        if sum(bobCache) == sum(frankCache) and len(bobCache) > 0:
            key = getKey(bobCache, frankCache, leftover, bIndex, fIndex)
            if key in memo:
                return 0

            memo.add(key)
            #print bobCache, '-' ,frankCache
            print key
            return 1

        if not leftover:
            return 0

        index = index + 1
        nextJewelry = leftover[0]
        leftoverJewelry = leftover[1:]
        #print nextJewelry, leftover, leftoverJewelry
        bobCopy = bobCache[:]
        frankCopy = frankCache[:]
        bobCopy.append(nextJewelry)
        tryBob = dp(bobCopy, frankCopy, leftoverJewelry, index +1, fIndex, index)

        bobCopy = bobCache[:]
        frankCopy = frankCache[:]
        frankCopy.append(nextJewelry)
        tryFrank = dp(bobCopy, frankCopy, leftoverJewelry, bIndex, index + 1, index)

        bobCopy = bobCache[:]
        frankCopy = frankCache[:]
        trySkip = dp(bobCopy, frankCopy, leftoverJewelry, bIndex, fIndex, index)

        return tryBob + tryFrank + trySkip


    return dp([], [], values ,0 ,0, 0)

for data in dataList:
    result = howMany(data[0])
    print result




