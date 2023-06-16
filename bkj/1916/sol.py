import sys
import heapq
input = sys.stdin.readline
N = int(input())
M = int(input())
INF = int(1e9+1e4)
graph = [[INF] * (N+1) for _ in range(N+1)]

for _ in range(M):
  a, b, c = map(int, input().split())
  graph[a][b] = min(graph[a][b], c)

src, dst = map(int, input().split())
dist = [INF] * (N+1)
dist[src] = 0

def dijkstra(src):
  q = []
  heapq.heappush(q, (0, src))

  while q:
    cost, a = heapq.heappop(q)
    for i in range(1, N+1):
      nn, nc = i, graph[a][i]
      if nc < INF and dist[nn] > cost+nc:
        dist[nn] = cost+nc
        heapq.heappush(q, (dist[nn], nn))

dijkstra(src)
print(dist[dst])