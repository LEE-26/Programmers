# 2016년 1월 1일은 금요일
# 2016년 a월 b일은 무슨 요일 ? 
# a, b 를 입력받아 2016년 a 월 b일이 무슨 요일인지 리턴하기 
# 요일의 이름은 일요일부터 토요일까지 (SUN ~ SAT)
import datetime

def solution(a, b):
    week_dic = {0:'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN'}
    day = datetime.date(2016, a, b)
    answer = week_dic[day.weekday()]
    
    return answer