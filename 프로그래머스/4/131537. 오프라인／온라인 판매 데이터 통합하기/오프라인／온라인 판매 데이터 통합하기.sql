# 2022년 3월 오프라인/온라인 상품 데이터의 판매 날짜, 상품 id, 유저 id, 판매량을 출력 
# OFFLINE_SALE 테이블의 판매 데이터의 USER_ID 값은 NULL로 표시 
# 판매일 기준 오름차순 정렬 
# 상품 ID 기준 오름차순 
# 유저 ID 기준 오름차순 정렬

# 날짜, 회원 ID, 상품 ID 조합에 대해서는 하나의 판매 데이터

SELECT 
    DATE_FORMAT(SALES_DATE, "%Y-%m-%d") SALES_DATE,
    PRODUCT_ID, 
    USER_ID, 
    SALES_AMOUNT
FROM ONLINE_SALE
WHERE MONTH(SALES_DATE) = 3
UNION 
SELECT 
    DATE_FORMAT(SALES_DATE, "%Y-%m-%d") SALES_DATE,
    PRODUCT_ID, 
    NULL AS USER_ID,
    SALES_AMOUNT
FROM OFFLINE_SALE
WHERE MONTH(SALES_DATE) = 3
ORDER BY SALES_DATE, PRODUCT_ID, USER_ID