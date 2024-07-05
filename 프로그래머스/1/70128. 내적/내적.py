def solution(a, b):
    # a, b 배열
    answer = 0
    
    for i, j in zip(a, b) : 
        answer += (i*j)
            
    return answer