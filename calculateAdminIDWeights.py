def calCheckDigit(adminID, weights, offset):
    return (sum(map(lambda x, y:int(x)*y, adminID, weights)) + offset) % 23

def calculateAdminIDWeights():
    """
    NYP Admin ID consists of 6 digits and a check digit alphabet
    This will calculate the weights of 6 digits, plus a offset
    Assume weights range from 1-9
    offsets range from 0-9
    Checkdigits take their alphabet place

    Seems like the letters I, O and V are omitted from the checkdigit
    Total Checkdigits = 23

    """
    adminIDs = []

    with open("adminIDs.txt", 'r') as f:
        adminIDs = [line.strip() for line in f]

    checkdigits = set()
    for id in adminIDs:
        checkdigits.add(id[6])

    # now checkdigits is an ordered list contaning the checkdigits
    checkdigits = sorted(checkdigits)
    
    weights = [1, 1, 1, 1, 1, 1]
    offset = 1
    for i in xrange(1111111,10000000):
        n = i
        offset = n % 10
        n /= 10
        
        for c in range(5, -1, -1): 
            weights[c] = n % 10
            n /= 10

        if i % 100000 == 0:
            print weights, offset

        count = 0
        for adminID in adminIDs:           
            cd = 22 - calCheckDigit(adminID[:6], weights, offset)
            if checkdigits[cd] == adminID[6]:
                # if the checkdigit matches, try the next adminID
                count += 1
                if count % 5 == 0:
                    print adminID, weights, offset, cd, checkdigits[cd]
                if count > 1000:
                    return
                continue
            else:
                # else break the admin number loop and try with another set of weights and offsets
                break
          



calculateAdminIDWeights()