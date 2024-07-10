# def solution(s, n):
#     # 예외 , 공백 z -> a
#     new_ls = []

#     for a_ in s :
#         if a_ != ' ' and a_ != 'z' and a_ != 'Z':
#             new_ls.append(chr(ord(f'{a_}') + n))
#         elif a_ == 'z' or a_ == 'Z' : 
#             new_ls.append(chr(ord(a_) - 26 + n))
#         else : 
#             new_ls.append(' ')

#     answer = ''.join(new_ls)
#     return answer

def solution(s, n):
    lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # s = "ab zA DH"    
    # n = 2

    result = [] 

    for s_ in s :
        if s_.isalpha() :
            if s_.islower() : 
                idx = lower_alphabet.find(s_) + n
                result.append(lower_alphabet[idx % 26])
            else : 
                idx = upper_alphabet.find(s_) + n
                result.append(upper_alphabet[idx % 26])
        
        else : 
            result.append(' ')
                
    answer = ''.join(result)
    print(answer)


    return answer


