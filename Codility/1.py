def solution(N):
    # Implement your solution here
    num = bin(N)[2:]
    tmp = num.strip('0').split('1')
    print(tmp)
    length = list(len(t) for t in tmp if t != '')
    return max(length) if length else 0

print(solution(1041))
print(solution(32))
# print(solution(15))
