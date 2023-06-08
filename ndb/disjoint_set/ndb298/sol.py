import sys

input = sys.stdin.readline
N, M = map(int, input().split())

p = [i for i in range(N + 1)]


def union(a, b, p):
  a = p[a]
  b = p[b]
  p[min(a, b)] = max(a, b)


def find(a, p):
  if a != p[a]:
    p[a] = find(p[a], p)
  return p[a]


while M:
  c, a, b = map(int, input().split())
  if c == 0:
    union(a, b, p)
  elif c == 1:
    pa = find(a, p)
    pb = find(b, p)
    print("YES" if pa == pb else "NO")
  M -= 1