# 길이가 n 
# 수박 ;;; 
# 홀, 짝으로 접근
def solution(n):
    # n = 3
    answer = ''
    for i in range(1, n+1) : # 1, 2, 3 
        if i % 2 != 0: 
            answer+='수'
            
        else : 
            answer+='박'
    
    return answer

solution(3)