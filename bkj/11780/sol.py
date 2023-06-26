import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
INF = int(10**8)
graph = [[INF]*(n+1) for _ in range(n+1)]
bt = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
  graph[i][i] = 0

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a][b] = min(graph[a][b], c)

for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      detour = graph[i][k] + graph[k][j]
      if graph[i][j] > detour:
        graph[i][j] = detour
        bt[i][j] = k

for g in graph[1:]:
  row = map(lambda x:x if x!=INF else 0, g[1:])
  print(" ".join(map(str, row)))

def find_route(a, b):
  k = bt[a][b]
  if k == 0:
    return [a, b]
  return find_route(a, k)[:-1] + find_route(k, b)

for i in range(1, n+1):
  for j in range(1, n+1):
    if i == j or graph[i][j] >= INF:
      print("0")
    else:
      path = find_route(i, j)
      print(" ".join(map(str, [len(path)]+path)))
        
