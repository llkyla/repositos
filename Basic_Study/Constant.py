# Constant
## Square
a = 2
b = 3
print(a ** b) # <- 8 (2^3)

## Remainder
a = 7
b = 3
print(a % b) # <- 1 (7 /  3 = 2...1)
print(b % a) # <- 3 (3 / 7 = 0...3)

## Floor
a = 7
b = 4
print(a // b) # <- 1 (7 / 4 = 1...3)

# Assignment Operation 복합연산자
## from typing import Final # constant a = 1 하고싶은데 안됨
## a: Final = 1

a = 1

#a = a + 1 # a에 a + 1 다시 대입

a = 1
a += 1 # <- a = a + 1
print(a) # <- 2 

a = 1
a -= 1 # <- a = a - 1
print(a) # <- 0

a = 1
a *= 1
print(a) # <- 1

a = 1
a /= 1
print(a) # <- 1.0

a = 1
a //= 1
print(a) # <- 1 # 이외에 %= **=도 있음

a = 1
a %= 1
print(a) # <- 0

a = 1
a **= 1
print(a) # <- 1