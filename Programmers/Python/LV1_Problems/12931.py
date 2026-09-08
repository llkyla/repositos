# 12931

def solution(n):
    
    ans = 0
    
    n = str(n)
    
    for i in range(len(n)):
        a = int(n[i])
        ans += a

    return ans

# or
def sum_digit(number):
    return sum(map(int, str(number))) # map(int, str(number)) = type change number to str, and make it as int
                                      # sum() = add all