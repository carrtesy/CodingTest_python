import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e12) - 1
dist = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
  dist[i][i] = 0

for _ in range(m):
  a, b, c = map(int, input().split())
  dist[a][b] = min(dist[a][b], c)

for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

for i in range(1, n + 1):
  for j in range(1, n + 1):
    if dist[i][j] >= INF:
      print(0, end=" ")
    else:
      print(dist[i][j], end=" ")
  print("")
