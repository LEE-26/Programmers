# 정수 n
# 118372 -> 873211 
# 정렬
def solution(n):
    str_n = str(n)
    
    temp = [] # 1 1 8 3 7 2  
    
    answer = ''
    
    for s in str_n : 
        temp.append(int(s))
        
    temp.sort(reverse = True)
    
    for t in temp : 
        answer += str(t)
        
    return int(answer)