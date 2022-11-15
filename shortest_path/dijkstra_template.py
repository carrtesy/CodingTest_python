import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
start = int(input())
print(n, m)
print(start)

graph = [[] for _ in range(n + 1)]
dist = [INF] * (n + 1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))


def dijkstra(start):
  q = []
  dist[start] = 0
  heapq.heappush(q, (0, start))

  while q:
    cur_cost, cur_node = heapq.heappop(q)

    for (node, cost) in graph[cur_node]:
      next_cost = cur_cost + cost
      if cost < dist[node]:
        dist[node] = next_cost
        heapq.heappush(q, (next_cost, node))


dijkstra(start)
for i in range(1, n + 1):
  print(dist[i])
