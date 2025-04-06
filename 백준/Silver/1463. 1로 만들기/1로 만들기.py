n = int(input())

def make_one(n):
    # dp[i]: 숫자 i를 1로 만드는 데 필요한 최소 연산 횟수를 저장할 리스트
    # n + 1인 이유는 인덱스를 1~n까지 사용하려고
    dp = [0] * (n + 1)
    # 1은 시작 숫자이자 목표 숫자니까, 이미 최소 연산 횟수가 0임 그래서 dp[1] = 0은 초기값으로 생각하고, 2부터 n까지에 대해서만 계산
    for i in range(2, n + 1):
        # 현재 수에서 1을 빼는 경우
        dp[i] = dp[i - 1] + 1
        # 현재 수가 2로 나누어떨어지는 경우
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        # 현재 수가 3으로 나누어떨어지는 경우
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    return dp[n]

print(make_one(n))