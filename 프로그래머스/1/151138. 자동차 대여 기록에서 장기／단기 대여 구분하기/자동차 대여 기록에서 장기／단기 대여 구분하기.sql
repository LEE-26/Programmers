# 대여 시작일 2022년 9월
# 대여 기간이 30일 이상이면 '장기 대여'
# 아니면 '단기 대여'
# RENT_TYPE, 대여기록
# 대여 기록 ID : HISTORY ID

# SELECT 
#     HISTORY_ID,
#     CAR_ID,
#     DATE_FORMAT(START_DATE, '%Y-%m-%d') START_DATE,
#     DATE_FORMAT(END_DATE, '%Y-%m-%d') END_DATE, 
#     CASE WHEN DATEDIFF(END_DATE, START_DATE) >= 30 THEN '장기 대여'
#          ELSE '단기 대여' END AS RENT_TYPE
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# WHERE DATE_FORMAT(START_DATE, '%Y-%m') = '2022-09'
# ORDER BY HISTORY_ID DESC;

SELECT HISTORY_ID, CAR_ID, 
	   DATE_FORMAT (START_DATE, "%Y-%m-%d") AS START_DATE, 
	   DATE_FORMAT (END_DATE, "%Y-%m-%d") AS END_DATE,
CASE WHEN DATEDIFF(END_DATE, START_DATE) < 29 then '단기 대여' 
            ELSE '장기 대여' 
            END AS  RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE START_DATE LIKE '2022-09-%'
ORDER BY HISTORY_ID DESC;