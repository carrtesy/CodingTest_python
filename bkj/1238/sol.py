import sys
import heapq

input = sys.stdin.readline
N, M, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
INF = int(1e9 - 1)

for _ in range(M):
  a, b, c = map(int, input().split())
  graph[a].append((c, b))


def dijkstra(start, end):
  dist = [INF] * (N + 1)

  q = []
  dist[start] = 0
  heapq.heappush(q, (0, start))

  while q:
    cc, cur = heapq.heappop(q)
    for (nc, nxt) in graph[cur]:
      if cc + nc < dist[nxt]:
        dist[nxt] = cc + nc
        heapq.heappush(q, (cc + nc, nxt))

  return dist[end]


max_time = 0
for n in range(1, N + 1):
  time_spent = dijkstra(n, X) + dijkstra(X, n)
  max_time = max(time_spent, max_time)
print(max_time)
