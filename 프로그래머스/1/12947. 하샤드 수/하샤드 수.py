# 하샤드 수
# x의 자릿수의 합으로 x가 나누어져야 한다. 
# 18 -> 1 + 8 = 9 , 9는 18의 약수
def solution(x):
    # 18
    # i = 0, 1 (index)
    ha = 0
    for i in range(len(str(x))) : 
        ha += int(str(x)[i])
    
    if x % ha == 0:
        return True
    
    else : return False
