
# generate permuations of numbers

def genPermutations(number):
    num_str = str(number)

    def permutate(numbers):
        if len(numbers) == 1:
            return numbers

        permutations = []
        for i in range(len(numbers)):
            permutations.extend(numbers[i]+n for n in permutate(numbers[:i] + numbers[i+1:]) )
        return permutations

    p = permutate(num_str)
    results = [int(n) for n in p]
    return results


print genPermutations(123)

i = 0
string = "12345"
for i in range(len(string)):
    print string[:i] + string[i+1:]

print int((7199928 / (120 * 1.0))+0.5)
print int((77 / (2 * 1.0))+0.5)


print -7199928%120


