def solution(arr1, arr2):
    answer = [] 
    
    for a1, a2 in zip(arr1, arr2): # [1] , [2]
        answer_2 = []
        # print(a1, a2)
        for a1_1, a2_1 in zip(a1, a2) : 
            # print(a1_1, a2_1)
            # print(a1_1 + a2_1)
            answer_2.append(a1_1 + a2_1)
            
        answer.append(answer_2)
    
    return answer