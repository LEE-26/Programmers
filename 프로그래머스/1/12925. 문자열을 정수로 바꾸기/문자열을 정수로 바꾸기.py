# 문자열 s를 숫자로 변환한 결과를 반환
# +, - 부호만 맨앞에 온다
# s 는 부호와 숫자로만 이루어져있다. 

def solution(s):
    
    
    if s[0] == '-' : 
        answer = int(s[1:])
        return -answer
    else :
        answer = int(s)
        return answer