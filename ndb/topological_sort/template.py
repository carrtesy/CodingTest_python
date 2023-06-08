from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v + 1)

graph = [[] for _ in range(v + 1)]
for i in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)
  indegree[b] += 1


def topological_sort():
  q = deque()
  result = []

  for i in range(1, v + 1):
    if indegree[i] == 0:
      q.append(i)

  while q:
    cur = q.popleft()
    result.append(cur)
    for nxt in graph[cur]:
      indegree[nxt] -= 1
      if indegree[nxt] == 0:
        q.append(nxt)
  return result


result = topological_sort()
print(result)
