# a system to get the hits for last x secs
import time
import random

random.seed("g")
hitCount = []

now = time.gmtime()
timenow = time.mktime(now)
print timenow, timenow
print timenow - (timenow % 60)


def addCount(timenow, count):
    if len(hitCount) and hitCount[-1][0] == timenow:
        hitCount[-1][0] += count
    else:
        hitCount.append((timenow, count))

def querySecs(timenow, duration):
    totalCount = 0
    index = len(hitCount) - 1
    timeLimit = timenow - duration
    while index != 0 and hitCount[index][0] >= timeLimit:
        totalCount += hitCount[index][1]
        index -= 1

    return totalCount

def compact(timenow):
    currIndex = -1
    endIndex = -1
    timeStop = timenow - (timenow % 60)
    timeStart = timeStop - 60
    for i in range(len(hitCount)):
        if hitCount[i][0] >= timeStart and hitCount[i][0] < timeStop:
            if currIndex == -1:
                currIndex = i
                hitCount[currIndex] = (timeStart, hitCount[currIndex][1])
                continue
            hitCount[currIndex] = (timeStart, hitCount[i][1] + hitCount[currIndex][1])
            endIndex = i
        elif hitCount[i][0] >= timeStop:
            hitCount[i-endIndex+currIndex] = hitCount[i]
    #discard the end
    del hitCount[len(hitCount) - endIndex:]


# add data
for i in range(100):
    addCount(i, random.randrange(10))

print hitCount
print querySecs(10, 60)

compact(99)
print hitCount


