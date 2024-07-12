def solution(array, commands):
    answer = []
    for n in range(len(commands)) : 

        i = commands[n][0] - 1
        j = commands[n][1]
        k = commands[n][2] - 1

        new_array = array[i:j]
        new_array.sort()

        answer.append(new_array[k])     
    
    return answer