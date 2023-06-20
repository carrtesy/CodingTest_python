import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
ind = [0]*(N+1)
for _ in range(M):
  row = list(map(int, input().split()))
  for i in range(2, len(row)):
    graph[row[i-1]].append(row[i])
    ind[row[i]] += 1

q = deque([])

for i in range(1, N+1):
  if ind[i] == 0:
    q.append(i)

order = []
while q:
  cur = q.popleft()
  order.append(cur)
  for nxt in graph[cur]:
    ind[nxt] -= 1
    if ind[nxt] == 0:
      q.append(nxt)

if len(order) == N:
  for node in order:
    print(node)
else:
  print("0")