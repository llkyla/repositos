# 1901

def print_num(n):
    if n == 0:
        return

    print_num(n-1)
    print(n)

n = int(input())
print_num(n)