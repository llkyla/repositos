# 12939

def solution(s):

    tmp = list(map(int, s.split()))
    return "{0} {1}".format(min(tmp),max(tmp)) # also can be:
                                               # str(min(s)) + " " + str(max(s))

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))