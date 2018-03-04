#substitution cipher

import string

key = string.ascii_lowercase
lookup = string.ascii_uppercase

cipher = {}
for l in list(string.ascii_lowercase):
    for i in range(26):
        if key[i] == l:
            cipher[l] = lookup[i]
            continue

#encode
encoded = ""
source = "hellokitty"
for l in source:
    encoded += cipher[l]

print encoded
