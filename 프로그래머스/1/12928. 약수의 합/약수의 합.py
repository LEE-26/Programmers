def solution(n):
    # 약수 : 나눠지는 수
    # n
    answer = 0 
    for i in range(1, n+1) : 
        if n % i == 0 : 
            answer += i
    
    return answer