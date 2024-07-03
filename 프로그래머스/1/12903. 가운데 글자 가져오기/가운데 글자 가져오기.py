def solution(s):
    # 123345
    if len(s) % 2 != 0 : 
        idx = len(s) // 2
        return s[idx]
    else : 
        idx = len(s)//2
        return s[idx-1:idx+1]