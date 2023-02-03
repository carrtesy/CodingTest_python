import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
  X, Y, K = map(int, input().split())
  graph[Y].append((X, K))
  indegree[X] += 1

q = deque()
recipe = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
  if indegree[i] == 0:
    recipe[i][i] = 1
    q.append(i)

while q:
  cur = q.popleft()
  for (nxt, cnt) in graph[cur]:
    indegree[nxt] -= 1
    for i in range(1, N + 1):
      recipe[nxt][i] += (recipe[cur][i] * cnt)

    if indegree[nxt] == 0:
      q.append(nxt)

for i in range(1, N + 1):
  if recipe[N][i] != 0:
    print(i, recipe[N][i])