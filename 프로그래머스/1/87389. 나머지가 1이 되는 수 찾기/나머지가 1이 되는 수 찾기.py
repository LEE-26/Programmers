def solution(n):
    # 매개변수
    # n 을 x 로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x 를 return
    answer = 0
    for x in range(1, n+1):
        if n % x == 1 : 
            answer += x
            break
    return answer