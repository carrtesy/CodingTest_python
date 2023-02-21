import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [[0] * n for _ in range(2)]

m = arr[0]
dp[0][0], dp[1][0] = arr[0], arr[0]
for i in range(1, n):
  dp[0][i] = max(arr[i], arr[i] + dp[0][i - 1])
  dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + arr[i])
  m = max(dp[0][i], dp[1][i], m)

print(m)