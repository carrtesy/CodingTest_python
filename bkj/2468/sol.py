import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 4 + 100)

N = int(input())
arr = []

L, H = 101, 0
for _ in range(N):
  row = list(map(int, input().split()))
  L = min(L, min(row))
  H = max(H, max(row))
  arr.append(row)


def dfs(arr, mask, r, c):
  dr = [0,0,1,-1]
  dc = [1,-1,0,0]

  mask[r][c] = True
  for i in range(4):
    rp, cp = r+dr[i], c+dc[i]
    if 0<=rp<N and 0<=cp<N and (not mask[rp][cp]):
      dfs(arr, mask, rp, cp)
  

ans = 0
for h in range(L-1, H+1):
  subans = 0
  mask = [[False] * N for _ in range(N)]
  for r in range(N):
    for c in range(N):
      if arr[r][c] <= h:
        mask[r][c] = True

  for r in range(N):
    for c in range(N):
      if not mask[r][c]:
        dfs(arr, mask, r, c)
        subans += 1
  
  ans = max(ans, subans)
print(ans)