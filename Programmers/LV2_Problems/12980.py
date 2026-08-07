# 12980
'''
N	    result
5	    2 
6	    2 
5000	5
'''
def solution(n):

    return bin(n).count('1')

print(solution(5))
print(solution(6))
print(solution(5000))

# or
'''
def solution(n):
    answer = 1
    while n > 1:
        answer += n % 2
        n = n // 2
    return answer
'''