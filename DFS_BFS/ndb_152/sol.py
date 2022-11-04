from collections import deque

N, M = map(int, input().split())
src = (0, 0)
dst = (N - 1, M - 1)

graph = []

for i in range(N):
  row = list(map(int, [*input()]))
  graph.append(row)

print(graph)

drs = [1, -1, 0, 0]
dcs = [0, 0, 1, -1]

queue = deque([(src, 1)])
while queue:
  (r, c), cnt = queue.popleft()
  graph[r][c] = 0
  if (r, c) == dst:
    print("answer: ", cnt)

  for (dr, dc) in zip(drs, dcs):
    _r, _c = r + dr, c + dc
    if (0 <= _r and _r < N) and (0 <= _c and _c < M) and (graph[_r][_c]):
      queue.append(((_r, _c), cnt + 1))
