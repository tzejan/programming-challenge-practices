#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      simtj
#
# Created:     17/10/2013
# Copyright:   (c) simtj 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
memo = {}
def longestZigZag(listOfNum):
    prevNum = listOfNum[0]
    difference = []
    for num in listOfNum[1:]:
        diff = num - prevNum
        if diff != 0:
            difference.append(diff)
        prevNum = num

    def getKey(currDiff, potDifference, seq):
        return (currDiff, tuple(potDifference), seq)

    def dp(currDiff, potDifference, seq):
        #print currDiff, potDifference, seq
        if getKey(currDiff, potDifference, seq) in memo:
            return memo[getKey(currDiff, potDifference, seq)]

        if not potDifference:
            memo[getKey(currDiff, potDifference, seq)] = seq + 1
            return seq+1

        contSeq = 0
        if currDiff * potDifference[0] < 0:
            contSeq = dp(potDifference[0], potDifference[1:], seq + 1)
            memo[getKey(potDifference[0], potDifference[1:], seq + 1)] = contSeq

        skipSeq = dp(currDiff, potDifference[1:], seq)
        memo[getKey(currDiff, potDifference[1:], seq)] = skipSeq

        return max(contSeq, skipSeq)



    #print difference
    if len(difference) > 1:
        return dp(difference[0], difference[1:], 1)
    else:
        return len(difference) + 1


inputList = [
                ([1,7,4,9,2,5],6),
                ([1,17,5,10,13,15,10,5,16,8],7),
                ([10,20],2),
                ([20,10],2),
                ([20,20],1),
                ([1,1],1),
                ([44],1),
                ([3,3,3,3,3],1),
                ([1,2,3,4,5,6,7,8,9],2),
                ([10,9,8,7,6,7,8,9,10],3),
                ([8,6,4,2,3,5,7,9],3),
                ([4,1,6,7,7,8,9,8,6,8],5),
                ([4,6,4,4,1,2,6,7,1,3],6),
                ([9,1,8,2,7,3,6,4,5,5,4,6,3,7,2,8,1,9],17),
                ([70,55,13,2,99,2,80,80,80,80,100,19,7,5,5,5,1000,32,32],8),
                ([4,4,4,4,4,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2],3),
                ([1,2,2,1,1,2,3,3,2,1,1,2,3,4,4,3,2,1,1,2,3,4,5,5,4,3,2,1],9),
                ([12,333,700,436,1,919,959,456,456,456,1000,193,192,13,75,818,197,197,2,777,99,81,222,109,1000,19,27,270,62,189,987,234,55,2,718],20),
##                ([12,333,700,436,1,919,959,456,456,456,1000,193,192,13,75,818,197,197,2,777,99,81,222,109,1000,19,27,270,62,189,987,234,55,2,718,238,901,901,900,432,55,606,89,7,7,23,789,790,800,1000],26),
##                ([396,549,22,819,611,972,730,638,978,342,566,514,752,871,911,172,488,542,482,974,210,474,66,387,1,872,799,262,567,113,578,308,813,515,716,905,434,101,632,450,74,254,1000,780,633,496,513,772,925,746],37),
##                ([374,40,854,203,203,156,362,279,812,955,600,947,978,46,100,953,670,862,568,188,67,669,810,704,52,861,49,640,370,908,477,245,413,109,659,401,483,308,609,120,249,22,176,279,23,22,617,462,459,244],36),
##                ([89,106,125,142,141,137,158,184,191,189,189,206,228,240,228,263,259,256,266,287,302,297,330,341,353,353,364,376,365,398,386,420,413,419,451,441,463,484,480,487,494,520,534,542,534,541,571,584,565,577],26),
##                ([61,82,126,97,167,186,119,154,155,142,153,181,172,192,223,272,273,260,280,330,329,350,273,324,349,306,385,375,420,416,435,457,373,477,395,487,500,439,493,537,518,549,542,500,524,541,512,589,549,543],35),

            ]

import time

t0 = time.time()

for testcase in inputList:
    result = longestZigZag(testcase[0])
    if testcase[1] != result:
        print testcase
        print testcase[1],">>", result

t1 = time.time()
print "done in %fs" % (t1-t0)