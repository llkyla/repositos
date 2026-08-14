##

def solution(N, A):
    # Implement your solution here
    counters = [0] * N
    max_val = 0 # max val after increase(); standard of maxCounter()
    last_max = 0 # num of max when latest maxCounter() tried 

    for x in A:
        if x <= N:
            if counters[x-1] <= last_max: # if counters[x-1] never changed after maxCounter()
                counters[x-1] = last_max  # update to the latest
            counters[x-1] += 1 # increase()
            max_val = max(max_val, counters[x-1]) # if increased > max_val before, update
        else:
            last_max = max_val # save the max of now rather than rlly change the list

    for i in range(N):
        if counters[i] < last_max:
            counters[i] = last_max # update all vals that may if not went thru 

    return counters

    
print(solution(5, [3, 4, 4, 6, 1, 4, 4]))