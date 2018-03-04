#big add 2


def bigAdd2(num1, num2):
    offset = abs(len(num1)-len(num2))

    bigger = num1
    smaller = num2
    if (len(smaller) > len(bigger)):
        smaller = num1
        bigger = num2

    result = ""

    for i in range(len(bigger)-1, -1, -1):
        carry = 0
        nsum = int(bigger[i]) + int(smaller[i-offset]) + carry
        carry = nsum / 10
        result += str(nsum % 10)

    return result[::-1]


print bigAdd2("123", "12")