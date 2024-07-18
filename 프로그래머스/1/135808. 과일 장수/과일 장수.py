def solution(k, m, score):
    # 만들 수 있는 상자 수
    n_box = len(score) // m
    n_box

    # 박스를 여러개 만들 수도 있음 .. 흠.. 
    # 높은 애들 부터 넣어야 함....

    score.sort(reverse=True) # 역순으로 정렬

    result = []
    if n_box > 0 : # 박스에 넣을 수 있으면,
        for idx in range(0, m*n_box, m) : # m : 박스안에 들어가는 사과 개수
            # print(idx, idx+m)
            result.append(min(score[idx:idx+m])*m)
    else : # box를 만들 수 없으면 return 0
        # print(0)
        return 0
    # print(sum(result))  
    return sum(result)