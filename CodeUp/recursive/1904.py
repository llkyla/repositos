# 1904
# a = 2 b = 7 [2, 7]

def f(a, b):

    if a > b:
        return

    if a % 2 != 0:
        print(a, end=' ')
        a = a + 2

    else:
        a = a + 1
    
    f(a, b)
        


a, b = map(int, input().split())

f(a, b)