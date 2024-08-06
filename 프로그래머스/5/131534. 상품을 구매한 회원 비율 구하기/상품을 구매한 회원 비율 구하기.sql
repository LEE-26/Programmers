# 2021년에 가입한 전체 회원들 중 상품을 구매한 회원수
# 구매한 회원의 비율 (2021년에 가입한 회원 중 상품을 구매한 회원수 / 2021년에 가입한 전체 회원 수)
# 년, 월 별로 출력 ??
# 비율 : ROUND(, 2)
# 년 기준 오름차순 -> 월 기준 오름차순
SELECT 
    YEAR(S.SALES_DATE) AS YEAR, 
    MONTH(S.SALES_DATE) AS MONTH,
    COUNT(DISTINCT USER_ID) AS PURCHASED_USERS,
    ROUND(COUNT(DISTINCT USER_ID) / (SELECT COUNT(*)
                                     FROM USER_INFO
                                     WHERE YEAR(JOINED) = 2021), 1) AS PUCHASED_RATIO
FROM USER_INFO I JOIN ONLINE_SALE S USING(USER_ID)
WHERE YEAR(I.JOINED) = 2021 
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH