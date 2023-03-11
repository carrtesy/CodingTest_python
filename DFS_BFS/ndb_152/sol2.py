from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

graph = []
for i in range(N):
  graph.append([*input().strip()])
print(graph)

q = deque([])
q.append((0, 0, 1))

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
while q:
  r, c, m = q.popleft()
  if (r == N - 1) and (c == M - 1):
    print(m)
    break

  for i in range(4):
    _r, _c = r + dr[i], c + dc[i]
    if 0 <= _r < N and 0 <= _c < M and graph[_r][_c] == '1':
      q.append((_r, _c, m + 1))
