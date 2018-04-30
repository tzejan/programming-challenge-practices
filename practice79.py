#https://www.codewars.com/kata/twice-linear/python

def dbl_linear(n):
    seq = [1]
    two_idx = 0
    three_idx = 0
    while (n > len(seq)-1):
        two_num = 2 * seq[two_idx] + 1
        three_num = 3 * seq[three_idx] + 1

        if (two_num <= seq[-1]):
            two_idx += 1
            continue
        if (two_num < three_num):
            seq.append(two_num)
            two_idx += 1
        else:
            seq.append(three_num)
            three_idx += 1

    return seq[n]