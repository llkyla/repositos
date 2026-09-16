# 1902

def print_num_rev(n):
    if n == 0:
        return
    
    print(n)
    print_num_rev(n-1)
    

n = int(input())
print_num_rev(n)