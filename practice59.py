def get_middle(str):
  mid = len(str) / 2
  print mid
  if len(str) % 2:
    print "here"
    return str[mid]
  else:
    print "even"
    return str[mid-1:mid+1]


print get_middle("t")

c = 't'
print c.upper()
#print "test"[2:4]


d = {1:1, 2:2, 3:3}

it = iter(d.values())
v = it.next

print v
"""

  
  letter_counts = {}
  
  for c in s:
    if c not in letter_counts:
      letter_counts[c] = 0
    letter_counts[c] += 1
    
  values_list = list(letter_counts.values())
  count = values_list[0]
  
  if count == 1:
    return True
  
  print (s, values_list)
  for v in values_list[1:]:
    if v != count:
      return True
  
  return False
  """


import re
val = '####### Snow White and the Seven Hashtags'
m = re.search('^\s*?(#+) (.+)', val)
print m.group(0), m.group(1)
text = m.group(2)
text = text.rstrip()
print "|"+text+"|"

string = 'fdsyffdsyffdsyffdsyffdsyf'

idx = 5
search = string[:idx]
print search
print string[idx:].find(search)

