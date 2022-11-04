from collections import deque
import sys

N, M, K, X = map(int, input().split())
graph = [[] for i in range(N + 1)]

for i in range(M):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)

visited = [False] * (N + 1)


def dfs(graph, src, depth):
  queue = deque([(src, 0)])
  visited[src] = True
  while queue:
    node, d = queue.popleft()
    if d == depth:
      queue.append((node, d))
      answer = sorted(list(map(lambda x: x[0], queue)))
      return '\n'.join(map(str, answer))
    for i in graph[node]:
      if not visited[i]:
        queue.append((i, d + 1))
        visited[i] = True
  return -1


answer = dfs(graph, X, K)
print(answer)
