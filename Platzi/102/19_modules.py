import sys
print(sys.path)

import re
text = 'Mi numero es el 311 123 121, el codigo es 57 y mi nuemto es 3'
result = re.findall('[0-9]+', text)
print(result)

import time
timestamp = time.time()
local= time.localtime()
result = time.asctime(local)
print(result)

#collections para manejar listas
import collections
numbers = [1,2,3,4,1,2,3,1,2,3,4,5,55]
counter = collections.Counter(numbers)
print(counter)




