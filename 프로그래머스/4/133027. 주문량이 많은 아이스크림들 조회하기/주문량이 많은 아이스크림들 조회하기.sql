# 상반기 주문 정보
# SELECT * 
# FROM FIRST_HALF;

# # 7월의 아이스크림 주문 정보
SELECT * 
FROM JULY; 

# SHIPMENT_ID, FLAVOR, TOTAL_ORDER
# FIRST_HALF 테이블의 기본 키는 FLAVOR
# JULY 테이블의 기본 키는 SHIPMENT_ID
# JUPY 테이블의 FLAVOR 는 FIRST_HALF 테이블의 FLAVOR 의 외래 키

# 7월 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량을 더한 값이 큰 순서대로 상위 3개의 맛을 조회하는 SQL 문

# SHIPMENT_ID : 출하 번호
# FLAVOR : 아이스크림 맛 
# TOTAL_ORDER : 총 주문량

SELECT 
    FLAVOR
FROM FIRST_HALF H LEFT JOIN JULY J USING(FLAVOR)
GROUP BY FLAVOR
ORDER BY SUM(H.TOTAL_ORDER) + SUM(J.TOTAL_ORDER) DESC
LIMIT 3 