
"""
Problem

You want to keep a limited history of the last few items seen during iteration or during 
some other kind of processing.

Solution

Keeping a limited history is a perfect use for a collections.deque.  For example, the 
following code performs a simple text match on a sequence of lines and yields the matching
line along with the previous N lines of context when found:

"""

from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f,'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)
    print(__name__)
