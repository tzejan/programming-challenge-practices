#find if string contatins unique elements

def isUnique(s):
    index = 0
    for c in s:
        for i in range(index+1, len(s)):
            if c == s[i]:
                return False
        index += 1
    return True

print isUnique("abcdefghi")

def removeDup(s):
    sl = list(s)
    for i in range(len(sl)):
        if sl[i] != ' ':
            for j in range(i+1, len(sl)):
                if sl[i] == sl[j]:
                    sl[j] = ' ' 

    print "".join(sl)
    send = 0
    for i in range(len(sl)):
        if sl[i] == ' ':
            continue
        if send == i:
            send += 1
            continue
        sl[send] = sl[i]
        send += 1
    return "".join(sl[:send])

print removeDup("hello world")