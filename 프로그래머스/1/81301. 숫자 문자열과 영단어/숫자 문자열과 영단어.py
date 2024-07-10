def solution(s):
    # 영단어를 숫자로 매핑하는 딕셔너리
    num_dict = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    # 임시 문자열을 저장할 변수
    temp_str = ""
    # 최종 결과를 저장할 변수
    result = ""

    # 입력 문자열을 하나씩 순회
    for char in s:
        # 만약 숫자라면 결과에 바로 추가
        if char.isdigit():
            result += char
        else:
            # 임시 문자열에 추가
            temp_str += char
            # 만약 임시 문자열이 영단어 딕셔너리에 있다면 변환하여 결과에 추가
            if temp_str in num_dict:
                result += num_dict[temp_str]
                temp_str = ""  # 임시 문자열 초기화

    return int(result)