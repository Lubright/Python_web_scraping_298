from collections import OrderedDict
from collections import defaultdict


dict1 = {}
dict1['a'] = 2
dict1['b'] = 3
dict1['c'] = 2
dict2 = defaultdict(list)
for k, v in dict1.items():
    dict2[v].append(k)
print(dict2)

for k in sorted(dict2, reverse=True):
    print(k, ':', dict2[k])
