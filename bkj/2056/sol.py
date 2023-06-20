import sys
from collections import deque
input = sys.stdin.readline
N = int(input())

ind = [0] * (N+1)
time = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for i in range(1, N+1):
  line = list(map(int, input().split()))
  time[i] = line[0]
  ind[i] = line[1]
  for j in range(2, 2+line[1]):
    graph[line[j]].append(i)

q = deque([])

for n in range(1, N+1):
  if ind[n] == 0:
    q.append(n)

while q:
  src = q.popleft()
  for tgt in graph[src]:
    ind[tgt] -= 1
    if ind[tgt] == 0:
      q.append(tgt)