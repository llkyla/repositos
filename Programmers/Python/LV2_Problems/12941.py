# 12941

def solution(A,B):
    res = 0
    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        tmp = A[i] * B[i]
        res += tmp

    return res


print(solution([1, 4, 2],[5, 4, 4]))
print(solution([1,2],[3,4]))

# or
def getMinSum(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])