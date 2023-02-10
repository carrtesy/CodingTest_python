import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

T = int(input())

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def dfs(r, c, m):
  m[r][c] = 0
  for i in range(4):
    _r, _c = r + dr[i], c + dc[i]
    if 0 <= _r and _r < M and 0 <= _c and _c < N:
      if m[_r][_c] == 1:
        dfs(_r, _c, m)


while T:
  T -= 1
  M, N, K = map(int, input().split())
  arr = [[0] * N for _ in range(M)]
  for _ in range(K):
    r, c = map(int, input().split())
    arr[r][c] = 1

  cnt = 0
  for r in range(M):
    for c in range(N):
      if arr[r][c] == 1:
        dfs(r, c, arr)
        cnt += 1
  print(cnt)
