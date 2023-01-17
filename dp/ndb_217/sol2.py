X = int(input())
dp = [-1] * (X + 1)

dp[1] = 0
dp[2], dp[3], dp[5] = 1, 1, 1


def go(i):
  if dp[i] != -1:
    return dp[i]
  else:
    a, b, c, d = 999999, 999999, 999999, 999999
    if i % 5 == 0:
      a = go(i // 5) + 1
    if i % 3 == 0:
      b = go(i // 3) + 1
    if i % 2 == 0:
      c = go(i // 2) + 1
    d = go(i - 1) + 1
    dp[i] = min(a, b, c, d)
    return dp[i]


print(go(X))
print(dp)
