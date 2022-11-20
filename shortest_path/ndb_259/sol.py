import sys

input = sys.stdin.readline

N, M = map(int, input().split())
INF = int(87654321)
dp = [[0 if i == j else INF for i in range(N + 1)] for j in range(N + 1)]

for _ in range(M):
  a, b = map(int, input().split())
  dp[a][b], dp[b][a] = 1, 1

X, K = map(int, input().split())

for k in range(1, N + 1):
  for a in range(1, N + 1):
    for b in range(1, N + 1):
      dp[a][b] = min(dp[a][b], dp[a][k] + dp[k][b], INF)
      dp[b][a] = min(dp[b][a], dp[b][k] + dp[k][a], INF)

print(dp[1][K] + dp[K][X])
