# 120585
def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1
    return answer

# 120583
def solution(array, n):
    count = 0
    for a in array:
        if a == n:
            count += 1
    return count