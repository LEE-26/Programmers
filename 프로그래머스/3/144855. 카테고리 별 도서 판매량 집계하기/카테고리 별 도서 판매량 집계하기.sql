-- 코드를 입력하세요

# 2022년 1월의 카테고리별 도서 판매량 합산 
# 카테고리, 총 판매량 리스트 출력
SELECT CATEGORY, SUM(SALES) TOTAL_SALES
FROM BOOK_SALES S LEFT JOIN BOOK B USING (BOOK_ID)
WHERE DATE_FORMAT(S.SALES_DATE, '%Y-%m') = '2022-01'
GROUP BY CATEGORY
ORDER BY CATEGORY
