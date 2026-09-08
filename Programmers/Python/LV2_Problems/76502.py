# 76502
'''
s	        result
"[](){}"	3
"}]()[{"	2
"[)(]"	    0
"}}}"	    0
'''

def solution(s):
    def valid(s):
        stack = []
        parenthesis = {')':'(', ']':'[','}':'{'}
        for p in s:
            if p in '([{':
                stack.append(p)
            else:
                if not stack or stack[-1] != parenthesis[p]: 
                    # stack[-1] != parenthesis[p]:= see if current closing one has its own opening one in the stack
                    return False
                stack.pop()
        return len(stack) == 0 # return only True = when len(stack) == 0

    count = 0
    for i in range(len(s)):
        rotated = s[i:] + s[:i]
        if valid(rotated):
            count += 1

    return count

print(solution("[](){}"))