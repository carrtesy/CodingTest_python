N = int(input())

dp = [0] * N

dp[0] = 1
dp[1] = 3

for i in range(2, N):
  dp[i] = dp[i - 1] + 2 * dp[i - 2]

print(dp[N - 1])
