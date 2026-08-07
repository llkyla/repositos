# How to calculate Fibonacci numbers using recursion functions

n = int(input())

def fibo1 (n):
    # Base case for Fibonacci sequence
    # F(0) = 0, F(1) = 0, F(2) = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    return fibo1(n - 1) + fibo1(n - 2)

'''
1. Base case can be more than 1
2. Setting base case = avoid max recursion depth exceeding error
'''

# OR ELSE to decrease time complexity:

def fibo2(n):
    global arr, cnt2
    cnt2 += 1

    if arr[n] != -1:
        return arr[n] # if the value is already computed, return it = replaced from -1 
        
        # n = 2 -> arr[2] = fibo2(1) + fibo2(0) = arr[2] = 1 + 0 = 1
        # n = 3 -> arr[3] = fibo2(2) + fibo2(1) = arr[3] = 1 + 1 = 2
        # n = 4 -> arr[4] = fibo2(3) + fibo2(2) = arr[4] = 2 + 1 = 3
    arr[n] = fibo2(n - 1) + fibo2(n - 2)
    print(arr)
    return arr[n]

arr = [-1] * (n + 1) # <- (1)
# ^ making [-1, -1, ..., -1] of size n + 1
ctn2 = 0
arr[0] = 0
arr[1] = 1 # <- (2) = [0, 1, -1, -1, ...., -1]

def main():
    print(f"Fibonacci of {n} is {fibo1(n)}; case 1")
    print(f"Fibonacci of {n} is {fibo2(n)}; case 2")
    print(ctn2)

print(main())
