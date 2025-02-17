def solution(n):

    if n <= 1:
        return n
    
    dp = [0, 1]

    for i in range(2, n + 1):
        # 이미 F(0)과 F(1)이 리스트에 있으므로 2부터 계산
        dp.append((dp[i-1] + dp[i-2]) % 1234567)
        
    return dp[n]