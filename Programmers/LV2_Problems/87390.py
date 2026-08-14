# 87390 
# 34'55"

'''
n	left	right	result
3	2	    5	    [3,2,2,3]
4	7	    14	    [4,3,3,3,4,4,4,4]
'''

# out of time:
'''
def solution(n, left, right):
    # 1. make n by n matrix
    # 2. fill as:
    #       1 2 3 i i+1 i+2
    #       2 2 3 i+1 i+1
    #       3 3 3
    # 3. make it as [1,2,3],[2,2,3],[3,3,3] -> [1,2,3,2,2,3,3,3,3]
    tmp = []
    for i in range(1,n+1): # col
        for j in range(1,n+1): # row
            tmp.append(max(i,j)) # j = 1, 2, 3 for each when i=1, 2, 3
                                 # so fill in with max(i,j)
            #print(tmp)
    # 4. slice [left:right+1]
    return tmp[left:right+1]
'''

def solution(n, left, right):
    tmp = []
    for i in range(left, right+1):
        row = i // n # ∵ in [] every n sized row is appened, so q of n would be saved
        col = i % n 
        tmp.append(max(row,col) + 1)
    return tmp

print(solution(3,2,5))