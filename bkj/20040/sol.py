import sys

input = sys.stdin.readline

n, m = map(int, input().split())
parents = [i for i in range(n)]


def union(a, b, parents):
  ra = find(a, parents)
  rb = find(b, parents)
  if ra < rb:
    parents[rb] = ra
  else:
    parents[ra] = rb


def find(a, parents):
  if a != parents[a]:
    parents[a] = find(parents[a], parents)
  return parents[a]


cycle = False
for i in range(1, m + 1):
  a, b = map(int, input().split())
  if find(a, parents) == find(b, parents):
    cycle = True
    break
  else:
    union(a, b, parents)
if cycle:
  print(i)
else:
  print(0)
