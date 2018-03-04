def stepnum(A, B):
        
    def next_steps(nums, idx):
        steps = []
        if idx <= 0:
            return nums

        for n in nums:
            ld = n % 10
            if ld > 0:
                steps.append(n*10 + ld-1)
            if n > 0 and ld < 9:
                steps.append(n*10 + ld+1)

        return next_steps(steps, idx - 1)
    
    n = A
    m = B
    nc = 0
    mc = 0
    while n >= 10:
        n /= 10
        nc += 1

    while m >= 10:
        m /= 10
        mc += 1

    results = []

    for c in range(nc, mc+1):
        seed = [i for i in range(10)]
        results.extend(filter(lambda x: x >= A and x <= B, next_steps(seed, c)))

    return results

print stepnum(1, 1000)
arr = [[1,2], [3,4], [5,6]]
for a, b in arr:
    print a, b