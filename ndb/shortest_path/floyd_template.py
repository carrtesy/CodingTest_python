import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
INF = int(1e9)
dp = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
  a, b, c = map(int, input().split())
  dp[a][b] = c
for n in range(1, N + 1):
  dp[n][n] = 0

# floyd
for k in range(1, N + 1):
  for a in range(1, N + 1):
    for b in range(1, N + 1):
      dp[a][b] = min(dp[a][b], dp[a][k] + dp[k][b])

for a in range(1, N + 1):
  for b in range(1, N + 1):
    print(dp[a][b], end=" ")
  print("")
