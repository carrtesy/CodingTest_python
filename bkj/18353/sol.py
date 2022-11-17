N = int(input())
arr = list(map(int, input().split()))

INF = int(1e9)
dp = [INF] * N
dp[0] = 0


def search(arr, i):
  print(f"i: {i}, dp: {dp}")
  if i <= 0:
    return 0
  if dp[i] != INF:
    return dp[i]

  # take i
  p = arr[i]
  j = i - 1
  while j > 0:
    if arr[j] > p:
      break
    j -= 1
  sol1 = search(arr, j) + (i - j - 1)

  # abandon i
  sol2 = search(arr, i - 1) + 1
  print(f"i: {i}, j: {j}, sol1: {sol1}, sol2: {sol2}")
  dp[i] = min(sol1, sol2)
  return dp[i]


print(search(arr, N - 1))

print(dp)
