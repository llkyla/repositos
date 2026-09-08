# queue

from collections import deque

# call queue
q = deque()

# appending 
q.append(10)
q.append(20)
q.append(30)

print(q) # deque([10, 20, 30])

# removing from the left
removed_element = q.popleft()
print("deleted:", removed_element)
print("after deleting:", q)
print()

# leftest element
front_element = q[0]
print("leftest element:", front_element)
print("curr q:", q)
print()

# len(q)
print("len q:", len(q))
print()

# in or no
print(10 in q)
print(20 in q)
print()

# loop
while q:
    print(q.popleft(), end=' ')