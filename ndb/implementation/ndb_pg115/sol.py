import itertools

loc = input()
i, j = int(loc[1]) - 1, ord(loc[0]) - ord('a')
print(i, j)

R, C = 8, 8
moves = []
moves += list(itertools.product((2, -2), (1, -1)))
moves += list(itertools.product((1, -1), (2, -2)))

print(moves)
cnt = 0
for m in moves:
  di, dj = m
  i_, j_ = i+di, j+dj
  if (0 <= i_ and i_ < R) and (0 <= j_ and j_ < C):
    cnt+=1
print(cnt)