# 42586
# 25'05"

'''
progresses	                speeds	            return
[93, 30, 55]	            [1, 30, 5]	        [2, 1]
[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]
'''

def solution(progresses, speeds):
    answer = []
    tmp = []
    for i in range(len(progresses)):
        tmp.append((100-progresses[i])//speeds[i])
    #print(tmp)
    
    for i in range(len(tmp)):
        if (100 - progresses[i]) % speeds[i] != 0:
            tmp[i] += 1

    max_day = tmp[0]
    count = 1
    for i in range(1, len(tmp)):
        if tmp[i] <= max_day:
            count += 1
        else:
            answer.append(count)
            max_day = tmp[i]
            count = 1
    answer.append(count)

    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

# or
def solution(progresses, speeds):
    Q = []
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]