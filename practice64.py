"""Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.

Example:

Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Make sure the returned strings are sorted in order)

"""

def restoreIpAddresses(A):
    result = []
    def increment(idx):
        i = 3
        while i != -1:
            idx[i] = (idx[i] + 1) % 4
            if idx[i] == 0:
                idx[i] = 1
                i -= 1
            else:
                break
        return idx 

        

    idx = [1,1,1,0]
    for _ in range(81):
        idx = increment(idx)
        
        if sum(idx) == len(A):
            print idx
            n = 0
            ipadd = []
            for i in idx:
                num = A[n:n+i]
                print i, num
                if int(num) > 255 or (len(num) != 1 and num[0] == '0'):
                    break
                ipadd.append(num)
                n += i
            if len(ipadd) == 4:
                result.append(".".join(ipadd))
    return result       

print restoreIpAddresses("100100")