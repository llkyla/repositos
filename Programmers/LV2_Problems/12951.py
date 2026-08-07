# 12951

# def solution(s):
#     tmp = [] 

#     for ch in s.split():
#         if ch.isalpha():
#             ch = ch[0].upper() + ch[1:].lower()
#         tmp.append(ch)
        
#     return ' '.join(tmp)

'''
^ does not work for s that has ' ' in a row
'''

def solution(s):
    res = [] 

    for i, ch in enumerate(s):
        if i == 0 or s[i-1] == ' ':
            res.append(ch.upper())
        else:
            res.append(ch.lower())
    return ''.join(res)

print(solution("3people unFollowed me"))
print(solution("for the last week"))

# or
def Jaden_Case(s):
    
    return s.title() # ∃ func .title()