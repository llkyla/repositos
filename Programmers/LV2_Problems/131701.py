# 131701
# window sliding
'''
elements	result
[7,9,1,1,4]	18
'''

# 1st try:
'''
def solution(elements):
    sums = set()

    for size in range(1, len(elements) + 1): # size of subsequence
        for i in range(len(elements)): # idx of each sized subsequence
            s = sum(elements[(i+j) % len(elements)] for j in range(size))
            # for j in range(size):= idx of subseq
            # elements[(i+j) % n]:= i is start, j is increasing;
            #                       i+j can exceed len(ele) so % len(ele) since circle
            sums.add(s)

    return len(sums)
''' # takes too long

# 2nd try
def solution(elements):
    n = len(elements)
    sums = set()

    for size in range(1, n+1):
        s = sum(elements[0:size]) # for some size, get a sum of 1st section in size size
                                  # ex) size = 3, starts with [7,9,1]
        sums.add(s) # s = 17

        for i in range(1, n):
            s = s - elements[i-1] + elements[(i+size-1) % n] 
                    # elements[i-1] := leftest element pop
                    # elements[(i+size-1) % n] := new rightest elements comes in to sum in circle
            sums.add(s) # s = 11, 6, ...

    return len(sums)

