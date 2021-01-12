from collections import deque
import os 
import sys
import ast

file = open('text10.txt' , 'r')
d = file.read()
print(d)
#dictionary = ast.literal_eval(d) gia na to kano dictionary alla den mou douleuei 
#ua to metrage sosta an ginotan



def depth(d):
    queue = deque([(id(d), d, 1)])
    memo = set()
    while queue:
        id_, o, level = queue.popleft()
        if id_ in memo:
            continue
        memo.add(id_)
        if isinstance(o, dict):
            queue += ((id(v), v, level + 1) for v in o.values())
    return level


print(depth(d))
