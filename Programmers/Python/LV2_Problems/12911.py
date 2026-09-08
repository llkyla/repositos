# 12911

def solution(n):

    one = bin(n).count('1')
    num = n + 1
    
    while bin(num).count('1') != one:
        num += 1

    return num

print(solution(78))
print(solution(15))

# or
'by using bit'
'''
n이 매우 커지는 경우를 대비해, 반복 없이 비트 연산만으로 "다음 큰 숫자"를 즉시 계산하는 규칙도 존재합니다. 핵심 아이디어는 다음과 같습니다.

n의 오른쪽에서부터 연속된 0들을 찾고, 그다음 나오는 1을 찾습니다.

그 1을 0으로 바꾸고, 그 바로 위 자리를 1로 바꿉니다(즉 그 1을 한 자리 위로 옮김).

그보다 오른쪽에 있던 나머지 1들은 모두 가장 오른쪽으로 몰아서 채웁니다.
'''

def solution(n):
    c = n & (-n)        # n에서 가장 오른쪽에 있는 1비트만 추출
    r = n + c            # 그 1비트를 한 단계 위로 올림 (자리올림 발생)
    answer = (((r ^ n) // c) >> 2) | r
    return answer

print(solution(78))  # 83