-- 코드를 입력하세요
# 가장 최근(늦게)에 들어온 동물은 언제 들어왔는지
SELECT DATETIME
FROM ANIMAL_INS
ORDER BY DATETIME DESC
LIMIT 1 