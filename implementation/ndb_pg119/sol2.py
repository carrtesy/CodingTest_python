import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A, B, d = map(int, input().split())
maps = []
for _ in range(N):
  maps.append(list(map(int, input().split())))
maps[A][B] = -1

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
cnt = 1
while True:
  print(d, A, B)
  prev_d = d
  for _ in range(4):
    d = (d + 1) % 4
    _A, _B = A + dr[d], B + dc[d]
    if 0 <= _A and _A < N and 0 <= _B and _B < M:
      if maps[_A][_B] not in [-1, 1]:
        A, B = _A, _B
        maps[A][B] = -1
        cnt += 1
        break
  if prev_d == d:
    _A, _B = A + dr[(d + 2) % 4], B + dc[(d + 2) % 4]
    if 0 <= _A and _A < N and 0 <= _B and _B < M:
      if maps[_A][_B] == 1:
        break
      else:
        A, B = _A, _B

print(cnt)