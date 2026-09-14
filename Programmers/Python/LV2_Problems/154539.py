# 154539

def solution(numbers):
    res = [-1] * len(numbers)
    stack = []

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            index = stack.pop()
            res[index] = numbers[i]

        stack.append(i)

    return res


    
print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))