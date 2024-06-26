# <<오답 처리>>

# def solution(n):
#     answer = []
    
#     str_n = str(n)
    
#     for s in str_n : 
#         answer.append(int(s))
#     answer.sort(reverse = True)    
#     return answer
    
def solution(n):
    answer = []
    
    for i in range(1, len(str(n))+1) : 
        answer.append(int(str(n)[-i]))
    return answer
    