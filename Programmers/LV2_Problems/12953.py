# 12953
'''
arr	        result
[2,6,8,14]	168
[1,2,3]	    6
'''
def solution(arr):

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    answer = 1
    for i in arr:
        answer = answer * i // gcd(answer, i)
        
    return answer

print(solution([2,6,8,14]))