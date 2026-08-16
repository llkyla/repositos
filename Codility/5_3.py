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

# no time error:
def solution(S, P, Q):
    N = len(S)
    M = len(P)

    prefixA = [0] * (N + 1)
    prefixC = [0] * (N + 1)
    prefixG = [0] * (N + 1)
    prefixT = [0] * (N + 1)

    for i in range(N):
        prefixA[i + 1] = prefixA[i] + (1 if S[i] == 'A' else 0)
        prefixC[i + 1] = prefixC[i] + (1 if S[i] == 'C' else 0)
        prefixG[i + 1] = prefixG[i] + (1 if S[i] == 'G' else 0)
        prefixT[i + 1] = prefixT[i] + (1 if S[i] == 'T' else 0)

    answers = [0] * M
    for k in range(M):
        p, q = P[k], Q[k]
        if prefixA[q + 1] - prefixA[p] > 0:
            answers[k] = 1
        elif prefixC[q + 1] - prefixC[p] > 0:
            answers[k] = 2
        elif prefixG[q + 1] - prefixG[p] > 0:
            answers[k] = 3
        else:
            answers[k] = 4

    return answers

print(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))