import random
import string

random.seed("zoe")

strList = []
for i in range(10):
    str1 = "".join([str(random.randrange(0, 9)) for _ in range(100)])
    print "\"%s\","%(str1)
print "\n"
for i in range(10):
    str1 = "".join([str(random.randrange(0, 9)) for _ in range(100)])
    print "\"%s\","%(str1)

print string.ascii_lowercase


upperlower = string.ascii_uppercase + string.ascii_lowercase

for _  in range(12):
    letters = []
    for i in range(26):
        offset = 26*random.randrange(2)
        letters.append(upperlower[i+offset])
    
    for i in range(26):
        ni = random.randrange(26)
        temp = letters[i]
        letters[i] = letters[ni]
        letters[ni] = temp
    #print "\""+ "".join(letters)+"\"," 

    word = []
    for _ in range(20):
        word.append(letters[random.randrange(26)])
    print "\""+ "".join(word)+"\"," 
