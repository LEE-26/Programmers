# def solution(arr):
#     arr.sort(reverse = True)
#     arr_pop = arr.pop()
#     if len(arr) < 1:
#         return [-1]
#     else : 
#         return arr

def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))
        return arr
    else:
        return [-1]