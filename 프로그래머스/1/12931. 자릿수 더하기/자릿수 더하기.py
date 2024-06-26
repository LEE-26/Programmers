def solution(n):
    str_n = str(n)
    
    answer = 0
    for i in range(len(str_n)) : 
        answer += int(str_n[i])
    
    # 런타임 에러
    return answer

