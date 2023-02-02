import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
edges = []
ps = [i for i in range(N + 1)]


def union(a, b, ps):
  ra = find(a, ps)
  rb = find(b, ps)
  if ra < rb:
    ps[rb] = ra
  else:
    ps[ra] = rb


def find(a, ps):
  if a != ps[a]:
    ps[a] = find(ps[a], ps)
  return ps[a]


for i in range(M):
  a, b, c = map(int, input().split())
  edges.append((a, b, c))

edges.sort(key=lambda x: x[-1])

total_cost = 0
max_cost = 0
for (a, b, c) in edges:
  if find(a, ps) != find(b, ps):
    union(a, b, ps)
    total_cost += c
    max_cost = c
total_cost -= max_cost
print(total_cost)
