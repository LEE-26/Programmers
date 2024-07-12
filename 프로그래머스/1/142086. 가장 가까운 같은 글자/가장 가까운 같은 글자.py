def solution(s):
    answer = [] 
    for i, s1 in enumerate(s) : 
        if i == 0 :
            answer.append(-1)
        else : 
            prior_str = [] # ['b', 'a', ...]
            for j in range(i) :
                prior_str.append(s[j]) # 비교하려는 문자들 , 기준 문자 앞의 문자들
            if s1 in prior_str : 
                max_index = max(list(filter(lambda x : prior_str[x] == s1, range(len(prior_str)))))
                answer.append(i - max_index)
            else :
                answer.append(-1)
    return answer