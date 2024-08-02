## <<시간초과 코드>>
# def solution(X, Y):
#     answer = []

#     X_list = list(X)
#     Y_list = list(Y)

#     for x in X_list : 
#         if x in Y_list : 
#             answer.append(x)
#             Y_list.remove(x) # remove() : 리스트에서 첫 번째로 나오는 x를 삭제

#     if len(answer) != 0 :
#         answer.sort(reverse=True)
#         result = ''.join(answer)
#         if set(result) == set('0') : 
#             return '0'
#         else : 
#             return result
        
#     else : 
#         return '-1'
def solution(X, Y):
    result = ''
    X_list = [0] * 10
    Y_list = [0] * 10

    for x in X :
        X_list[int(x)] += 1
    for y in Y : 
        Y_list[int(y)] += 1

    # print(X_list, Y_list)

    for i in range(9, -1, -1) : 
        if X_list[i] > 0 and Y_list[i] > 0 : 
            result += str(i) * min(X_list[i], Y_list[i]) # 둘 중 작은 수만큼 추가 : 공통으로 나타나는 수
    if result == '' :
        return '-1'
    elif result[0] == '0':
        return '0'
    else : 
        return result