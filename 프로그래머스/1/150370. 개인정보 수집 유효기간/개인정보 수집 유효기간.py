# 날짜를 일수로 변환 
def to_days(date) : 
    y, m, d = map(int, date.split('.'))
    return y*12*28 + m*28 + d

def solution(today, terms, privacies) :
    answer = [] 
    today = to_days(today)
    
    # 약관 정보 
    term = dict()
    for t in terms : 
        type_, period = t.split()
        term[type_] = int(period)*28
    
    # 개인정보 만료기간과 오늘 일수를 비교하여 파기 목록에 추가
    for idx, p in enumerate(privacies) : 
        numb = idx+1
        date, type_ = p.split()
        
        # 오늘 보다 만료기간이 짧으면 파기
        if to_days(date) + term[type_] - 1 < today : # -1 : 만료일까지 포함 , 예시) 2022.01.01 시작 + 28일 = ~2022.01.28 계약을 한 시점을 포함해 28일이기 때문
            answer.append(numb)
    
    return answer 