# players = ["mumu", "soe", "poe", "kai", "mine"]
# callings = ["kai", "kai", "mine", "mine"]
# result = ["mumu", "kai", "mine", "soe", "poe"]

# 1등부터 3등까지 "mumu", 'soe', 'poe'


def solution(players, callings):
    
    result = {player : i for i, player in enumerate(players)} # 선수 : 등수
    for who in callings :
        idx = result[who] # 호면된 선수의 현재 등수
        result[who] -= 1 # 하나 앞 등수로 바꿔줌
        result[players[idx - 1]] += 1 # 앞에 위치했던 선수의 등수 +1
        players[idx-1] , players[idx] = players[idx], players[idx-1] # 위치 변경

        
        # idx = players.index(c) # index : 전체를 조회하기 때문에, 시간복잡도가 높음. 사용 지양
        # players.insert(idx-1, players.pop(idx))
        
    return players