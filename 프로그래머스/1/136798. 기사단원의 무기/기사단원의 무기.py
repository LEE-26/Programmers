def solution(number, limit, power):
    # 약수 개수를 저장할 리스트 초기화
    ls2 = [0] * (number + 1)

    # 각 숫자의 약수 개수 계산
    # 외부 루프 : i 가 1부터 numbrer 까지 각 숫자를 순회
    # 내부 루프 : j 가 i부터 i의 배수인 숫자를 순회
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            ls2[j] += 1

    # 결과 계산
    result = [power if l2 > limit else l2 for l2 in ls2[1:]]
    answer = sum(result)
    
    
    return answer