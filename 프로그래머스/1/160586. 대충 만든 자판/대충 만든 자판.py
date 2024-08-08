def solution(keymap, targets):
    answer = []

    for target in targets : # 'ABCD', 'AABB'
        cnt = 0
        for idx, t in enumerate(target) : # 'A', 'B', 'C', 'D'
            try : 
                n_typing = min([key.find(t) for key in keymap if t in key]) + 1  # 0, 0, 1, 4
            except : 
                cnt = -1
                break 
            else : 
                cnt += n_typing # 0부터 시작하니까 +1

        answer.append(cnt)
        
    return answer