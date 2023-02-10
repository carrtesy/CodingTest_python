N, M = map(int, input().split())

m = []
for _ in range(N):
  a = list(input())
  r = list(map(int, a))
  m.append(r)
print(m)

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def dfs(r, c, m):
  m[r][c] = 1
  for i in range(4):
    _r, _c = r + dr[i], c + dc[i]
    if 0 <= _r and _r < N and 0 <= _c and _c < M:
      if m[_r][_c] != 1:
        dfs(_r, _c, m)


cnt = 0
for r in range(N):
  for c in range(M):
    if m[r][c] == 0:
      dfs(r, c, m)
      cnt += 1
print(cnt)
