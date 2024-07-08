def solution(n, m):
    # 최대 공약수, 최소 공배수
    answer = []
    # 약수 구하기
    num1_ls = set([x for x in range(1, n+1) if n % x == 0])
    num2_ls = set([x for x in range(1, m+1) if m % x == 0])
    
    gcd = max(num1_ls & num2_ls) # the greatest common divisor
    
    # LCM : 두 수를 곱하고 최대공약수로 나눈다.
    lcm = n * m / gcd
    
    answer = [gcd, lcm]
    
    return answer