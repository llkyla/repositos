##

def solution(A):
    # Implement your solution here
    east_cnt = 0
    tot_cnt = 0

    for i, d in enumerate(A):
        if d == 0:
            east_cnt += 1
        else:
            tot_cnt += east_cnt
            if tot_cnt > 1000000000:
                return -1

    return tot_cnt


print(solution([0, 1, 0, 1, 1]))

# for this one, not necessarily use enumerate