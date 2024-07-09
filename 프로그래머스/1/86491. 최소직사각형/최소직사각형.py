def solution(sizes):
    width = 0 
    height = 0
    
    for s in sizes : 
        w = max(s)
        h = min(s)
        
        if width < w : 
            width = w
        if height < h : 
            height = h  
    
    answer = width * height
    
    return answer