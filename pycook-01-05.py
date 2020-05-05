"""
1.5 Implementing a Priority Queue

Problem

You want to implement a queue that sorts items by a given priority and always
returns the item with the highest priorty on each pop operation.

Solution

The following class uses the heapq module to implement a simple priority queue.
"""

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self,item,priority):
        heapq.heappush(self._queue,(priority,self._index,item))
        self._index += 1
    
    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name) 

q = PriorityQueue()
q.push(Item('foo'), 4)       
q.push(Item('bar'), 2)
q.push(Item('spam'), 3)
print(q.pop())
print(q.pop())
print(q.pop())