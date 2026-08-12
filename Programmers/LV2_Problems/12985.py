# 12985

'''
N	A	B	answer
8	4	7	3
'''
def solution(n,a,b):
    count = 0
    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2
        count += 1

    return count

print(solution(8, 4, 7))