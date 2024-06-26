def solution(x, n):
    # 정수 x
    # 자연수 n 
    # x부터 시작해 x 씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 한다.
    answer = []
    
    # if x > 0 : 
    #     for i in range(x , (x*n)+1, x) : 
    #         answer.append(i)
    # else : 
    #     for i in range(x, (x*n)-1, x) : 
    #         answer.append(i)
    for i in range(1, n+1) : 
        answer.append(x*i)
                
    return answer