import heapq
import sys

input = sys.stdin.readline
INF = 1e9

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n + 1)]
dist = [INF] * (n + 1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))


def dijkstra(start):
  q = []
  dist[start] = 0
  heapq.heappush(q, (start, 0))

  while q:
    cur, c = heapq.heappop(q)

    for next in graph[cur]:
      nn, nc = next
      if dist[nn] > c + nc:
        dist[nn] = c + nc
        heapq.heappush(q, (nn, c + nc))


dijkstra(start)
print(dist)
