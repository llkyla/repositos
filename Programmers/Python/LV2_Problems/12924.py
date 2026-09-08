# 12924

def solution(n):
    cnt = 0
    
    for i in range(1, n+1, 2):
        if n % i == 0:
            cnt += 1

    return cnt

print(solution(15))

'''
number of sum of continuous N = number of odd divisors of N

proof.
Let
    a := 1st ℕ of continuous ℕ
    k := number of ℕ to be added.
    Then,
    n = a + (a+1) + (a+2) ... (a+k-1) ...(1)

By using the formula of sum of arithmetic sequence on (1):
    n = k(2a + k - 1) / 2 ...(2)

Multiplying 2 on both sides of (2) gives:
    2n = k(2a + k - 1) ...(3)
    Here in (3), k is number of ℕ, and (2a + k - 1) is another ℤ. 
    Now we know that k is divisor of 2n.
    In (3), for (2a + k - 1) part, we know that 2a is always even; we know that 


'''