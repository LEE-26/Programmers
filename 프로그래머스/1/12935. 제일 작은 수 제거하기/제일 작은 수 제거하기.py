def solution(arr):
    if len(arr) > 1:    
        arr.sort(reverse = True)
        arr_pop = arr.pop(-1)
        return arr
    else : 
        return [-1]
    
def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))
        return arr
    else:
        return [-1]