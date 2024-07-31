def solution(lottos, win_nums):
    answer = []

    # 최고 순위와 , 최저 순위

    dic = {6 : 1, 5 : 2, 4 : 3, 3 : 4, 2 : 5, 1 : 6, 0 : 6}

    for l in lottos : 
        if l in win_nums :
            answer.append(l)
    
    return dic[len(answer) + lottos.count(0)], dic[len(answer)]