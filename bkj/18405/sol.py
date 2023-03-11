import sys
import heapq

input = sys.stdin.readline
N, K = map(int, input().split())
graph = [[-1] * (N + 1)]

pq = []
for i in range(1, N + 1):
  graph.append([-1] + list(map(int, input().split())))
  for j in range(1, N + 1):
    if graph[i][j] != 0:
      heapq.heappush(pq, (0, graph[i][j], i, j))
S, X, Y = map(int, input().split())

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

while pq:
  t, p, r, c = heapq.heappop(pq)
  if t >= S: break

  for i in range(4):
    _r, _c = r + dr[i], c + dc[i]
    if 1 <= _r <= N and 1 <= _c <= N and graph[_r][_c] == 0:
      graph[_r][_c] = p
      heapq.heappush(pq, (t + 1, p, _r, _c))

print(graph[X][Y])