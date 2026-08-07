def solution(sizes):
    
    maxx = []
    minn = []
    
    for size in sizes:
        maxx.append(max(size))
        minn.append(min(size)) 
    answer = max(maxx) * max(minn)
    
    return answer
    