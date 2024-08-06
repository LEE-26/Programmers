# def solution(n, lost, reserve):
#     # 정렬
#     lost.sort()
#     reserve.sort()

#     # lost, reverse 에 공통으로 있는 요소 제거
#     # 잃어 버린 학생이 여벌의 체육복을 가져온 학생이면 빌려줄 수 없음
#     # 왜 ? 빌려줄 수 없는 학생들을 제거하기 위함
#     for i in reserve : 
#         if i in lost : 
#             lost.remove(i)
#             reserve.remove(i)

#     # 체육복 빌려주기 (앞번호부터)
#     for i in reserve : # 여벌의 체육복을 가져온 학생들
#         if i-1 in lost : # 앞번호 학생이 잃어버린 학생이면
#             lost.remove(i-1) # True 이면 elif 로 넘어가지 않고 다시 for 문으로 돌아감
#         elif i+1 in lost : # 뒷번호 학생이 잃어버린 학생이면
#             lost.remove(i+1)
            
#     return n - len(lost)

def solution(n, lost, reserve):
    reserve_set = set(reserve)-set(lost)
    lost_set = set(lost)-set(reserve)
    
    for r in reserve_set:
        if r-1 in lost_set:
            lost_set.remove(r-1)
        elif r+1 in lost_set:
            lost_set.remove(r+1)
            
    return n-len(lost_set)