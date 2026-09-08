# 42842

'''
b b b b
b y y b
b b b b

y = (w - 2) * (h - 2)
w * h = b + y

brown	yellow	return
10	    2	    [4, 3] 
8	    1	    [3, 3]
24	    24	    [8, 6] <- we can see that return = divisors of (b + y)
'''
def solution(brown, yellow):
    tot = brown + yellow

    for h in range(1, int(tot ** 0.5) + 1):
        if tot % h != 0: # if h not divisor of tot
            continue # skip cuz make no sense

        w = tot // h
        
        if (w - 2) * (h - 2) == yellow:
            return[w, h]