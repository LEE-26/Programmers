def solution(s):
    
    split_ls = s.split(' ')
    # 단어별로 짝/홀 인덱스
    result = []
    for sl in split_ls : 
        string_ls = [s_.upper() if idx % 2 == 0 else s_.lower() for idx, s_ in enumerate(sl)]
        result.extend(string_ls)
        result.extend(" ")
    
    answer = ''.join(result)[:-1]
    return answer