# 12947

def solution(x):
    temp = 0
    y = str(x)
    
    for i in range(len(y)):
        z = int(y[i])
        temp += z
        
    if x % temp == 0:
        return True
    else:
        return False
