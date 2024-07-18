def solution(answers):
    len_answers = len(answers)

    supo1_pattern = [1, 2, 3, 4, 5] # 요걸 0, 1, 2, 3, 4 -> 0, 1, 2, 3, 4 이렇게 반복시켜야함.
    supo2_pattern = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3_pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 각 수포자들의 정답지 
    supo1_score = sum([supo1_pattern[idx%len(supo1_pattern)] == answers[idx] for idx in range(len_answers)])
    supo2_score = sum([supo2_pattern[idx%len(supo2_pattern)] == answers[idx] for idx in range(len_answers)])
    supo3_score = sum([supo3_pattern[idx%len(supo3_pattern)] == answers[idx] for idx in range(len_answers)])

    scores = [supo1_score, supo2_score, supo3_score]
    maxi = max(scores)
    
    return [idx + 1 for idx,val in enumerate(scores) if val == maxi]