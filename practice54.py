# generate all anagrams

word = "abcd"

def anagram(word):
    result = []
 #   print "<>", word
    if len(word) == 1:      
        return[word]

    for i in xrange(len(word)):
        subset = word[:i] + word[i+1:]
#        print word, subset, i
        result.extend(map(lambda x: word[i] + x, anagram(subset)))

    return result


result = anagram(word)
print len(result), result




"""
abcd
abdc
acbd
acdb
adcb
adbc
...


0123
abcd
 123
0 23
01 3
012
"""