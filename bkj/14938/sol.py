import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
item = [0]+list(map(int, input().split()))
INF = int(1e9+1)
graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
  graph[i][i] = 0

for _ in range(r):
  a, b, l = map(int, input().split())
  graph[a][b] = graph[b][a] = l

for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

print(max([sum([(g[i]<=m) * item[i] for i in range(1, n+1)]) for g in graph]))
