def reverseString(s):
    sl = list(s)

    for i in range(len(sl)/2):
        temp = sl[i]
        sl[i] = sl[-i-1]
        sl[-i-1] = temp

    return "".join(sl)


def reverseString2(s):
    sl = list(s)
    slen = len(sl)

    for i in range(slen/2):
        temp = sl[i]
        sl[i] = sl[slen-i-1]
        sl[slen-i-1] = temp

    return "".join(sl)

print reverseString("hello hallo")
print reverseString2("hello hallo")

