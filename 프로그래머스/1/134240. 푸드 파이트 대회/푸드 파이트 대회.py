def solution(food) : 
    answer = ''
    for i, f in enumerate(food) :  
        answer += str(i) * (f // 2)

    answer += '0'

    reverse_answer = ''
    for c in answer[:-1] :
        '122333'
        reverse_answer = c + reverse_answer

    answer = answer + reverse_answer
    return answer