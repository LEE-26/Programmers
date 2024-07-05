def solution(phone_number):
    idx = len(phone_number) - 4
    back = phone_number[idx:]

    return "*"*idx+back