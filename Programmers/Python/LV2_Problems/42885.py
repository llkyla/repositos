# 42885

'''
people	            limit	return
[70, 50, 80, 50]	100	    3
[70, 80, 50]	    100	    3
'''

def solution(people, limit):
    people.sort() # 5 5 7 8
    light, heavy = 0, len(people) - 1
    count = 0

    while light <= heavy:
        if people[light] + people[heavy] <= limit:
            light += 1
        heavy -= 1
        count += 1

    return count

print(solution([70, 50, 80, 50], 100))

# or 
'''
from collections import deque

def solution(people, limit):
    result = 0
    deque_people = deque(sorted(people))

    while deque_people:
        left = deque_people.popleft()
        if not deque_people:
            return result + 1
        right = deque_people.pop()
        if left + right > limit:
            deque_people.appendleft(left)
        result += 1
    return result
    
'''