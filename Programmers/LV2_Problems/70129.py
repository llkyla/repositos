# 70129

def solution(s):
    count = 0
    zero = 0

    while s != '1':
        zero += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        count += 1

    return [count, zero] 

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))