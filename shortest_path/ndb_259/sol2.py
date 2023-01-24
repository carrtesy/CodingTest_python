import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
INF = 1e9 - 1
dist1 = [INF] * (N + 1)
dist2 = [INF] * (N + 1)

for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
X, K = map(int, input().split())


def dijkstra(s, dist):
  q = []
  heapq.heappush(q, s)
  dist[s] = 0

  while q:
    cur = heapq.heappop(q)
    for next in graph[cur]:
      if dist[next] > dist[cur] + 1:
        dist[next] = dist[cur] + 1
        heapq.heappush(q, next)


dijkstra(1, dist1)
dijkstra(K, dist2)
print(dist1[K] + dist2[X])
