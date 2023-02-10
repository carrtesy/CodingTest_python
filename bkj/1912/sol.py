import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))

dp = [0] * N
answer = dp[0] = arr[0]
for i in range(1, N):
  dp[i] = arr[i] + max(dp[i - 1], 0)
  answer = max(answer, dp[i])

print(answer)
