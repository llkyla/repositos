# 12909

def solution(s):
    stack = []
    
    for p in s:
        stack.append(p)
        
        if len(stack) >= 2 and stack[-2:] == ['(', ')']: 
            stack.pop() 
            stack.pop() 

    return True if len(stack) == 0 else False 

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))



# more efficient version 
'''
∵ if ')' comes in to stack, it immediately pop
  = so just stack '(' in stack
'''

def solution(s):
    stack = []
    
    for p in s:

        if p == '(':
            stack.append(p)

        else:
            if not stack: # case of 1st p = )
                return False # always False if parenthesis starts with )
            stack.pop() # else pop
    
    return not stack # ∵ stack empty = () all made
                     #   but Python automatically thinks empty = False
                     #   so return not stack