from collections import deque

N, src, dst = map(int, input().split())

graph = []
graph.append([])
for i in range(N):
  lst = list(map(int, input().split()))
  graph.append(lst)
print(graph)


def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=" ")
  for nn in graph[v]:
    if not visited[nn]:
      dfs(graph, nn, visited)


def bfs(graph, v, visited):

  queue = deque([])
  queue.append(v)
  visited[v] = True
  while queue:
    cur = queue.popleft()
    print(cur, end=" ")

    for nn in graph[cur]:
      if not visited[nn]:
        queue.append(nn)
        visited[nn] = True


visited = [0] * (N + 1)
dfs(graph, src, visited)
print(" ")
visited = [0] * (N + 1)
bfs(graph, src, visited)
print(" ")
