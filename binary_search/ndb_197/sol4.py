import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
M = int(input())
req = list(map(int, input().split()))

arr.sort()

for r in req:
  s, e = 0, N - 1
  while s <= e:
    print(s, e)
    m = (s + e) // 2
    if r < arr[m]:
      s, e = s, m - 1
    elif r > arr[m]:
      s, e = m + 1, e
    else:
      print("yes")
      break
  print("no")
