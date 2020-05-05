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
