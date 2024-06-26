-- 코드를 입력하세요
## 2022년 5월에 예약한 환자 수를 진료과코드 별로 조회

SELECT MCDP_CD '진료과 코드', COUNT(*) '5월예약건수'
FROM APPOINTMENT 
WHERE DATE_FORMAT(APNT_YMD, '%m') = 5
GROUP BY MCDP_CD
ORDER BY 2, 1

# 41행
# SELECT COUNT(*)
# FROM APPOINTMENT

# 7가지 진료 코드
# SELECT DATE_FORMAT(APNT_YMD, '%m'), COUNT(DATE_FORMAT(APNT_YMD, '%m'))
# FROM APPOINTMENT
# GROUP BY DATE_FORMAT(APNT_YMD, '%m')

