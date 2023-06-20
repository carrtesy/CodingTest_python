import sys
import heapq
input = sys.stdin.readline
N = int(input())
M = int(input())

INF = int(1e9+1e3)

graph = [[INF]*(N+1) for _ in range(N+1)]
for n in range(1, N+1):
  graph[n][n] = 0
for _ in range(M):
  a, b, c = map(int, input().split())
  graph[a][b] = min(graph[a][b], c)
  
dist = [INF]*(N+1)
bt = [0]*(N+1)

src, dst = map(int, input().split())
bt[src] = src

q = []
q.append((0,src))
while q:
  cost, cur = heapq.heappop(q)
  
  for i in range(1, N+1):
    nn, nc = i, graph[cur][i]
    if nc < INF:
      if dist[nn] > cost+nc:
        dist[nn] = cost+nc
        bt[nn] = cur
        heapq.heappush(q, (cost+nc, nn))

path = [dst]
prev = dst
while prev != bt[prev]:
  prev=bt[prev]
  path.insert(0, prev)

print(dist[dst])
print(len(path))
print(" ".join(map(str, path)))