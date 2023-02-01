import sys

sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline

n, m = map(int, input().split())
parents = [i for i in range(n + 1)]


def find(a, parents):
  if a != parents[a]:
    parents[a] = find(parents[a], parents)
  return parents[a]


def union(a, b, parents):
  ra = find(a, parents)
  rb = find(b, parents)
  if ra < rb:
    parents[rb] = ra
  else:
    parents[ra] = rb


for _ in range(m):
  c, a, b = map(int, input().split())
  if c == 0:
    union(a, b, parents)
  elif c == 1:
    if find(a, parents) == find(b, parents):
      print("yes")
    else:
      print("no")

print(parents)
