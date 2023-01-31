import sys

input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]
M = max(arr)
f = [1] * (M + 1)
g = [0] * (M + 1)
g[1] = 1

for x in range(2, M + 1):
  for cx in range(x, M + 1, x):
    f[cx] += x
  g[x] = f[x] + g[x - 1]

print("\n".join(map(lambda x: str(g[x]), arr)))
