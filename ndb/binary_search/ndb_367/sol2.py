import sys

input = sys.stdin.readline
N, x = map(int, input().split())
arr = list(map(int, input().split()))

s, e = 0, N - 1
l, r = -1, -1
# left
while s <= e:
  mid = (s + e) // 2
  print(s, mid, e)
  if x < arr[mid]:
    s, e = s, mid - 1
  elif x > arr[mid]:
    s, e = mid + 1, e
  else:
    if mid == 0 or arr[mid - 1] < x:
      l = mid
      break
    else:
      s, e = s, mid - 1

if l == -1:
  print(-1)
else:
  s, e = 0, N - 1
  # right
  while s <= e:
    mid = (s + e) // 2
    if x < arr[mid]:
      s, e = s, mid - 1
    elif x > arr[mid]:
      s, e = mid + 1, e
    else:
      if mid == N - 1 or arr[mid + 1] > x:
        r = mid
        break
      else:
        s, e = mid + 1, e
  print(r - l + 1)
