import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N
bt = [-1] * N

LS, maxidx = 0, -1
for i in range(N):
  for j in range(0, i):
    if arr[i] > arr[j]:
      if dp[j] + 1 > dp[i]:
        dp[i] = dp[j] + 1
        bt[i] = j

  if dp[i] > LS:
    LS, maxidx = dp[i], i

LIS = []
i = maxidx
while True:
  LIS.insert(0, arr[i])
  i = bt[i]
  if i == -1:
    break
print(LS)
print(" ".join(map(str, LIS)))
