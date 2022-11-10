import sys

N, M = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))
print(arr)


def search(arr, q, s, e):
  if s > e:
    return -1

  m = (s + e) // 2
  v = sum(map(lambda x: max(x - m, 0), arr))

  print(f"m {m}, v {v}")
  if v < q:
    print(f"[too small] s {s}, e {m-1}")
    return search(arr, q, s, m - 1)
  if v > q:
    print(f"[too much] s {m+1}, e {e}")
    ans = search(arr, q, m + 1, e)
    return m if ans == -1 else ans
  else:
    return m


print(search(arr, M, 0, max(arr) - 1))
