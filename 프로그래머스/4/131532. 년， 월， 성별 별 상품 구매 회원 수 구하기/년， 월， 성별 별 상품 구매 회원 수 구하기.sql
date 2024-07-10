# SELECT * 
# FROM USER_INFO

# SELECT *
# FROM ONLINE_SALE

# USER_INFO 테이블과 ONLINE_SALE 테이블에서 년,월,성별 별로 상품을 구매한 회원수를 집계
# 년,월,성별을 기준으로 오름차순 정렬
# 성별 정보 없는 경우 제외
# JOINED : 가입일 

SELECT 
    DATE_FORMAT(SALES_DATE, '%Y') YEAR,
    MONTH(SALES_DATE) MONTH,
    GENDER, 
    COUNT(DISTINCT USER_ID) AS USERS
FROM ONLINE_SALE S LEFT JOIN USER_INFO I USING (USER_ID)
WHERE GENDER IS NOT NULL
GROUP BY DATE_FORMAT(SALES_DATE, '%Y'), MONTH(SALES_DATE), GENDER
ORDER BY DATE_FORMAT(SALES_DATE, '%Y'), MONTH(SALES_DATE), GENDER