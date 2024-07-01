def solution(t, p):
    len_p = len(p)
    sub_t = [] 
    for idx in range(len(t)) : # len(t) : 7, 0~6
        if idx+len_p <= len(t) : 
            sub_t.append(t[idx:idx+len_p])
        else : 
            break
    answer = 0 
    print(sub_t)
    for st in sub_t : 
        if int(st) <= int(p) : 
            answer += 1
    return answer
