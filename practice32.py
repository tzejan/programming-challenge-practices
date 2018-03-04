#https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/signal-range/

def get_tower_range(tower_height):
    tower_range = []
    for i in range(len(tower_height)):
        if i == 0:
            tower_range.append(1)
            continue
        check_tower_index = i - 1
        while (check_tower_index >= 0 and tower_height[i] >= tower_height[check_tower_index]):
            check_tower_index -= tower_range[check_tower_index]
        tower_range.append(i - check_tower_index)
    return tower_range



t = int(raw_input())
for _ in range(t):
    n = int(raw_input())
    th = map(int, raw_input().split())
    tower_range = get_tower_range(th)
    print " ".join([str(r) for r in tower_range])