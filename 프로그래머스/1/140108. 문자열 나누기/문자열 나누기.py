def solution(s):
    answer = 0

    x = s[0]
    same = 0
    diff = 0 

    for idx, s_ in enumerate(s) : 

        if x == s_ : 
            same += 1
        else : 
            diff += 1

        if (same == diff) & (idx != len(s)-1) : 
            answer += 1 
            x = s[idx + 1]
            same = 0 
            diff = 0 

    return answer + 1