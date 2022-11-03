from collections import deque

def dfs(graph, v, visited, dst):
  # check in
  visited[v] = True
  print(v, end=" ")
  # arrived?
  # iterate
  for i in graph[v]:
    # next
    if not visited[i]:
      # visit
      dfs(graph, i, visited, dst)
      # check out

def bfs(graph, src, visited, dst):
  queue = deque([src])
  visited[src] = True

  while queue:
    # pop
    v = queue.popleft()
    print(v, end=" ")
    # arrived?
    # iterate
    for i in graph[v]:
      # next
      if not visited[i]:
        # visit, enqueue
        queue.append(i)
        visited[i] = True

N, src, dst = map(int, input().split())
graph = []
graph.append([])
for i in range(N):
  lst = list(map(int, input().split()))
  graph.append(lst)

visited = [False] * (N+1)
dfs(graph, src, visited, dst)
print()

visited = [False] * (N+1)
bfs(graph, src, visited, dst)
print()