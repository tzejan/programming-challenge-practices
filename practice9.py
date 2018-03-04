def reverseString(s):
    result = ""
    for i in range(len(s)-1, -1, -1):
        result += s[i]

    return result


def rstring(s):
    if len(s) == 1:
        return s

    return rstring(s[1:]) + s[0]

print reverseString("abcdef")
print rstring("abcdef")

sl = list("wahah")
print sl