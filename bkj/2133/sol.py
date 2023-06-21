n = int(input())
if n == 1:
  print(0)
else:
  dp = [0] * (n+1)
  dp[0], dp[2] = 1, 3
  for i in range(4, n+1, 2):
    dp[i] = dp[i-2] * dp[2] + 2 * sum([dp[j] for j in range(0, i-3, 2)])
  print(dp[n])