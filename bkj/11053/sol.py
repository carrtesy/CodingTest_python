import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N

LIS = 0
for i in range(N):
  for j in range(0, i):
    if arr[i] > arr[j]:
      dp[i] = max(dp[i], dp[j] + 1)
  LIS = max(LIS, dp[i])
print(LIS)