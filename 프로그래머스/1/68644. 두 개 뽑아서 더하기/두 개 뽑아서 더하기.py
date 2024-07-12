def solution(numbers):
    answer = []

    for i in range(len(numbers)-1) : # 0, 1, 2, 3
        for j in range(len(numbers)-1) : # 1, 2, 3, 4 
            if i == j+1 : 
                continue
            answer.append(numbers[i] + numbers[j+1])

    result = list(set(answer))
    result.sort()
    
    return result