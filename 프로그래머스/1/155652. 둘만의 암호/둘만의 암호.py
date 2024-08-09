def solution(s, skip, index):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    for skip_alphabet in skip : 
        alphabet = alphabet.replace(skip_alphabet, '')

    for s_alphabet in s :
        answer += alphabet[(alphabet.find(s_alphabet) + index)%len(alphabet)]
    return answer