import sys

input = sys.stdin.readline
v, e = map(int, input().split())
parent = [i for i in range(v + 1)]


def find_root(a, parent):
  if a != parent[a]:
    parent[a] = find_root(parent[a], parent)
  return parent[a]


def merge(a, b, parent):
  ra = find_root(a, parent)
  rb = find_root(b, parent)
  if ra <= rb:
    parent[b] = ra
  else:
    parent[a] = rb


for _ in range(e):
  a, b = map(int, input().split())
  merge(a, b, parent)

for i in range(1, v + 1):
  find_root(i, parent)
print(parent)
