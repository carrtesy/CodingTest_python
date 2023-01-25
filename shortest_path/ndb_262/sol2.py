import sys
import heapq

input = sys.stdin.readline

N, M, C = map(int, input().split())
graph = [[] for _ in range(N + 1)]
INF = int(1e9) - 1
dist = [INF] * (N + 1)
for _ in range(M):
  X, Y, Z = map(int, input().split())
  graph[X].append((Y, Z))


def dijkstra(s):
  q = []
  heapq.heappush(q, s)
  dist[s] = 0

  while q:
    cur = heapq.heappop(q)

    for nxt, nc in graph[cur]:
      if dist[nxt] > dist[cur] + nc:
        heapq.heappush(q, nxt)
        dist[nxt] = dist[cur] + nc


dijkstra(C)
print(dist)

cnt, maxtime = 0, 0
for i in range(1, N + 1):
  if dist[i] < INF and dist[i] != 0:
    cnt += 1
    if dist[i] > maxtime:
      maxtime = dist[i]

print(cnt, " ", maxtime)
