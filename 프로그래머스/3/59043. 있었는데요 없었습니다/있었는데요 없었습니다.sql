-- 코드를 입력하세요

# 일부 동물의 입양일이 잘못 입력
# 보호 시작일보다 입양일이 더 빠른 동물의 (아이디, 이름 조회)
SELECT i.ANIMAL_ID, i.NAME
FROM ANIMAL_INS i LEFT JOIN ANIMAL_OUTS o ON i.ANIMAL_ID=o.ANIMAL_ID
WHERE i.DATETIME > o.DATETIME
ORDER BY i.DATETIME
