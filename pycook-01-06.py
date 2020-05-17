"""
Mapping Keys to Multiple Values in a Dictionary

Problem

You want to make a dictionary that maps keys to more than one value
(a so-called "multidict")

Solution

A dictionary is a mapping where each key is mapped to a single value.
If you want to map keys to multiple values, you need to store the multiple values
in another container such as a list or set.  For example, you might make
dictionaries like this:
"""

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

"""
defaultdict() will create a new key in the dictionary if it is accessed and 
does not yet exist.

To avoid this behaviour use the setdefault() method of a dictionary object
"""

d = {}
d.setdefault('a',[]).append(1)
d.setdefault('a',[]).append(2)
d.setdefault('b',[]).append(4)

pairs = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
pairs2 = {'key1':'value4', 'key2':'value5', 'key3':'value6'}
d = defaultdict(list)
for key in pairs:
    d[key].append(pairs[key])
for key in pairs2:
    d[key].append(pairs2[key])

print(d)
