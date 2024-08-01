# 몇 시에 입양이 가장 많은지 
# 0시부터 23시까지 각 시간대별로 몇 건 발생했는지 조회 
# 시간대 순 정렬
SET @HOUR = -1;
SELECT 
    (@HOUR := @HOUR + 1) AS HOUR,
    (SELECT COUNT(HOUR(DATETIME))
    FROM ANIMAL_OUTS
    WHERE HOUR(DATETIME) = @HOUR) AS COUNT
FROM ANIMAL_OUTS
WHERE @HOUR < 23;
    

