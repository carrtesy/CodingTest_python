import sys

N = int(input())
coord = sorted(list(map(int, sys.stdin.readline().split())))

minidx, mindist = -1, 999999999
for i in range(N):
  dist = sum(map(lambda x: abs(x - coord[i]), coord))
  if dist < mindist:
    minidx, mindist = coord[i], dist

print(minidx)