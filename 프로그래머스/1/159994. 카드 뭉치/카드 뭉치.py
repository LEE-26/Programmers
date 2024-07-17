def solution(cards1, cards2, goal) : 
    first_idx = 0

    for g in goal : 
        if cards1 and g == cards1[first_idx] : 
            cards1.pop(first_idx)
        elif cards2 and g == cards2[first_idx] : 
            cards2.pop(first_idx)
        else : return 'No'
    return 'Yes'