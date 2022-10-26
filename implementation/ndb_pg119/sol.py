N, M = map(int, input().split())
x, y, h = map(int, input().split())

maps = []
for i in range(N):
  maps.append(list(map(int, input().split())))

print(maps)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

stop = False
cnt = 0
while True:
  h = (h - 1) % 4
  _h = h

  while True:
    _x, _y = x + dx[_h], y + dy[_h]
    if (0 <= _x and _x < N) and (0 <= _y and _y < M) and (maps[_x][_y] == 0):
      x, y, h = _x, _y, _h
      maps[x][y] = -1
      cnt += 1
      break

    _h = (_h - 1) % 4
    if _h == h:
      _h, h = _h + 1, h + 1
      _x, _y = x + dx[(_h - 2) % 4], y + dy[(_h - 2) % 4]
      if maps[_x][_y] == 1:
        stop = True
      else:
        x, y = _x, _y
      break

  print()
  for m in maps:
    print(m)
  print()

  if stop:
    break

print(cnt)
