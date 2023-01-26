import sys

input = sys.stdin.readline
N, x = map(int, input().split())
arr = list(map(int, input().split()))

s, e = 0, N - 1
idx = -1
while s < e:
  mid = (s + e) // 2
  if arr[mid] > x:
    s, e = s, mid - 1
  elif arr[mid] < x:
    s, e = mid + 1, e
  else:
    idx = mid
    break

if idx == -1:
  print(idx)
else:
  lidx, hidx = idx, idx
  while lidx >= 0 and arr[lidx] == x:
    lidx -= 1
  while hidx < N and arr[hidx] == x:
    hidx += 1
  print(hidx - lidx - 1)
