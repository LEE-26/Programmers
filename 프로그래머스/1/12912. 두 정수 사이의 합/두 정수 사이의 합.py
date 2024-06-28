# a, b 는 정수 
# a 와 b 사이에 속한 모든 정수의 합을 리턴
def solution(a, b):
    answer = 0
    for i in range(min(a,b), max(a,b)+1) : 
        answer += i 
    return answer