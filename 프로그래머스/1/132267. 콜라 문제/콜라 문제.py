def solution(a, b, n):
    cnt = 0
    answer = 0 # 총 return 받은 병 개수
    total = n

    while total >= a : # 줄 수 없을 때 까지 줘야 하는 개수보다 적게 가지고 있으면 못 주니까
        return_item, remain = divmod(total, a) # 몫, 나머지
        return_item, remain = return_item*b, remain
        # print(return_item, remain)

        answer += return_item

        total = return_item + remain
        cnt += 1
    
    return answer