def solution(survey, choices):
    # survey = ["AN", "CF", "MJ", "RT", "NA"]
    # choices = [5, 3, 2, 7, 5]
    # result = "TCMA"
    
    category = {"R" : 0,
                "T" : 0,
                "C" : 0, 
                "F" : 0,
                "J" : 0,
                "M" : 0,
                "A" : 0,
                "N" : 0}

    score = {'1' : 3,
             '2' : 2,
             '3' : 1,
             '4' : 0,
             '5' : 1,
             '6' : 2,
             '7' : 3}

    for s, c in zip(survey, choices) : # "AN", 5
        if c < 4 :
            category[s[0]] += score[str(c)]
        else :
            category[s[1]] += score[str(c)]

    # 단, 하나의 지표에서 각 성격 유형 점수가 같으면, 두 성격 유형 중 사전 순으로 빠른 성격 유형을 검사자의 성격 유형이라고 판단합니다.
    # RT, CF, JM, AN
    result = ''
    pairs = ["RT", "CF", "JM", "AN"]

    for p in pairs:
        if category[p[0]] == category[p[1]]:
            result += sorted(p)[0]
        else:
            result += max(p, key=lambda x: category[x])
    return result