# 2650

def gcd(a, b):
    while b:
        a, b = b, a % b

    return a

a, b, c = map(int, input().split())

print(gcd(gcd(a,b), c))

'''
import math

a, b, c = map(int, input().split())

res = math.gcd(math.gcd(a,b),c)

print(res)

'''