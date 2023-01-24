import sys
from itertools import combinations
from collections import deque
from copy import deepcopy

input = sys.stdin.readline
N, M = map(int, input().split())

graph = []
for r in range(N):
  graph.append(list(map(int, input().split())))

zeros = []
twos = []
for r in range(N):
  for c in range(M):
    if graph[r][c] == 0:
      zeros.append((r, c))
    elif graph[r][c] == 2:
      twos.append((r, c))

threes = combinations(zeros, 3)


def bfs(th, graph):
  q = deque(twos)
  g = deepcopy(graph)
  for (r, c) in th:
    g[r][c] = 1

  dr = [0, 0, 1, -1]
  dc = [1, -1, 0, 0]

  while q:
    r, c = q.popleft()
    for i in range(4):
      _r, _c = r + dr[i], c + dc[i]
      if 0 <= _r and _r < N and 0 <= _c and _c < M and g[_r][_c] == 0:
        q.append((_r, _c))
        g[_r][_c] = 2

  cnt = 0
  for r in range(N):
    for c in range(M):
      if g[r][c] == 0:
        cnt += 1
  return cnt


safety_area = 0
for th in threes:
  sol = bfs(th, graph)
  if sol > safety_area:
    safety_area = sol

print(safety_area)
