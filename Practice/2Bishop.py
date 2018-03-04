def numOfSteps(position, target):
    x = position % 8
    y = position / 8

    tx = target % 8
    ty = target / 8

    # on target, no need to move
    if position == target:
        return 0

    # impossible to reach target
    if (x + y) % 2 != (tx + ty) % 2:
        return -1

    # on same axis, reachable in 1 step
    diff = abs(position - target)
    if diff % 7 == 0 or diff % 9 == 0:
        #print diff
        if diff / 8 <= max(abs(x-tx), abs(y-ty)):
            return 1

    # reachable in 2 steps
    return 2

steps = {-1:[], 0:[], 1:[], 2:[]}
for p in range(0, 64):
    for t in range(0, 64):
        steps[numOfSteps(p, t)].append((p,t))
        #print p, t, numOfSteps(p, t)
    
for key, val in steps.iteritems():
    print key
    for v in val:
        print v

    print "\n"

