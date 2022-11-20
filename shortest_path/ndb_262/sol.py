import sys

input = sys.stdin.readline
N, M, C = map(int, input().split())
INF = int(1e9)
graph = [[] for i in range(N + 1)]
distance = [INF] * (N + 1)
for _ in range(M):
  X, Y, Z = map(int, input().split())
  graph[X].append((Y, C))

import heapq


def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]

      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))


dijkstra(start=C)
print(distance)
print(list(map(lambda x: x if x != INF else 0, distance)))
