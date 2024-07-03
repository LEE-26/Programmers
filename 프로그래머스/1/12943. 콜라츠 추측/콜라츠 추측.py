def solution(num):
    answer = 0
    
    # 주어진 수가 1인 경우 0 return
    if num == 1:
        return 0
    
    while True:
        num = num/2 if num % 2 == 0 else (num*3)+1
        answer += 1
        # num 이 1이 되거나 answer 가 500이 넘어가면 멈추기
        if num == 1:
            return answer 
        elif answer == 500:
            return -1
    
    return answer