def solution(nums):
    sosu = [] 

    for i in range(len(nums)) : # 0
        for j in range(i+1, len(nums)) : # 1
            for k in range(j+1, len(nums)) : # 2, 3 # iteration 안되면 그냥 넘어감 ?
                sum_3 = nums[i] + nums[j] + nums[k]
                if len([i for i in range(1, sum_3 + 1) if sum_3 % i == 0]) == 2 : 
                    sosu.append(sum_3)
                    
    return len(sosu)