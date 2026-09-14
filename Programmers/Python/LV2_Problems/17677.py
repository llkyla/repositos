# 17677

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    s1 = []
    s2 = []

    for i in range(len(str1)-1):
        window1 = str1[i:i+2]
        if window1.isalpha():
            s1.append(window1)

    for i in range(len(str2)-1):
        window2 = str2[i:i+2]
        if window2.isalpha():
            s2.append(window2)

    if len(s1) == 0 and len(s2) == 0:
        return 65536

    cap = 0
    tmp = s2.copy()

    for x in s1:
        if x in tmp:
            cap += 1
            tmp.remove(x)

    cup = len(s1) + len(s2) - cap

    res = int(65536 * (cap / cup))

    return res

print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))
