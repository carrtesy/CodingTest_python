import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

s, e = 0, max(arr)
while True:
  m = (s + e) // 2

  cut = sum(map(lambda x: max(0, x - m), arr))

  if cut > M:
    if sum(map(lambda x: max(0, x - (m + 1)), arr)) < M:
      print(m)
      break
    else:
      s, e = m + 1, e
  elif cut < M:
    s, e = s, m - 1
  else:
    print(m)
    break