import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (N+1)
start = 1

def dfs(graph, s):
  visited[s] = True
  for nxt in graph[s]:
    if not visited[nxt]:
      dfs(graph, nxt)
dfs(graph, start)
print(sum(visited)-1)