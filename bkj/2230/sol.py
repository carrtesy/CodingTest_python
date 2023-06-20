import sys
input = sys.stdin.readline
N, M = map(int, input().split())
s, e = 0, 1
arr = [int(input()) for _ in range(N)]
arr.sort()
min_diff = int(1e10+1)
while s < e <= N:
  diff = arr[e-1] - arr[s]
  if diff >= M:
    if diff < min_diff:
      min_diff = diff
    s += 1
  else:
    e += 1
print(min_diff)