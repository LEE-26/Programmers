def solution(numbers):
    zero_to_nine = [x for x in range(0,10)]
    
    for e in numbers :
        if e in zero_to_nine : 
            zero_to_nine.remove(e)
            
    answer = sum(zero_to_nine)
                
    return answer