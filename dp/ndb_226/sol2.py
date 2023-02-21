import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dp = [-1] * (M + 1)
for _ in range(N):
  a = int(input())
  if a <= M:
    dp[a] = 1

for m in range(2, M + 1):
  if dp[m] > 0:
    continue
  for k in range(1, m):
    a, b = k, m - k
    da, db = dp[a], dp[b]
    if da > 0 and db > 0:
      if dp[m] <= 0:
        dp[m] = da + db
      else:
        dp[m] = min(dp[m], da + db)

print(dp)
