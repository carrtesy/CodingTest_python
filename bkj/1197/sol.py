import sys
input = sys.stdin.readline
V, E = map(int, input().split())

edges = []
for _ in range(E):
  A, B, C = map(int, input().split())
  edges.append((C, A, B))
edges.sort()

p = [i for i in range(V+1)]

def find(a):
  if p[a] != a:
    p[a] = find(p[a])
  return p[a]

def union(a, b):
  a = find(a)
  b = find(b)
  if a < b:
    p[b] = a
  else:
    p[a] = b 

total_cost = 0
for (c, a, b) in edges:
  if find(a) != find(b):
    union(a, b)
    total_cost += c
print(total_cost)