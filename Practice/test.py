import re

testStr = "foo (bar ( new Point(x, graph.getY()) ));"

result = re.sub(r'([\(\)])', r' \1 ', testStr)
result = re.sub(r'\s+', r' ', result)

print testStr
print result

def printReverse(text):
    if len(text) == 1:
        return text        
    return printReverse(text[1:]) + text[0]
    
print printReverse(result)


#find anagram

#output 10 most frequent words

def generateStrings_(input):

    result = [""]
    
    for s in input:
        length = len(result)
        if s != '?':            
            #for idx, val in enumerate(result):                
            #    result[idx] = val + s
            for i in range(0, length):
                result[i] += s

        else:            
            result.extend(result)
            for i in range(0, length):
                result[i] += '0'
            for i in range(length, length*2):
                result[i] += '1'

    return result

#print generateStrings("10?10?")

def generateStrings(input):    
    if len(input) == 1:        
        if input != '?':
            return [input]
        else:
            return['0', '1']
    else:
        if input[-1] != '?':
            result = generateStrings(input[:-1])            
            for i in range(len(result)):
                result[i] += input[-1]
            return result
        else:
            result = generateStrings(input[:-1])
            length = len(result)
            for i in range(length):
                result[i] += '0'
                result.append(result[i]+'1')
            return result

    return []


#print generateStrings("10?10?")

def checkCorrectParenthesis(input):
    ppairs = {'(': ')', '{': '}', '<':'>', '[': ']'}

    stack = []

    for i in input:
        if i in ppairs:
            stack.append(i)
        else:
            if len(stack) == 0:
                return False

            if i != ppairs[stack.pop()]:
                return False

    if len(stack) > 0:
        return False

    return True

#print checkCorrectParenthesis("{()}")

def getKLargest(data, k):
    kLargest = []

    for i in data:
        if len(kLargest) < k:
            #insert i into kLargest sorted list
            kLargest.append(i)
        else:
            if i > kLargest[-1]:
                kLargest.pop()
                kLargest.append(i)
            else:
                continue

        for j in range(len(kLargest)-1, 0, -1):            
            if kLargest[j] > kLargest[j-1]:
                #swap
                temp = kLargest[j]
                kLargest[j] = kLargest[j-1]
                kLargest[j-1] = temp
            else:
                break

    return kLargest[-1]

data = [2,4,5,7,54,3,2,67,3,4,46]

k = 3
#print sorted(data)
#print data
#print getKLargest(data, 3)


m = re.match(r"(.+?)", "+ = /* lalalal */")
if m:
    print "matched", m.groups()

findAll = re.findall(r"([^\s]+)", "   using namespace void  int    int    void  int    void  void   int int   new int   int      int        int bool  true while               switch    case                        if         else if         else if         else     break  case       break case      break case    false  break default      break    void  int    int     int float float float                                                                       return  void  int                    return ")
if findAll:
    print "findAll", findAll
'''
import matplotlib.pyplot as plt
plt.figure(1)                # the first figure
plt.subplot(211)             # the first subplot in the first figure
plt.plot([1,2,3])
plt.subplot(212)             # the second subplot in the first figure
plt.plot([4,5,6])


plt.figure(2)                # a second figure
plt.plot([4,5,6])            # creates a subplot(111) by default

plt.figure(1)                # figure 1 current; subplot(212) still current
plt.subplot(211)             # make subplot(211) in figure1 current
plt.title('Easy as 1,2,3')   # subplot 211 title
#plt.show()
'''

import random
theList = range(10)
random.shuffle(theList)
print theList

print ">>>"

random.seed('Adela')
#random.seed('Jenny')
random.seed('Jessica')
#random.seed('Tammie')

for a in range(0, 5):    
    d = random.randrange(1, 32767)
    a = random.randrange(1, 100)
    n = random.randrange(7, 8) 
    series = [a+i*d for i in range(n)]
    if (series[-1] <= 0):
        lastNum = series[-1] - 1
        series = [n-lastNum for n in series]
    print "{%s},"%(", ".join(str(t) for t in series))
    print "{%d, %d, %d, %d},"%(series[2], series[-3], sum(series), len(series))

for i in range (0, 10):
    number = []
    for j in range (0, 4):
        v = random.randrange(0, 5)
        number.append(v)


    print "ASSERT_EQ(, ConvertToNumber(\"%dm%dc%dx%di\"));" % tuple(number)


for i in range (0, 10):
    numbers = []
    for j in range (0, random.randrange(5, 25)):
        numbers.append(random.randint(1,1000))
    
    #print "{" +  ",".join([str(num) for num in numbers]) + "},"
    lastFewSum = 0    
    lastfew = random.randrange(1, len(numbers))
    for k in range(lastfew, len(numbers)):
        lastFewSum += numbers[k]
    print "{%d, %d, %d, %d}," %(len(numbers) , lastFewSum, lastfew, len(numbers) - lastfew)
    


for i in range (0, 10):    
    print "ASSERT_EQ(0, LargestValueDigit(%d));  " % (random.randint(-2147483647, 0))


code = [104, 97, 99, 107, 101, 114, 116, 114, 97, 105, 108, 46, 99, 111, 109, 47, 105, 100, 97]

url = ""
for c in code:
    url += chr(c)

print url


import hmac
import base64
import hashlib 
import urllib


h = hmac.new("24181bf0970045259169cbbba5e92237", "GET\n\n\n\n/connect", hashlib.sha1)
a = base64.encodestring(h.digest()).rstrip()
print a
print urllib.quote(a)


class decorator(object):
    def __init__(self, func):
        print "in init()"
        self.func = func

    def __call__(self, *args, **kwargs):
        print 'instance %s of class %s this is now decorated whee!' % ( self.obj, self.cls )
        print "in call()"
        print self.obj.__name__
        print args, kwargs
        self.obj.obj = "haha"
        
        return self.func(self.obj, *args, **kwargs)

    def __get__(self, instance, owner):
        print "in get()"
        self.obj = instance
        self.cls = owner
        return self.__call__


class someClass(object):
    def __init__(self):
        self.obj = "lala"
        self.__name__ = "someClass"

    @decorator
    def funcA(self, inputText, input2):
        print "in funcA"
        print "obj", self.obj


sc = someClass()
print sc.obj
sc.funcA("wowowow", input2="mush")

authSchemePattern = r"MM-TOKEN"
base64Pattern =r"(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?"
authPattern = re.compile("^%s (%s):(%s)$" % (authSchemePattern, base64Pattern, base64Pattern))
m = authPattern.match("MM-TOKEN 86b81f313e684f28b369b992b6b88d44:XsKVTd9QbcpuRsLGj3f/GvP6b9U=")
if (m):
    print "yeah"
    print m.group(0)
    print m.group(1)
    print m.group(2)
else:
    print "nay"

userid = None
signature = None


from time import gmtime, strftime, time
print strftime("%Y-%m-%d %H:%M:%S", gmtime())
print gmtime()
now = gmtime(time() + 28800)

print now
nowstr = strftime("%Y-%m-%d %H:%M:%S", now)
print nowstr

