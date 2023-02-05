import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
  arr.append(list(map(int, input().split())).sort(reverse=True))


if N == 1:
  print(arr[0][0])
else:
  cnt = 1
  i, j = N-1, arr[-1].index(max(arr[-1]))
  a, b = (i, j), (i, j)
  while cnt != N:
    cand1 = 
    cnt += 1