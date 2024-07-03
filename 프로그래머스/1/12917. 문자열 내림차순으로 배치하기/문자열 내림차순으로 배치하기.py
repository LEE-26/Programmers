def solution(s):
    
    ls = [e for e in s]
    ls.sort(reverse = True)
    answer = ''.join(ls)

    return answer