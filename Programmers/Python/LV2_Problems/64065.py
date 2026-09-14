# 64065

def solution(s):
    s = s[2:-2]
    s = s.split('},{')
    s = [list(map(int, x.split(","))) for x in s]
    s.sort(key=len)

    res = []

    for numbers in s:
        for num in numbers:
            if num not in res:
                res.append(num)

    return res

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
