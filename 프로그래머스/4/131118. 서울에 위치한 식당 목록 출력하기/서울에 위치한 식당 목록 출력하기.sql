# 이 코드가 왜 틀렸을까 ? - 튜터님 질문 !
SELECT 
    REST_ID,
    REST_NAME, 
    FOOD_TYPE, 
    FAVORITES,
    ADDRESS,
    ROUND(AVG(REVIEW_SCORE), 2) SCORE
FROM REST_REVIEW R INNER JOIN REST_INFO I USING (REST_ID)
GROUP BY REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS
HAVING ADDRESS LIKE '서울%'
ORDER BY SCORE DESC, FAVORITES DESC 

# 정답코드
# SELECT A.REST_ID, B.REST_NAME, B.FOOD_TYPE, B.FAVORITES, B.ADDRESS, ROUND(AVG(A.REVIEW_SCORE),2) AS SCORE
# FROM REST_REVIEW A
# JOIN REST_INFO B ON A.REST_ID = B.REST_ID
# GROUP BY A.REST_ID
# HAVING B.ADDRESS LIKE '서울%'
# ORDER BY SCORE DESC, B.FAVORITES DESC