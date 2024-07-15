# 조회수가 가장 높은 중고거래 게시물에 대한 첨부파일 경로 조회 ,,, VIEWS !
# FILE ID 를 기준으로 내림차순 
# 기본적인 파일 경로 : /home/grep/src/ 
# 게시글 ID를 기준으로 디렉토리 구분 
# 파일 ID, 파일 이름, 파일 확장자로 구성
# 조회수가 가장 높은 게시물은 하나만 존재

# SELECT * 
# FROM USED_GOODS_BOARD ;

# SELECT * 
# FROM USED_GOODS_FILE ;

SELECT CONCAT('/home/grep/src/', BOARD_ID, '/', FILE_ID, FILE_NAME, FILE_EXT) FILE_PATH
FROM USED_GOODS_BOARD B INNER JOIN USED_GOODS_FILE USING(BOARD_ID)
WHERE VIEWS = (SELECT MAX(VIEWS) FROM USED_GOODS_BOARD)
ORDER BY FILE_ID DESC

