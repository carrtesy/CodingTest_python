import sys

input = sys.stdin.readline

loc = str(input())
r, c = int(ord(loc[0]) - ord('a')), int(loc[-1]) - 1
print(r, c)

dr = [1, 1, -1, -1, 2, -2, 2, -2]
dc = [2, -2, 2, -2, 1, 1, -1, -1]

cnt = 0
for a, b in zip(dr, dc):
  nr, nc = r + a, c + b
  if 0 <= nr and nr < 8 and 0 <= nc and nc < 8:
    cnt += 1

print(cnt)
