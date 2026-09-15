# 42839
from itertools import permutations
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False

    return True

def solution(numbers):
    ans = set()

    for length in range(1, len(numbers)+1):
        for p in permutations(numbers, length):
            num = int(''.join(p))

            if is_prime(num):
                ans.add(num)

    return len(ans)

print(solution("17"))
print(solution("011"))

'''
dfs structure

for all_possible_cases:
    if condition:
        ans += 1
'''