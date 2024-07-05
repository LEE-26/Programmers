# arr의 각 element 중 divisor로 나누어 떨어지는 값을 (오름차순)으로 정렬한 배열을 반환하는 함수, 
# divisor 로 나누어 떨어지는 element 가 하나도 없다면 배열에 -1을 담아서 반환
def solution(arr, divisor):
    answer = []
    for arr_ in arr : 
        if arr_ % divisor == 0 : 
            answer.append(arr_)
    if len(answer) < 1 : 
        return [-1]
    else : 
        answer.sort()
        return answer   