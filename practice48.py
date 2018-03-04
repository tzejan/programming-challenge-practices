#t = int(raw_input())
#n = map(int, raw_input())

t = 2
n = [3, 15]

for tn in n:
    for i in range(1, tn+1):
        if (i % 3 == 0 or i % 5 == 0):
            if ( i % 15 == 0):
                print "FizzBuzz"
            elif (i % 3 == 0):
                print "Fizz"
            elif (i % 5 == 0):
                print "Buzz"
        else:
            print i