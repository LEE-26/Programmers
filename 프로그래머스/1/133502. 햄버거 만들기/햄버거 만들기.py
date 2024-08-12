def solution(ingredient):
    # ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
    # result = 2 : 햄버거의 개수

    hamburger = []
    cnt = 0

    for i in ingredient : 
        hamburger.append(i)
        if hamburger[-4:] == [1, 2, 3, 1] : # 뒤에서 부터 4개가 완성되는 조합이면 
            cnt += 1
            for _ in range(4) : # 완성된 조합은 제거, pop() 4번, pop은 리스트의 마지막 요소를 제거
                hamburger.pop()
    # print(cnt)
    return cnt