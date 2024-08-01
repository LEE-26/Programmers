def solution(babbling):
    baby = ["aya", 'ye', 'woo', 'ma']
    answer = 0
    
    for bab in babbling:
        original_bab = bab  # 원래 문자열 저장
        valid = True

        for b in baby:
            if b+b in bab:  # 연속된 문자열이 있는 경우
                valid = False
                break

        if valid:  # 연속된 문자열이 없는 경우에만 진행
            for b in baby:
                bab = bab.replace(b, ' ')
            bab = bab.replace(' ', '')  # 공백 제거

            if len(bab) == 0:  # 모든 문자열이 baby의 조합으로만 이루어진 경우
                answer += 1
    
    return answer