#https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/monk-and-philosophers-stone/
'''
n = int(raw_input())
h_coins = map(int, raw_input().split())
m_coins = []
m_tot_val = 0
q, x = map(int, raw_input().split())
'''
n = 0
h_coins = []
m_coins = []
m_tot_val = 0
q = 0
x = 0
with open("bcf79ac4-a-input-bcf7966.txt.clean.txt", 'r') as f:
    n = f.readline()
    h_coins = map(int, f.readline().split())
    h_coins.reverse()
    m_coins = []
    m_tot_val = 0
    q, x = map(int, f.readline().split())


    for i in range(q):
        instruction = f.readline()
        print sum(m_coins), x
        if sum(m_coins) == x:
            print "<><><><>"
        if instruction[0] == 'H':
            coin = h_coins.pop()
            m_coins.append(coin)
            m_tot_val += coin
            if m_tot_val == x:
                print len(m_coins)
                break
        else:
            m_tot_val -= m_coins.pop()
    else:
        print -1
