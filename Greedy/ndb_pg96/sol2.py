import sys

input = sys.stdin.readline

N, M = map(int, input().split())

M = 0
for _ in range(N):
  m = min(list(map(int, input().split())))
  if m > M:
    M = m
print(M)
