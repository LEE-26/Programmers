-- 코드를 입력하세요
# 식품 정보 FOOD PRODUCT
# PRODUCT 40개 유니크
# 주문 테이블 FOOD_ORDER
# 생산일자 2022년 5월 , 식품 ID, 식품 이름, 총매출 조회 
# 총매출 내림차순 -> 식품 ID 오름차순 

SELECT O.PRODUCT_ID PRODUCT_ID, P.PRODUCT_NAME PRODUCT_NAME, SUM(O.AMOUNT * P.PRICE) TOTAL_SALES
FROM FOOD_ORDER O INNER JOIN FOOD_PRODUCT P USING (PRODUCT_ID)
WHERE DATE_FORMAT(PRODUCE_DATE, '%Y-%m') = '2022-05'
GROUP BY O.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, PRODUCT_ID ASC 