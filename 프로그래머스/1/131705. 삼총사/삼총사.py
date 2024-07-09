def solution(number):
    # 3명의 정수를 더했을 때 0이 되면 3명의 학생을 삼총사라고 한다. 
    # 삼총사를 만들 수 있는 방법의 수를 return
    
    answer = 0
    for i in range(len(number)) : 
        for j in range(i+1, len(number)) : 
            for k in range(j+1, len(number)) : 
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer