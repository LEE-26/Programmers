def solution(n, m, section):
    answer = 0 
    painted = 0

    # s 칠해야 하는 영역 
    # m 한 번에 칠할 수 있는 길이
    for s in section : 
        if s > painted : 
            painted = s+m-1
            answer += 1 
    return answer