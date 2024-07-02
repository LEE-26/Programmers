-- 코드를 입력하세요
# 중성화 수술을 거친 동물
# 들어올 당시 중성화 X 
# 나갈 때는 중성화 
# 아이디, 생물 종, 이름
# 아이디 순
SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME
FROM ANIMAL_INS I INNER JOIN ANIMAL_OUTS O USING (ANIMAL_ID)
WHERE 
    I.SEX_UPON_INTAKE LIKE "%Intact%" AND
    (O.SEX_UPON_OUTCOME LIKE "%Spayed%" OR
    O.SEX_UPON_OUTCOME LIKE "%Neutered%")
ORDER BY I.ANIMAL_ID;