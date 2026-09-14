# 84512

def solution(word):
    vowels = ['A', 'E', "I", "O", "U"]
    pers = [781, 156, 31, 6, 1] # after 1st place there can be 5^4 + 5^3 + 5^2 + 5^1 + 5^0 = 781
                                # after 2nd place there can be       5^3 + 5^2 + 5^1 + 5^0 = 156

    res = 0

    for i in range(len(word)):
        res += vowels.index(word[i]) * pers[i] + 1

    return res

print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))