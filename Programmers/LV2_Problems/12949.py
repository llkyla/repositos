# 12949
# 13'31"
'''
arr1	                            arr2	                            return
[[1, 4], [3, 2], [4, 1]]	        [[3, 3], [3, 3]]	                [[15, 15], [15, 15], [15, 15]]
[[2, 3, 2], [4, 2, 4], [3, 1, 4]]	[[5, 4, 3], [2, 4, 1], [3, 1, 1]]	[[22, 22, 11], [36, 28, 18], [29, 20, 14]]
'''

def solution(arr1, arr2):
    ans = []
    arr2t = [list(row) for row in zip(*arr2)] # zip(*arr2) = zip([5,4,3], [2,4,1], [3,1,1])

    for row1 in arr1:
        tmp = []
        for row2t in arr2t:
            val = sum(a*b for a,b in zip(row1, row2t))
            tmp.append(val)
        ans.append(tmp)

    return ans

print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],[[5, 4, 3], [2, 4, 1], [3, 1, 1]]))