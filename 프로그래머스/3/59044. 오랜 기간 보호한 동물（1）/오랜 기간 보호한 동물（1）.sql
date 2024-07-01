-- 코드를 입력하세요
# ANIMAL INS 테이블 (animal id, animal type, datetime, intake_condition, name, sex_upon_intake, )
# ANIMAL OUTS 테이블 (animal id, animal type, datetime, name, sex_upon_outcome)
# animal_outs(animal_id) 는 animal_ins의 animal_id 의 외래키? 

# 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일
# SELECT *
# FROM ANIMAL_INS


SELECT a.NAME, a.DATETIME
FROM ANIMAL_INS a LEFT JOIN ANIMAL_OUTS b on a.ANIMAL_ID=B.ANIMAL_ID
WHERE b.DATETIME IS NULL
ORDER BY a.DATETIME
LIMIT 3

