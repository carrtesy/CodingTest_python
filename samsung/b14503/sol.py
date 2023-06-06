import sys
input = sys.stdin.readline
N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = []
for _ in range(N):
  row = list(map(int, input().split()))
  arr.append(row)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cnt = 0
while True:
  if arr[r][c] == 0:
    arr[r][c] = 2
    cnt += 1

  exist = False
  for i in range(4):
    rp, cp = r + dr[i], c+dc[i]
    if arr[rp][cp] == 0:
      exist = True
      break

  if not exist:
    rp, cp = r - dr[d], c - dc[d]
    if arr[rp][cp] != 1:
      r, c = rp, cp
    else:
      break
  else:
    d = (d+3)%4
    rp, cp = r + dr[d], c + dc[d]
    if arr[rp][cp] == 0:
      r, c = rp, cp

print(cnt)