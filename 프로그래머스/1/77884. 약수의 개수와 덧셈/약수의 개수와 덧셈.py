# left 부터 right 까지의 모든 수들 중에서
# 약수의 개수가 짝수인 수는 더하고, 
# 약수의 개수가 홀수인 수는 뺀 수를 return 
def solution(left, right):
    answer = 0 
    for num in range(left, right+1) : # left ~ right 까지 순회
        cnt = 0 # 약수 개수 stacking
        for i in range(1, num+1) : # 값 하나씩 약수의 개수 파악
            if num % i == 0 : 
                cnt+=1
        if cnt % 2 == 0 :         # for 문 밖에서 약수의 개수 짝, 홀 판별 
            answer += num         # 짝수면 더하고, 홀수면 뺀다
        else : 
            answer -= num
                    
    return answer
