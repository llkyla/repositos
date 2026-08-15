##

def solution(S, P, Q):
    # Implement your solution here
    pass
    dict = {'A':1, 'C':2, 'G':3, 'T':4}
    n = len(P)
    ans = []

    for k in range(n):
        p = P[k]
        q = Q[k]
        min_val = 5  # max(dict factor) = 4
        for i in range(p, q + 1):
            val = dict[S[i]]
            if val < min_val:
                min_val = val
        ans.append(min_val)

    return ans

print(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))